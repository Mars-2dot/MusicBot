import asyncio
import os
import sys

import discord

from discord.ext import commands
from cogs.Bot import Music
from logic import Logic


async def setup(bot):
    asyncio.create_task(bot.add_cog(Music(bot)))


if __name__ == '__main__':
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    asyncio.run(setup(bot))
    bot.run(Logic.parse_ctl(sys.argv))
