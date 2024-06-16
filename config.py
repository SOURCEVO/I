from pyrogram import Client
from Plugin.databesas import *
from Plugin.api import *
import os 

SUDO = 1321338802 # admin or sudo id
CHANNLS_BOT = ['radfx2'] # bot channls 
API_KEY = '7186812281:AAGPWo9CGnYFjfBUR1rJXlfakez2RnyZ4Sk'  # API_KEY OR BOT_TOKN 


if not os.path.exists('./.session'):
    os.mkdir('./.session')

if not os.path.exists('./.databesas'):
    os.mkdir('./.databesas')

app = Client(
    '.session/rad',
    bot_token=API_KEY, # API_KEY 
    api_hash='ba86e5ea56ce780c45371caea695bcd7', # UserBot api_hahs
    api_id='21477147' # UserBot api_id 
)

datas, apiV = databesas(), TempMailApi()


