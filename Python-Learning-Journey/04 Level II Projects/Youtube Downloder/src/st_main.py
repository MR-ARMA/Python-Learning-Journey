import streamlit as st
from pytube import YouTube
from pathlib import Path
from pytube.exceptions import VideoUnavailable

class YouTubeDownloader():
    def __init__(self, url, quality='highest', output_path=None):
        self.quality = quality
        self.url = url
        self.yt = YouTube(url,
                          on_progress_callback=self.on_progress,
                          on_complete_callback=self.on_complete)
        self.output_path = output_path or Path.cwd()
        
    def download(self):
        try:
            self.yt.check_availability()
        except VideoUnavailable:
            st.error(f"Video is unavailable. URL '{self.url}' cannot be found. Please try again.")
            return

        st.write('The download process has started...')
        
        if self.quality == 'highest':
            video_stream = self.yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        else:
            video_stream = self.yt.streams.filter(resolution=self.quality, progressive=True, file_extension='mp4').first()
        
        # You might want to implement a custom progress bar here
        video_stream.download(output_path=self.output_path)

    def on_progress(self, stream, chunk, bytes_remaining):
        # Implement progress bar update here
        pass

    def on_complete(self, stream, file_path):
        st.success(f"Downloading is completed. File is saved at: {file_path}")

def main():
    st.image('https://robots.net/wp-content/uploads/2023/09/how-can-to-download-youtube-videos-1695345612.jpg')
    st.markdown("<h1 style='text-align: center; color: black;'>YouTube Video Downloader</h1>", unsafe_allow_html=True)

    input_url = st.text_input("Enter your YouTube video URL:", "https://www.youtube.com/shorts/pdOWKIDanE8")
    if input_url:
        input_quality = st.radio("Select video quality:", ["144p", "240p", "360p", "480p", "720p", "1080p", "highest"])
        input_output_path = st.text_input("Enter output path (optional):", value="")

        if st.button("Download"):
            test = YouTubeDownloader(url=input_url, quality=input_quality, output_path=input_output_path)
            test.download()

if __name__ == '__main__':
    main()
