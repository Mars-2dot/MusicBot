import discord
from discord import voice_client


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
