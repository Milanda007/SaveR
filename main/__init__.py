#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 27590454
API_HASH = "11bdf99a73d502d2df4f333b02fd2b2f"
BOT_TOKEN = "6201704107:AAHyEywDMN1DP9aW_EeEWSQsOcDInrriaHo"
SESSION = "AQB3R6Neih5YY6ZpmExttE6ljTN4GkUF3IJdWz_wbXVYDr1aX3Q65y6tKLzcvJRqQChy6D76QJEegwkDYZr8Ct-8wX7RVyMgTPWbgZv9UUoN0SiSibccTTFRlVgVliaNBBH-giUWPg9ypeyVJ6vizf0q99ApZEtFPYSQ2Z_yd0f1xObjNq9-NR1OS-JV6hUSoUXAkgyVZTHp2pXd8NOLR2sGZSHM15g4CCN1TduqjhoC2FMhmr9GVHIrDPQM2DcfGgGsQh93VnEVh1DbxhwekklTZVd6eF_cBIgNxLnmNmOnDnR2smOEK0wTZTjC9SsY56LK5gcDPdX7GmkuNuQCI9v0AAAAAS8Y3EIA"
FORCESUB = "channelforwarded"
AUTH = 5085125698

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
