import discord
import os
import urllib.parse, urllib.request, re 
import json

from discord.ext.commands.core import guild_only
from config import settings
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

client = commands.Bot(command_prefix='!') 

players = {}

YDL_OPTIONS = { 'format': 'worstaudio/best', 'noplaylist': 'True', 'simulate': 'True', 'preferredquality': '192', 
                'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = { 'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
SETTING_FILE = 'settings.json'
PLAYLIST_PATH = 'playlists/'

currentTrack = 1
currentPlayList = ''
queue = []
isPlayList = False

if not os.path.exists(PLAYLIST_PATH):
    os.mkdir(PLAYLIST_PATH)

def writeJson(namePlayList, track):
    with open(PLAYLIST_PATH + namePlayList + '.json') as f:
        list = json.load(f) 
    list.insert(1, track)
    
    with open(PLAYLIST_PATH + namePlayList + '.json', 'w') as f:
        json.dump(list, f)

def readJson(namePlayList):
    with open(PLAYLIST_PATH + namePlayList + '.json') as f:
        list = json.load(f)
        return list

def getTitleVideo(url):
    with YoutubeDL() as ydl:
      info_dict = ydl.extract_info(url, download=False)
      video_title = info_dict.get('title', None)
      return video_title

def loadPlayList(namePlayList):
    path = PLAYLIST_PATH + namePlayList + '.json'
    if os.path.exists(path) and os.path.getsize(SETTING_FILE) > 0:
        with open(path) as f:
            playList = json.load(f)
            return playList
    else:
        return False

async def checkAndStartPlay(ctx, list):
    if list != False:
        if len(list) > 0:
            await p(ctx, list[int(currentTrack - 1)])
        else:
            await ctx.send('Playlist is empty')
    else:
        await ctx.send('There is no such playlist')

async def stopPlay(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()

async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@client.event 
async def on_ready():
    print('Bot online')

@client.command()
async def j(ctx):
    join(ctx)
    
@client.command()
async def disconnect(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients,guild=ctx.guild)
    if voice and voice.is_connectec():  
        voice = await channel.disconnect()
    else:
        await ctx.send('Fail try...')

@client.command()
async def p(ctx, url):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing ' + url)
    else:
        await ctx.send("Bot is already playing")
        return

@client.command()
async def r(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')

@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')

@client.command()
async def s(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Messages have been cleared")
    
@client.command()
async def yt(ctx, *, search):
    global isPlayList
    isPlayList = False
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    query_string = urllib.parse.urlencode({'search_query': search})
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                    htm_content.read().decode())
    # await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])   
    url = 'http://www.youtube.com/watch?v=' + search_results[0]
    print(url)
    
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing http://www.youtube.com/watch?v=' + search_results[0])
    else:
        queue.append(url)
        await ctx.send('Add to queue')
        return

@client.command()
async def cpl(ctx, namePlayList):
    list = []
    with open(PLAYLIST_PATH + namePlayList + '.json', 'w') as f:
        json.dump(list, f)
        await ctx.send('Play list was created with name: ' + namePlayList)

@client.command()
async def apl(ctx, namePlayList, link):
    writeJson(namePlayList, link)
    await ctx.send('Track - ' + link + ' was recorded in playlist: ' + namePlayList)

@client.command()
async def lpl(ctx, namePlayList):
    list = readJson(namePlayList)
    await ctx.send("In playlist " + namePlayList + ' ' + str(len(list)) + ' traks')
    count = 1

    for track in list:
        countStr = str(count)
        await ctx.send(countStr + ': ' + getTitleVideo(track))
        count += 1

@client.command()
async def spl(ctx, namePlayList):
    global isPlayList
    isPlayList = True
    writeJson('settings', namePlayList)
    list = readJson(namePlayList)
    p(ctx, list[0])

@client.command()
async def ppln(ctx, namePlayList, number):
    global isPlayList
    isPlayList = True
    global currentPlayList
    global currentTrack
    currentPlayList = namePlayList
    currentTrack = int(number)

    list = loadPlayList(namePlayList)

    await checkAndStartPlay(ctx, list)

@client.command()
async def ppl(ctx, namePlayList):
    global isPlayList
    isPlayList = True
    global currentPlayList
    global currentTrack
    currentPlayList = namePlayList
    currentTrack = 1

    list = loadPlayList(namePlayList)

    await checkAndStartPlay(ctx, list)

@client.command()
async def next(ctx):
    global currentTrack

    if isPlayList:
        await stopPlay(ctx)
        global currentPlayList
        playList = loadPlayList(currentPlayList)
        currentTrack += 1

        if len(playList) < currentTrack:
            currentTrack = 1

        await ppln(ctx, currentPlayList, currentTrack)
    else:
        global queue
        if len(queue) != 0:
            if len(queue) >= currentTrack:
                await stopPlay(ctx)
                await p(ctx, queue[currentTrack - 1])
                currentTrack += 1
                await ctx.send(currentTrack)
                await ctx.send(len(queue))
            else:
                await ctx.send("There are no more tracks in the queue")
        else:
            await ctx.send("Queue is empty")

@client.command()
async def allpl(ctx):
    playLists = os.listdir(PLAYLIST_PATH)
    if len(playLists) > 0:
        count = 1
        for playList in playLists:
            name = playList.split('.')[0]
            await ctx.send(str(count) + ': ' + name + ' contains: ' + str(len(loadPlayList(name))) + ' traks')
            count += 1
    else:
        await ctx.send('There is not a single playlist')

@client.command()
async def traceQueue(ctx):
    global queue
    await ctx.send(queue)

@client.command()
async def clear(ctx):
    global queue
    queue.clear
    await ctx.send('Queue was empty')

@client.command()
async def clear(ctx):
    global queue
    queue.pop
    await ctx.send('Last track was empty')

@client.command()
async def h(ctx):
    await ctx.send(
        "Базовые комманды: \n!h - помощь \n!p [url] - воспроизводит музыку по указанной ссылке\n!yt [search arg] - производит поиск по ютубу и воспроизводит самый реливантный ответ" +
        "\n\nПлейлисты: \n!cpl [name playlist] - создает плейлист с указынным именем\n!apl [name playlist] [url] - добавляет в указанный плейлист ссылку\n" +
        "!lpl [name playlist] - содержимое плейлиста\n!ppln [name playList] [number track] - воспроизводит конкретный трек по номеру из списка, номер можно узнать командой !lpl" +
        "\n!ppl [name playList] - воспроизводит указанный трек с начала\n!next - воспроизводит следующий по очереди трек в плейлисте, плейлист зациклен, поэтому при использовани комманды\n"+
        "находясь на последнем треке плейлист будет восприозведен с начала\n!allpl - список существующих плейлистов"
    )

client.run(settings['token'])  