import os
from datetime import datetime
import ffmpeg
from pytube import YouTube

def download_youtube_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")

        # Generate the output file name using the current timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d-%H%M%S")
        output_file = f"{timestamp}.mp4"

        # Download the video with the specified output file name
        video.download(filename=output_file)

        print(f"Download complete: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to download the video.")


def download_youtube_audio(url):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        print(f"Downloading: {yt.title}")

        # Download the audio file
        audio_file = audio.download(filename="temp_audio")

        # Generate the output file name using the current timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d-%H%M%S")
        output_file = f"{timestamp}.mp3"

        # Convert the audio file to MP3
        ffmpeg.input(audio_file).output(output_file).run()

        # Remove the temporary audio file
        os.remove(audio_file)

        print(f"Download complete: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to download the audio.")


url = input("Please enter the YouTube video URL: ")
option = input("Type 1 for mp3 or 2 for mp4: ")

if option == '1':
    download_youtube_audio(url)
elif option == '2':
    download_youtube_video(url)
else:
    print('Nothing was selected.')
