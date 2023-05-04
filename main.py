from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, client,  filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
import pyrogram
from pyrogram import Client, filters
from details import api_id, api_hash, bot_token
# from dotenv import load_dotenv
import tgcrypto
from p_bar import progress_bar
from subprocess import getstatusoutput
import helper
import logging
import time
import aiohttp
import asyncio
import aiofiles
from pyrogram.types import User, Message
import os
bot = Client(
    "bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

logger = logging.getLogger()

os.makedirs("./downloads", exist_ok=True)

@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Hello im txt file downloader\nPress /pyro to download links listed in a txt file in the format **Name:link**\n\nBot made by - ")
        


@bot.on_message(filters.command(["pyro"]))
async def account_login(bot: Client, m: Message):
    editable = await bot.ask(m.chat.id, "Send txt file**")
    x = await editable.download()
    await editable.delete(True)
    

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)        
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable1 = await bot.ask(m.chat.id, f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")            
    raw_text = editable1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0
    
    
    editable2 = await bot.ask(m.chat.id, "Enter Title")    
    raw_text0 = editable2.text    
    input2=await bot.ask(m.chat.id, "**Enter resolution**")    
    raw_text2 = input2.text

    input6= await bot.ask(m.chat.id, "Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")    
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
           
    count =int(raw_text)    
    try:
        for i in range(arg, len(links)):
        
            url = links[i][1]
            name = links[i][0].replace("\t", "")
                # await m.reply_text(name +":"+ url)

            Show = f"**Downloading:-**\n\n**Name :-** ```{name}\nQuality - {raw_text2}```\n\n**Url :-** ```{url}```"
            prog = await m.reply_text(Show)
            cc = f'>> **Name :** {name}\n>> **Title :** {raw_text0}\n\n>> **Index :** {count}'
            
            
            if "youtu" in url:
                if raw_text2 in ["144", "240", "480"]:
                    ytf = f'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]'
                elif raw_text2 == "360":
                    ytf = 18
                elif raw_text2 == "720":
                    ytf = "22/18"
                else:
                    ytf = 18
            else:
                ytf=f"bestvideo[height<={raw_text2}]"
#             try:
            if "jwplayer" in url:
                if raw_text2 in ["180", "144"]:
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf = f"{out['320x180 ']}/{out['256x144 ']}"
                    except Exception as e:
                        if e==0:
                            raw_text2=="no"
                elif raw_text2 in ["240", "270"]:
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf = f"{out['480x270 ']}/{out['426x240 ']}"
                    except Exception as e:
                        if e==0:
                            raw_text=="no"
                elif raw_text2 == "360":
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf = out['640x360 ']
                    except Exception as e:
                        if e == 0:
                            raw_text2=="no"
                        #cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
                elif raw_text2 == "480":
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf = f"{out['960x540 ']}/{out['852x480 ']}"
                    except Exception as e:
                        if e==0:
                            raw_text2=="no"
                    # cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
                elif raw_text2 == "720":
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf = f"{out['1280x720 ']}"
                    except Exception as e:
                        if e==0:
                            raw_text2=="no"
                    # cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
                elif raw_text2 == "1080":
                    try:
                        cmd = f'yt-dlp -F "{url}"'
                        k = await helper.run(cmd)
                        out = helper.vid_info(str(k))
                        ytf =f"{out['1920x1080 ']}/{['1920x1056']}"
                    except Exception as e:
                        if e==0:
                            raw_text2=="no"
                else:
                   # cmd = f'yt-dlp -F "{url}"'
                   # k = await helper.run(cmd)
                    #out = helper.vid_info(str(k))
                   # ytf = out['640x360 ']
                    #cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
                    raw_text2=="no"
#             except Exception as e:
#                 print(e)
            

            if ytf == f'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]':
                cmd = f'yt-dlp -o "{name}.mp4" -f "{ytf}" "{url}"'

            # elif "jwplayer" in url:# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
            #     cmd=f'yt-dlp -o "{name}.mp4" "{url}"'    
            elif "adda247" in url:# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
                cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
            elif "kdcampus" or "streamlock" in url:
                cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
            elif ".pdf" in url: #and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
                cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
            elif "drive" in url:
                cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
            elif raw_text2 == "no":# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
                cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
#             elif "unknown" in ytf:
#                 cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -o "{name}.mp4" -f "{ytf}+bestaudio" "{url}"'

            
            
                # download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                # os.system(download_cmd)
            try:
                if cmd == f'yt-dlp -o "{name}.pdf" "{url}"' or "drive" in url:
#                 if "drive" in url:
                    try:
                        ka=await helper.download(url)
                        await prog.delete (True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(ka, caption=f'>> **File :** {name}\n>> **Title :** {raw_text0}\n\n>> **Index :** {count}')
                        count+=1
                        # time.sleep(1)
                        await reply.delete (True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif cmd == f'yt-dlp -o "{name}.pdf" "{url}"' or ".pdf" in url:
                    try:
                        ka=await helper.aio(url)
                        await prog.delete (True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(ka, caption=f'>> **File :** {name}\n>> **Title :** {raw_text0}\n\n>> **Index :** {count}')
                        count+=1
                        # time.sleep(1)
                        await reply.delete (True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    try:
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                        os.system(download_cmd)
                        filename = f"{name}.mp4"
                        subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
                        await prog.delete (True)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        try:
                            if thumb == "no":
                                thumbnail = f"{filename}.jpg"
                            else:
                                thumbnail = thumb
                        except Exception as e:
                            await m.reply_text(str(e))

                        dur = int(helper.duration(filename))
            #                         await prog.delete (True)
                        start_time = time.time()
                        await m.reply_video(f"{name}.mp4",caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur, progress=progress_bar,progress_args=(reply,start_time))
                        count+=1
                        os.remove(f"{name}.mp4")

                        os.remove(f"{filename}.jpg")
                        await reply.delete (True)
                        time.sleep(1)
                    except Exception as e:
                        await m.reply_text(f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - ```{url}```")
                        continue
            except Exception as e:
                await m.reply_text(str(e))
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")


bot.run()
