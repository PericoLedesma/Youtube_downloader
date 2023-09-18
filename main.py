# YouTube downloader
'''

Video tutorial:https://www.youtube.com/watch?v=NtzDjNhPZgU

'''

# Libraries
from pytube import YouTube
from pathlib import Path
from colorama import init, Fore # Color font
import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment #Para recortar el audio
import subprocess

# Files
from shazam_API import * # Trying to extract real names

# CODE
def convert_video_to_audio_moviepy(video_file, destiny_path, output_ext="mp3"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{destiny_path}.{output_ext}")

def on_complete(stream, file_path):
    print('Download completed')
    print('\tFile path: ', file_path)
    print(' ')
    return file_path

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'\tDownloading... {round((stream.filesize - bytes_remaining) / stream.filesize * 100)}'
    print(progress_string)

def cutting_lenght(video_object, file_path):
    print(" Cutting length....")

    sound = AudioSegment.from_file(file_path, format="mp4")
    EndSec = video_object.length  # en segundos

    # Time to milliseconds conversion
    EndTime = StrtMin * 60 * 1000 + EndSec * 1000

    # Opening file and extracting portion of it
    extract = sound[0:EndTime]
    print(" Done")

    print(" Exporting to mp4...")
    os.remove(file_path)  # First we remove
    extract.export((str(file_path_audio_itunes) + "/" + video_object.title + ".mp4"), format="mp4")
    print(" Done")


def convert_video_to_audio_ffmpeg(file_path, file_path_audio_itunes, output_ext="wav"):
    """Converts video to audio directly using `ffmpeg` command
    with the help of subprocess module"""

    print("Destination path...")
    basename = os.path.basename(file_path)
    destination_path = os.path.join(file_path_audio_itunes, os.path.splitext(basename)[0])

    print("Extracting audio from video....")
    subprocess.call(["ffmpeg", "-y", "-i", file_path, f"{destination_path}.{output_ext}"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    print("Removing previous file...")
    os.remove(file_path)
    print(" Done")

def main():
    print(' ')
    print(Fore.RED + '------------YOUTUBE DOWNLOADER------------'+Fore.RESET)

    # Download paths
    download_directory = Path('/Users/pedrorodriguezdeledesmajimenez/Downloads')
    file_path_TV_auto_import = Path('/Users/pedrorodriguezdeledesmajimenez/Movies/TV/Media.localized/Automatically Add to TV.localized')
    file_path_audio_itunes = Path('/Users/pedrorodriguezdeledesmajimenez/Music/Music/Media.localized/Automatically Add to Music.localized')

    downloading = True
    while downloading:
        URL = input("Enter video URL: ")
        video_object = YouTube(URL,
                               on_complete_callback=on_complete,
                               on_progress_callback=on_progress)

        # Video Information
        print('Video information...')
        print(f'\tTitle: {video_object.title}')
        print(f'\tLength: {video_object.length / 60} minutes')
        print(f'\tAuthor: {video_object.author}')
        # print(video_object.description)

        download_choice = input('Download video(v) or audio(a): ')

        if download_choice == 'v' or download_choice == 'V':
            video_object.streams.get_highest_resolution().download(output_path=file_path_TV_auto_import)
        elif download_choice == 'a' or download_choice == 'A':
            # Downloading as audio the length is incorrect.
            '''
            file_path = video_object.streams.get_audio_only().download(output_path=file_path_audio_itunes)
            cutting_lenght(video_object, file_path)
            '''
            file_path = video_object.streams.get_highest_resolution().download(output_path=download_directory)
            convert_video_to_audio_ffmpeg(file_path, file_path_audio_itunes)



        other = input('Other video ? (Y/N)')
        if other == 'y' or other == 'Y':
            downloading = True
        elif other == 'n' or other == 'N':
            downloading = False
        else:
            print('Error. Quitting')
            downloading = False

# --------------------------------------------------
if __name__ == '__main__':
    print('Running script...l')
    # Get_song()
    # quit()

    main()
    print('**End**')


