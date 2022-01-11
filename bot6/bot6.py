import discord
import time
import os
from discord.ext import commands

botdir="/home/srenan/workspace/discord/bot6/"
os.chdir(botdir)


## DISCORD
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

## Cogs
for file in os.listdir("cogs"):
  if file.endswith(".py"):
    name = file[:-3]
    bot.load_extension(f"cogs.{name}")
  
## RUN THE BOT
token_file = open("token.txt")
TOKEN = token_file.read().strip()
try:
  bot.run(TOKEN)
except Exception as e:
  print(f'Error when logging in: {e}')

