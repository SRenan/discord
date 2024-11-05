import discord
import asyncio
import logging
import sys
import time
import os
from discord.ext import commands

botdir="/home/pi/mygit/discord/bot6/"
os.chdir(botdir)


## DISCORD
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

## Cogs
async def load_extensions():
  for file in os.listdir("cogs"):
    if file.endswith(".py"):
      name = file[:-3]
      await bot.load_extension(f"cogs.{name}")
  

## Logging
root = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
root.addHandler(handler)

## RUN THE BOT
token_file = open("token.txt")
TOKEN = token_file.read().strip()

async def main():
  async with bot:
    await load_extensions()
    await bot.start(TOKEN)

try:
  asyncio.run(main())
except Exception as e:
  print(f'Error when logging in: {e}')

