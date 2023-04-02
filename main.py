import asyncio
import discord

from discord.ext import commands
from cogs.Bot import Music

async def setup(bot):
    asyncio.create_task(bot.add_cog(Music(bot)))


if __name__ == '__main__':
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    asyncio.run(setup(bot))
    bot.run("OTAzOTM5NDQxODQyODc2NDg4.GJVneV.Hj8zgevgMP1rdVE2fhnxCVpKfxO3-_EyhK3F8Y")
