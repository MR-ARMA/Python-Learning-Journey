![picture](./pictures/youtube-videos.jpg)
# YouTube Downloader

YouTube Downloader is a command-line tool and web application designed to provide users with a simple and efficient way to download videos from YouTube for offline viewing. This project aims to solve the problem of needing to access YouTube videos without an internet connection or wanting to save videos for later viewing.

## Features

- **Command-Line Interface (CLI):** Allows users to download videos directly from the terminal.
- **Web Application:** Provides a user-friendly interface for downloading videos through a web browser.
- **Quality Selection:** Users can choose from various video qualities, including  144p,  240p,  360p,  480p,  720p,  1080p, and the highest available quality.
- **Output Path Customization:** Users can specify the output directory for downloaded videos.
- **Progress Tracking:** Displays the download progress in real-time.

## Installation

### Prerequisites

- Python  3.6 or higher
- pip (Python package installer)

### Installation Steps

1. Clone the repository
2. Navigate to the project directory
3. Install the required packages

## Usage

### Command-Line Interface

To download a video using the CLI, run the following command:

```bash
python main.py -u <video_url> -q <quality> -o <output_path>
```

Replace `<video_url>` with the URL of the YouTube video you want to download, `<quality>` with the desired video quality, and `<output_path>` with the path where you want to save the video.

### Web Application

To run the web application, execute the following command:

```bash
streamlit run src/st_main.py
```


Then, open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
