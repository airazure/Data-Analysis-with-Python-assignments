import subprocess
import youtube_dl

yt_link = ['https://www.youtube.com/watch?v=jx85qK1ztAc']
with youtube_dl.YoutubeDL() as ydl:
    ydl.download(yt_link)


cmd = "ffmpeg -i 'Which countries have emitted the most CO2-jx85qK1ztAc.mp4' -r 10 youtube_gif.gif"
subprocess.call(cmd, shell = True)
