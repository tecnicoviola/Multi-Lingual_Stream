# Speech-to-Speech Streaming in Multilingual Contexts
## Description:
This repository contains the implementation and documentation of our internship project at Infosys Springboard. The project focuses on building a multilingual speech-to-speech streaming system. It leverages modern NLP and AI techniques to process, translate, and re-integrate speech in different languages seamlessly.

## Project Overview:
### Key Objectives:
1.Process multimedia content and extract speech components.

2.Translate extracted speech into multiple languages.

3.Reintegrate the translated speech back into the original video.

### Learning Milestones:
###   1.Project Foundations:

1.In-depth exploration of key concepts like ingestion, retrieval, basic agent functionality, and agent memory.

2.Hands-on learning with tools and frameworks to set the foundation for the project.

### 2.Implementation Steps:

### Speech Extraction:
1.Extracted audio from video files and converted it to MP3 format.

2.Utilized tools to isolate speech from MP3 files.

### 3.Speech-to-Text Conversion:
1.Used pre-trained models (e.g., Hugging Face Transformers) for high-accuracy speech-to-text processing.

### 4.Multilingual Translation:
Applied translation models to convert text to the desired target languages.

### 5.Text-to-Speech Generation:
Generated speech in the target language using state-of-the-art text-to-speech (TTS) models.

### 6.Video Integration:
Synchronized the translated speech back into the original video to produce a seamless multilingual output.


## Advanced Learnings:

### LangGraph:
Explored and implemented graph-based NLP workflows for processing complex language transformations.

Created a mini-project using LangGraph to understand its capabilities better.

### AI Models Used:
1.Hugging Face models for natural language understanding and generation.

2.TTS models and libraries for high-quality speech generation.

3.Additional tools and APIs for audio and video processing.

4.Mini-Project on LangGraph-based Speech Workflow

5.Developed a mini-project using LangGraph to visualize and execute a speech-to-speech translation pipeline. This helped us understand graph-based workflows for complex AI tasks.

## Technologies & Tools

Python

Hugging Face Transformers

LangGraph

Text-to-Speech Libraries (e.g., gTTS, Google Cloud TTS)

Video Processing Libraries (e.g., FFmpeg)

APIs for multilingual translation (Google Translate API, DeepL, etc.


## How to Use

### Clone the repository:
git clone https://github.com/your-username/speech-to-speech-streaming.git

cd speech-to-speech-streaming

### Install dependencies:
pip install -r requirements.txt

### Run the scripts in sequence:
python scripts/extract_audio.py
python scripts/speech_to_text.py
python scripts/translate.py
python scripts/text_to_speech.py
python scripts/integrate_video.py
