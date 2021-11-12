import youtube_dl   # pip install youtube_dl

print("Youtube mp4 conventer -- (Hope you gonn download Travis Scott)")
vid_url = input("Youtube linkini giriniz\n>")

vid_info = youtube_dl.YoutubeDL().extract_info(url=vid_url,download=False)

file_name = f"{vid_info['title']}.mp4"

settings ={
    'format':'134',
    'outtmpl':file_name,
}

with youtube_dl.YoutubeDL(settings) as ydl:
    ydl.download([vid_info['webpage_url']])

print(f"Dosya yüklendi: {file_name}")