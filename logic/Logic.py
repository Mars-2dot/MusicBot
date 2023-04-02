import discord
import os
from environs import Env
from discord import voice_client


def parse_ctl(*args):
    env = Env()
    env.read_env()
    for arg in args[0]:
        if arg == "prod":
            return env("MusicBotToken")
        elif arg == "test":
            return env("MusicBotTokenTest")

    raise Exception("Token not found, enter \"prod\" or \"test\"")

class Logic:
    """Implementation of business logic not related to the main coge"""

    def getTime(self, ctx):
        vc = ctx.voice_client

        seconds = vc.source.duration % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            return "%dh %02dm %02ds" % (hour, minutes, seconds)
        else:
            return "%02dm %02ds" % (minutes, seconds)
