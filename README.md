# MultiStream: Speech-to-Speech Streaming Platform
## **Description**:
This repository implements a web application that enables real-time, multilingual communication through video content. It leverages cutting-edge Natural Language Processing (NLP) and Artificial Intelligence (AI) techniques to seamlessly process, translate, and integrate speech across different languages within video files.

### **How it Works:**
1. **Upload an MP4 video and choose a target language.**
2. **The application extracts audio, converts it to text, translates it, and generates synthetic speech in your chosen language.**
3. **Audio speed is adjusted to match the video, and the translated audio is seamlessly integrated into a new video.**
4. **Download your translated video!**

### **Technology Stack:**
*   **Backend Framework:** Flask (Python web framework)
*   **Speech-to-Text:** Whisper (Automatic Speech Recognition model)
*   **Multilingual Translation:** Google Generative AI (AI for text translation)
*   **Text-to-Speech:** gTTS (Python library for text-to-speech generation)
*   **Video Processing:** MoviePy (Python library for video editing)
*   **Audio Processing:** pydub (Python library for audio manipulation)
---
### **Getting Started:**

1.  **Clone the Repository:**

    ```bash
    git clone https://your-username/speech-to-speech-streaming.git
    ```

2.  **Install Dependencies:**

    ```bash
    cd speech-to-speech-streaming
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables:**

    *   Create a `.env` file in the project root directory.
    *   Add the line `GOOGLE_API_KEY=<your_google_api_key>` within the `.env` file, replacing `<your_google_api_key>` with your actual Google Cloud API Key.

4.  **Run the Application:**

    ```bash
    python app.py
    ```

    This will start the web application, typically accessible at `http://127.0.0.1:5000/` in your web browser.
---
### **Usage/Screenshots:**

#### 1.  Choose a file & upload your video:
![image](https://github.com/user-attachments/assets/b7ac0cbb-96af-4792-b7ce-7e8026890584)


#### 2.  Select your target language:
![image](https://github.com/user-attachments/assets/52fc7da5-1b1b-4428-b468-df4cb95ea1be)

#### 3.  Processing : The application processes the video, does translation, and video integration.
![image](https://github.com/user-attachments/assets/cdebca49-71ae-4dd5-ac48-9d295b47bfe1)

#### 4.  View the translated video: A download link will be provided upon completion.
![image](https://github.com/user-attachments/assets/d15d8f5c-68aa-4c98-8ad3-95b33c70fd7c)

---
## **Future Improvements:**

*   **Real-Time Processing:** Implement real-time speech-to-speech streaming.
*   **Improved TTS Models:** Integrate advanced neural TTS models for more natural speech synthesis.
*   **Dynamic Language Support:** Add more languages and dialects for translation.
*   **Optimized Video Integration:** Enhance the synchronization process to handle more complex videos.
*   **Interactive UI:** Develop a web-based interface for user-friendly interaction.

## **Acknowledgments:**

*   **Open Source Communities:** For the tools and libraries that made this project possible.

## **Additional Notes:**

*   The current implementation supports MP4 video files for processing.
*   The maximum file size for upload is limited to 50MB.
