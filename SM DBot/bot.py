from secrets import *
from func import *
import commands
from commands import *
import discord
from discord.ext import commands
import asyncio

@bot.event
async def on_ready():
    print("__________________")
    print("Logged in as: ")
    print(bot.user.name)
    print(bot.user.id)
    print("___________________")

run(TOKEN)