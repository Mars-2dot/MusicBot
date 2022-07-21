settings = {
    'token': 'OTA0NzY0Njc2MDE2MDcwNjU2.YYARxA.4PpNo0ZW3RRZFyXOu20k_jcEIc8',
    'bot': 'GreenTeaBot',
    'id': 904764676016070656,
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
    'cookiefile': 'youtube.com_cookies.txt'
}

ytdloptsPL = {
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
    "extract_flat": True,
    'username': 'botgeshka@mail.ru',
    'password': 'onyxlotus2664',
    'cookiefile': 'youtube.com_cookies.txt',


}

ffmpegopts = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 100",
    'options': '-vn'
}