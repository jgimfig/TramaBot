from pyrogram import Client

import os

API_HASH =  "e7e863f305866da6e453c1028d11cc37"
API_ID = 25564784
token_bot = "6073032396:AAF-VXsRsf1Ze0ujUwL05ScX5Ucy_-NiXl8"

app = Client("trama bot",
        api_hash=os.environ.get('API_HASH', API_HASH),
        api_id=os.environ.get('API_ID', API_ID), bot_token=token_bot)

app.run()