import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

settings = {
    'bot': 'GreenTeaBot',
    'id': 904764676016070656,
    'prefix': '!'
}

settingsTest = {
    'bot': 'GreenTeaBot',
    'id': 903939441842876488,
    'prefix': '!'
}

ytdlopts = {
    'format': 'worstaudio/best',
    'restrictfilenames': True,
    'simulate': 'True',
    'preferredquality': '192',
    'preferredcodec': 'mp3',
    'key': 'FFmpegExtractAudio',
    'noplaylist': True,
    'logtostderr': False,
    'default_search': 'auto',
    # 'playlist-start': 1
    # "extract_flat": True
    'username': 'botgeshka@mail.ru',
    'password': 'onyxlotus2664',
    'cookiefile': 'settings/cookies.txt'
}

ffmpegopts = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 100",
    'options': '-vn'
}