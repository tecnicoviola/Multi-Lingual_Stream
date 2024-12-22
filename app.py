from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from transformers import pipeline
from moviepy import VideoFileClip
from gtts import gTTS
from pydub import AudioSegment
import subprocess

# Load environment variables
load_dotenv(dotenv_path='config/env')

# Flask app initialization
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data/uploads/'
OUTPUT_FOLDER = 'data/output/'  # Output folder for translated audio and video
TEMP_FOLDER = 'data/temp/'  # Temporary folder for intermediate files
ALLOWED_EXTENSIONS = {'mp4', 'mp3'}
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Max file size 50MB

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(TEMP_FOLDER, exist_ok=True)

# Initialize Google Generative AI for translation
google_chat_model = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    api_key=os.getenv('GOOGLE_API_KEY')
)

# Load the Whisper model pipeline for speech-to-text
speech_to_text = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large-v3",
    device=-1  # Use GPU if available
)

# Function to process audio file
def transcribe_audio(file_path):
    result = speech_to_text(file_path)
    return result['text']

# Function to translate text using Google Generative AI
def translate_text(text, target_language):
    prompt = f"Translate the following text to {target_language}:\n\n{text}"
    response = google_chat_model.predict(prompt)
    return response

# Function to convert text to speech using gTTS
def convert_to_audio(text, output_file="output.mp3"):
    tts = gTTS(text, lang='hi')  # Change 'lang' as needed for the target language
    tts.save(output_file)
    return output_file

# Function to adjust audio speed to match duration
def adjust_audio_speed(audio_file, target_duration, output_file="adjusted_audio.mp3"):
    output_file = os.path.join(TEMP_FOLDER, output_file)  # Save adjusted audio in TEMP_FOLDER
    audio = AudioSegment.from_file(audio_file)
    current_duration = audio.duration_seconds
    speed_factor = current_duration / target_duration

    # Adjust speed
    adjusted_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed_factor)
    }).set_frame_rate(audio.frame_rate)

    adjusted_audio.export(output_file, format="mp3")
    return output_file

# Function to convert MP4 video to MP3 audio
def convert_video_to_audio(video_file_path, output_audio_file="output_audio.mp3"):
    video = VideoFileClip(video_file_path)
    video.audio.write_audiofile(output_audio_file)
    return output_audio_file

# Function to replace the audio in the original video with translated audio
def replace_audio_in_video(original_video_path, translated_audio_path, output_video_path="output_video.mp4"):
    output_video_path = os.path.join(OUTPUT_FOLDER, output_video_path)
    command = [
        "ffmpeg",
        "-y",  # Overwrite output files without asking
        "-i", original_video_path,
        "-i", translated_audio_path,
        "-c:v", "copy",  # Copy video stream without re-encoding
        "-map", "0:v:0",  # Use the video stream from the first input
        "-map", "1:a:0",  # Use the audio stream from the second input
        output_video_path
    ]
    subprocess.run(command, check=True)
    return output_video_path

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle file upload and processing
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        target_language = request.form.get('target_language')

        if not file or not allowed_file(file.filename):
            return jsonify({'error': 'Unsupported file type. Please upload an MP4 or MP3 file.'})

        # File size limit check
        if file.content_length > app.config['MAX_CONTENT_LENGTH']:
            return jsonify({'error': 'File is too large. Maximum size is 50MB.'})

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        try:
            if filename.endswith('.mp4'):
                # Process video file
                audio_file = convert_video_to_audio(file_path, os.path.join(OUTPUT_FOLDER, "output_audio.mp3"))
                transcription = transcribe_audio(audio_file)
                
                translated_text = translate_text(transcription, target_language)
                
                translated_audio_file = os.path.join(OUTPUT_FOLDER, "translated_audio.mp3")
                convert_to_audio(translated_text, output_file=translated_audio_file)
                
                video = VideoFileClip(file_path)
                adjusted_audio_file = adjust_audio_speed(translated_audio_file, video.audio.duration)
                
                final_video_file = replace_audio_in_video(file_path, adjusted_audio_file, "final_video.mp4")

                video_url = f'/data/output/{os.path.basename(final_video_file)}'
                return jsonify({'success': True, 'video_url': video_url})  # Send JSON response with video URL
            else:
                return jsonify({'error': 'Unsupported file type. Only MP4 files are supported for now.'})
        except Exception as e:
            app.logger.error(f"Error during file processing: {str(e)}")
            return jsonify({'error': f'Error during processing: {str(e)}'})

    return render_template('index.html')

# Route to serve output files
@app.route('/data/output/<filename>')
def serve_output(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

# Main program entry point
if __name__ == "__main__":
    app.run(debug=True)
