import discord
import time
import os
import asyncio
from discord import Status
from discord.ext import tasks, commands
from discord.utils import get



class Europa(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def f10(self, ctx, code):
    print("screenshots")
    # handle bad code
    # Post image to channel

async def setup(bot):
  await bot.add_cog(Europa(bot))
