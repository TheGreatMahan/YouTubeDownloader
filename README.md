# YouTube Video Downloader

## Overview
This application provides a simple graphical user interface (GUI) to download YouTube videos directly to a selected directory on your computer. It allows users to enter the URL of a YouTube video, select a directory, and download the video in the best available quality.

## Features
- **URL Input**: Enter the URL of the desired YouTube video.
- **Directory Selection**: Browse and select a directory where the video will be saved.
- **Video Download**: Download the video in the highest available quality, combining video and audio if necessary.

## Dependencies
This project requires the following software and libraries:
- Python 3.x
- PyQt5
- yt-dlp
- ffmpeg (for video and audio merging)

### Installing Dependencies

#### Python
Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

#### PyQt5
PyQt5 can be installed via pip. Run the following command in your terminal:

```bash
pip install PyQt5
```

#### yt-dlp
yt-dlp is used for downloading videos from YouTube. Install it using pip:

```bash
pip install yt-dlp
```

#### ffmpeg
ffmpeg is required for merging video and audio streams when downloading the best quality. 

##### Windows
1. Download ffmpeg from [FFmpeg.org](https://ffmpeg.org/download.html).
2. Extract the downloaded zip to a known location (e.g., `C:\ffmpeg`).
3. Add the bin folder (e.g., `C:\ffmpeg\bin`) to your system's PATH.
   - Search for 'Environment Variables' in Windows search and select "Edit the system environment variables".
   - Click on "Environment Variables".
   - Under "System variables", find and select "Path", then click "Edit".
   - Click "New" and add the path to the ffmpeg bin directory.
   - Click "OK" to close all dialogs.

##### macOS
Install ffmpeg using Homebrew:

```bash
brew install ffmpeg
```

##### Linux
Use the package manager to install ffmpeg. For Ubuntu, for example:

```bash
sudo apt update
sudo apt install ffmpeg
```

## Running the Application
To run the application, navigate to the project directory and run the script via Python:

```bash
python app.py
```

Ensure you are in the correct directory and have all dependencies installed as described above.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
