from pytube import YouTube
from sys import argv
import os

yt = YouTube(str(input("Enter the URL of the video that you wish to download: ")))

video = yt.streams.filter(only_audio=True).first()

out_file = video.download(output_path="C:\Python projects\Songs and videos\songs")

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " has been successfully downloaded.")


