
# Media Transcriber

Media Transcriber is a macOS application built with Python that processes audio and video files, transcribes them using the Whisper model, and outputs the transcriptions in a structured format.

## Features
- Transcribes audio and video files using the Whisper model.
- Outputs transcriptions as `.json` files with timestamps and text.
- Supports media files in various formats.

## Prerequisites

Before running the application, ensure that you have the following installed on your macOS system:

- Python 3.12 or later
- [ffmpeg](https://ffmpeg.org/download.html) for media file conversion
- Whisper model (installed via the `whisper` Python package)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BSaikiran22/MediaTranscriber.git
   cd MediaTranscriber/src
Install dependencies: Install the required Python libraries by running:

bash
Copy
Edit
pip install -r requirements.txt
Install ffmpeg: Follow the instructions on the ffmpeg website to install ffmpeg on your macOS machine.

Usage
To run the app, use the following command:

bash
Copy
Edit
python app.py
This will begin the transcription process. The results will be saved as a .json file with the transcription text.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Fork the repository.
Create your feature branch (git checkout -b feature-name).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-name).
Create a new Pull Request.
vbnet
Copy
Edit

This README should provide clear instructions on setting up the project and using it. If you're interested in additional sections (like testing, usage examples, or contributing guidelines), we can expand on it.

### 2. **Add License File**:
If you haven’t added a license yet, consider adding an MIT license, which is widely used in open-source projects. To do this:

- Create a `LICENSE` file in the root directory of your project.
- Copy the following text into the `LICENSE` file:

```txt
MIT License

Copyright (c) [year] [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
3. Create a New Branch for Features:
If you're planning to add more features, it's a good idea to create a new branch:

bash
Copy
Edit
git checkout -b add-new-feature
4. Push Your Changes to GitHub:
Once you have updated the README.md and added the LICENSE file, you can commit the changes and push them to GitHub:

bash
Copy
Edit
git add README.md LICENSE
git commit -m "Updated README and added LICENSE file"
git push -u origin master
5. Track Issues and Projects on GitHub:
You can create issues for bugs, features, or tasks you'd like to complete. You can also use GitHub Projects to organize them into a Kanban-style board.

To create an issue:

Go to the Issues tab in your GitHub repository.
Click New Issue and provide a title and description.
You can assign labels, milestones, and even assignees to keep track of progress.
Let me know if you need more details on any of the steps, or if you'd like to add anything specific to your project!
python app.py
This will transcribe the provided media files and save the transcription as a .json file.
