from pytube import YouTube
import os

try:
    link = input("Enter link of the Video : ")
    youtube_1 = YouTube(link)

    print(f'Title is : {youtube_1.title}')

    inp = input("Enter v for video and a for audio : ")

    if (inp == 'v'):
        print("Please Wait......")
        youtube_1.streams.filter(res='720p').first().download(filename_prefix='video')
        print("Video Download Complete")

    elif (inp == 'a'):
        print("Please Wait......")
        out_file = youtube_1.streams.filter(only_audio=True).first().download(filename_prefix='audio')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("Audio Download Complete")

    else:
        print("Enter valid input, v for video and a for audio")

except:
    print("Enter valid input")
