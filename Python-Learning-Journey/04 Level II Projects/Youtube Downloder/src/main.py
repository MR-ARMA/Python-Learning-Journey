from pytube import YouTube

class YouTubeDownloader():
    def __init__(self, url, quality = None, output_path = None):
        self.quality = quality or '144p'
        self.url = url
        self.yt = YouTube(url)
        self.output_path = output_path or '.'
        
    def download(self):
        
        if self.quality == 'highest':
            video_stream = self.yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        else:
            video_stream = self.yt.streams.filter(resolution=self.quality, progressive=True, file_extension='mp4').first()
            
        video_stream.download(output_path=self.output_path)
        
def main():
    test = YouTubeDownloader('https://www.youtube.com/shorts/GYg_YisJRck')
    test.download()

if __name__ == '__main__':
    main()

