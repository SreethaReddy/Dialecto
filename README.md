# Dialecto – AI Powered Subtitle Generator for Low-Resource Languages

## Overview

**Dialecto** is an AI-powered system that converts video content into regionally accurate subtitles for low-resource local languages. The project focuses on improving accessibility by generating subtitles that are linguistically correct and culturally relevant for underrepresented communities.

Dialecto combines speech recognition, language detection, machine translation, and subtitle synchronization to automatically generate subtitles from video content. The system is designed to help bridge accessibility gaps in education, media, and digital content platforms.

---

## Features

* Automatic conversion of video speech into subtitle text
* Supports multilingual video input
* Generates subtitles in underrepresented regional languages
* AI-based speech-to-text transcription
* Automatic language detection
* Machine translation pipeline
* Subtitle timestamp synchronization
* Subtitle export in `.srt` format

---

## Project Workflow

1. Upload or provide a video file.
2. Extract audio from the video.
3. Convert speech to text using a speech recognition model.
4. Detect the source language of the transcript.
5. Translate the transcript into the selected regional language.
6. Synchronize the translated text with video timestamps.
7. Generate a subtitle file (`.srt`).

---

## Project Structure

```
Dialecto/
│
├── app.py              # Main application logic
├── subtitles.srt       # Generated subtitle output
├── README.md           # Project documentation
│
├── templates/          # Frontend HTML templates
│
└── utils/              # Utility modules
    ├── speech_to_text.py
    ├── translator.py
    ├── subtitle_sync.py
```

---

## Technologies Used

* Python
* Speech Recognition Models
* Machine Translation APIs / Models
* Natural Language Processing (NLP)
* Subtitle Processing (.srt)

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/Dialecto.git
cd Dialecto
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

---

## Example Use Case

1. Upload a lecture video in English.
2. Dialecto transcribes the spoken content.
3. The system translates the text into a regional language.
4. A subtitle file is generated and synchronized with the video.

---

## Impact

Dialecto aims to improve accessibility for regional audiences by supporting low-resource languages. The system helps provide subtitles for educational content, digital media, and online platforms, enabling better understanding for speakers of local languages.

---

## Future Improvements

* Real-time subtitle generation
* Support for additional regional language models
* Speaker recognition and diarization
* Integration with video streaming platforms
* Improved translation accuracy for dialect-specific expressions

---

## Author

Sreetha Reddy

GitHub: https://github.com/SreethaReddy

---

## License

This project is released under the MIT License.
