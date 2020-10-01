import youtube_dl
import subprocess


def run():
    # ask the user for the video they need to download
    video_url = input("Please enter the Youtube Video URL:")
    # download and convert to mp3 and store in downloads folder
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options)as ydl:
        ydl.download([video_info['webpage_url']])
    # open the file once it has been downloaded
    subprocess.call(["open", filename])


if __name__ == '__main__':
    run()
