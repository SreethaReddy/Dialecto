# Dialecto – AI Powered Subtitle Generator for Low-Resource Languages

## Overview

**Dialecto** is an AI-powered subtitle generation system designed to convert video content into regionally accurate subtitles for low-resource and underrepresented languages. The system improves accessibility by automatically generating subtitles that are linguistically meaningful and culturally relevant.

Dialecto integrates speech recognition, language detection, machine translation, and subtitle synchronization to produce subtitle files in `.srt` format. The project aims to bridge language barriers in education, digital media, and online content platforms.

---

## Features

* Automatic conversion of video speech into text
* Supports multilingual video input
* Generates subtitles for regional and low-resource languages
* AI-based speech-to-text transcription
* Automatic language detection
* Machine translation pipeline
* Subtitle timestamp synchronization
* Export subtitles in `.srt` format
* Simple web interface for video upload and subtitle generation

---

## Project Workflow

1. Upload a video file through the web interface.
2. Extract audio from the video.
3. Convert speech into text using a speech recognition model.
4. Detect the source language automatically.
5. Translate the transcript into the desired regional language.
6. Synchronize translated text with timestamps.
7. Generate subtitles in `.srt` format.
8. Display the generated output to the user.

---

## Project Structure

```text
Dialecto/
│
├── app.py                    # Main Flask application
├── subtitles.srt             # Generated subtitle output
├── README.md                 # Project documentation
│
├── templates/                # HTML templates
│   ├── index.html            # Upload page
│   └── result.html           # Output page
│
└── utils/                    # Utility modules
    ├── processor.py          # Audio extraction and speech processing
    └── subtitle_generator.py # Translation and subtitle generation
```

---

## Module Description

### app.py

Acts as the central controller of the application.

Responsibilities:

* Accept video uploads.
* Coordinate processing modules.
* Generate subtitle files.
* Render results to the user interface.

---

### processor.py

Handles preprocessing tasks such as:

* Audio extraction from video.
* Speech-to-text conversion.
* Source language detection.

---

### subtitle_generator.py

Responsible for:

* Translating transcripts into regional languages.
* Synchronizing subtitles with timestamps.
* Generating `.srt` subtitle files.

---

### index.html

Provides the user interface for:

* Uploading videos.
* Selecting processing options.
* Starting subtitle generation.

---

### result.html

Displays:

* Generated subtitles.
* Output results.
* Downloadable subtitle files.

---

## Technologies Used

* Python
* Flask
* Speech Recognition Models
* Machine Translation APIs / Models
* Natural Language Processing (NLP)
* Subtitle Processing (.srt)
* HTML and CSS

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Dialecto.git
cd Dialecto
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

---

## Example Use Case

1. Upload an English lecture video.
2. Dialecto extracts the audio.
3. Speech is converted into text.
4. The transcript is translated into a regional language.
5. Subtitle timestamps are generated automatically.
6. A synchronized `.srt` subtitle file is created and displayed.

---

## Applications

* Educational videos
* Online learning platforms
* Regional media content
* Social media videos
* Podcasts and interviews
* Accessibility for hearing-impaired users

---

## Impact

Dialecto aims to improve digital accessibility by supporting low-resource languages. It enables regional audiences to access educational and multimedia content in their native languages, reducing language barriers and promoting inclusivity.

---

## Future Improvements

* Real-time subtitle generation
* Support for additional regional languages
* Speaker recognition and diarization
* Integration with video streaming platforms
* Improved translation accuracy for dialect-specific expressions
* Multi-speaker subtitle support

---

## Author

**Sreetha Reddy**

GitHub: https://github.com/SreethaReddy

---

## License

This project is released under the MIT License.

