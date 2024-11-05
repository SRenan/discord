import discord
import asyncio
from discord import FFmpegPCMAudio
from discord.ext import commands, tasks
from utils import utils


class Random(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.homies = utils.homies()

  @commands.command(aliases = ["Paris", "PARIS", "paris", "Jtan", "Laboheme"])
  async def noisy(self, ctx):
    """
    ICI C PARIS!
    """
    paris_image = '../images/noisy_le_sec.png'
    paris_sound = '../sounds/paris_est_magique.mp3'
    discord_file = discord.File(paris_image, filename="le_voisin.jpg")
    await ctx.channel.send(file=discord_file, delete_after=10)
    vc = await ctx.author.voice.channel.connect()
    source = FFmpegPCMAudio(paris_sound)
    player = vc.play(source)
    while vc.is_playing():
      await asyncio.sleep(.5)
    await vc.disconnect()

  @commands.command(aliases = ["boulogne", "Boulogne", "92"])
  async def abhaal(self, ctx):
    """
    92 EN FORSS!
    """
    boul_sound = '../sounds/boulogne_est_magique.mp3'
    vc = await ctx.author.voice.channel.connect()
    source = FFmpegPCMAudio(boul_sound)
    player = vc.play(source)
    while vc.is_playing():
      await asyncio.sleep(.5)
    await vc.disconnect()

async def setup(bot):
  await bot.add_cog(Random(bot))
