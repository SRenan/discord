import discord
import os
import asyncio
import time
from discord import Status
from discord.ext import tasks, commands
from discord.utils import get
from utils import utils



class Camera(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.homise = utils.homies()

  @commands.command()
  async def snapshot(self, ctx):
    print("Taking pic")
    fname = "/home/srenan/shared/wcam0.jpg"
    cmd = "fswebcam -r 1280x720 --no-banner " + fname
    os.system(cmd)
    discord_file = discord.File(fname, filename="image.jpg")
    await ctx.channel.send(file=discord_file, delete_after=10)

def setup(bot):
  bot.add_cog(Camera(bot))
