from secrets import *
import discord
from discord.ext import commands
import asyncio


bot = commands.Bot(command_prefix="%")
help = "-präfix = %\n" \
       "-test = test ob der Bot an ist\n" \
       "-mal/minus/mal/geteilt/hoch2 = kleiner Rechner\n" \
       "-raten = rate eine Zahl von 1 bis 10"


def run(TOKEN):
    bot.run(TOKEN)
