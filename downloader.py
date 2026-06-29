import os
import requests
import yt_dlp

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
VIDEO_URL = os.environ["VIDEO_URL"]

output = "video.mp4"

ydl_opts = {
    "outtmpl": output,
    "format": "best[ext=mp4]/best"
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([VIDEO_URL])

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"

with open(output, "rb") as video:
    requests.post(
        url,
        data={
            "chat_id": CHAT_ID
        },
        files={
            "video": video
        }
    )
