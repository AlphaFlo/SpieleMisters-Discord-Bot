from func import *
import asyncio
import discord
import random


@bot.command()
async def test(bot):
    await bot.send("TEST!")
    au = bot.message.author
    print(au, "test: %test")
@bot.command()
async def plus(bot, z1: int, z2: int):
    await bot.send(z1 + z2)
    au = bot.message.author
    print(au, "plus: ", z1, "+", z2)
@bot.command()
async def minus(bot, z1: int, z2: int):
    await bot.send(z1 - z2)
    au = bot.message.author
    print(au, "minus: ", z1, "-", z2)
@bot.command()
async def mal(bot, z1: int, z2: int):
    await bot.send(z1 * z2)
    au = bot.message.author
    print(au, "mal: ", z1, "*", z2)
@bot.command()
async def geteilt(bot, z1: int, z2: int):
    await bot.send(z1 / z2)
    au = bot.message.author
    print(au, "geteilt: ", z1, "/", z2)
@bot.command()
async def hoch2(bot, z1: int):
    await bot.send(z1 * z1)
    au = bot.message.author
    print(au, "hoch2: ", z1, "²")
@bot.command()
async def raten(bot,input: int):
    rzahl = random.randint(1, 10)
    au = bot.message.author
    if input == rzahl:
        await bot.send("Richtig!")
        print(au, "raten: ", input)
    else:
        await bot.send("Falsch!")
        await bot.send(rzahl)
        print(au, "raten: ", input, "/", rzahl)
@bot.command()
async def hilfe(bot):
    await bot.send(help)
@bot.command()
async def coin(bot):
    coin = random.randint(1, 2)
    au = bot.message.author
    if coin == 1:
        await bot.send("Zahl")
        print(au, "coin: Zahl")
    else:
        await bot.send("Kopf")
        print(au, "coin: Kopf")