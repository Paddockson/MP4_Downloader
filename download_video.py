import os
import sys
import yt_dlp

def download_dailymotion_video(url):
    # Path to Downloads folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
        'format': 'mp4',  # ensure MP4 output
    }

    # Download video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    # Get URL from arguments or ask user
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        video_url = input("Enter Dailymotion video URL: ").strip()

    download_dailymotion_video(video_url)
