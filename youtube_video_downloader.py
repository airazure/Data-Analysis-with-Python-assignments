import youtube_dl 
yt_link = ['https://www.youtube.com/watch?v=7ZSKZA0b_mk']
with youtube_dl.YoutubeDL() as ydl:
    ydl.download(yt_link)
    
ffmpeg -ss 5 -t 1 -i 'Which countries have emitted the most CO2?-jx85qK1ztAc.mkv' youtube_gif.gif