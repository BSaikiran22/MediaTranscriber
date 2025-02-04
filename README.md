
# Media Transcriber

A simple Windows application that processes media files (audio/video), transcribes them using Whisper, and saves the transcription in a structured format.

## Features
- Transcribes audio and video files using Whisper.
- Outputs transcription results in JSON format.

## Prerequisites
- macOS
- Python 3.12+
- ffmpeg (for processing media files)
- Whisper model

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BSaikiran22/MediaTranscriber.git
   cd MediaTranscriber/src
Install required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Make sure ffmpeg is installed on your machine.

Usage
To run the application:

bash
Copy
Edit
python app.py
This will transcribe the provided media files and save the transcription as a .json file.
