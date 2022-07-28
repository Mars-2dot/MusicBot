import os

from cogs.Bot import Music
from settings.Config import bot


def setup(bot):
    bot.add_cog(Music(bot))


if __name__ == '__main__':
    setup(bot)
    bot.run(os.environ["MusicBotTokenTest"])
