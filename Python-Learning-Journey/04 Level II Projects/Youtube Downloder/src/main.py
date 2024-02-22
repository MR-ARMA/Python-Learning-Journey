from pytube import YouTube
from pathlib import Path

class YouTubeDownloader():
    def __init__(self, url, quality = None, output_path = None):
        self.quality = quality or 'highest'
        self.url = url
        self.yt = YouTube(url,
                          on_progress_callback=self.on_progress,
                          on_complete_callback=self.on_complete)
        self.output_path = output_path or Path.cwd()
        
    def download(self):
        
        if self.quality == 'highest':
            video_stream = self.yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        else:
            video_stream = self.yt.streams.filter(resolution=self.quality, progressive=True, file_extension='mp4').first()
          
        video_stream.download(output_path=self.output_path)

    def on_progress(self, stream, chunk, byte_remaining):
        total_size = stream.filesize
        byte_downloaded = total_size - byte_remaining
        print(f"progress: {100*(byte_downloaded / total_size)}")

    def on_complete(self, stream, file_pass):
        total_size = stream.filesize
        print()
        print(f"Downloading is completed in this path:{self.output_path}")
        print(f"size of file: {int(total_size / 1024 / 1024)}MB")
        
        
def main():
    test = YouTubeDownloader('https://www.youtube.com/shorts/pdOWKIDanE8')
    test.download()

if __name__ == '__main__':
    main()

