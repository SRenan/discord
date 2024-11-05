import discord
import time
import os
import asyncio
from discord import Status
from discord import FFmpegPCMAudio
from discord.ext import tasks, commands
from discord.utils import get
from utils import utils


class Sounds(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.homies = utils.homies()

  async def play_sound(self, ctx, mp3):
    voice = await ctx.author.voice.channel.connect()
    source = FFmpegPCMAudio(mp3)
    player = voice.play(source)

  @commands.command()
  async def list_mp3(self, ctx):
    """
    List available audio files for !son
    """
    sons = [f for f in os.listdir('../sounds') if f.endswith('.mp3')]
    await ctx.channel.send(sons)

  @commands.command()
  async def son(self, ctx, son):
    """
    Le gros son du 2-2
    """
    mp3 = '../sounds/'+son
    mp3_ext = os.path.splitext(mp3)[1]
    if(mp3_ext != ".mp3"):
      mp3 = mp3+'.mp3'
    vc = await ctx.author.voice.channel.connect() #vc class VoiceClient
    source = FFmpegPCMAudio(mp3)
    player = vc.play(source)
    while vc.is_playing():
      await asyncio.sleep(.5)
    await vc.disconnect()

  @commands.Cog.listener() #Use instead of '@bot.events' inside cogs
  async def on_voice_state_update(self, member, before, after):
    homies_names = [ item['name'] for item in self.homies]
    if member.name in homies_names:
      if before.channel == None and after.channel != None:
        print(after.channel.name)
        # Get matching dictionary from list
        homie = next(item for item in self.homies if item["name"] == member.name)
        mp3 = homie["intro"]
        try:
          vc = await after.channel.connect()
          source = FFmpegPCMAudio(mp3)
          player = vc.play(source)
          while vc.is_playing():
            await asyncio.sleep(.2)
          await vc.disconnect()
        except discord.Forbidden:
          print(f'Error while joining the voicechannel: {e}')
        except discord.ClientException:
          print(f'Error. Bot already playing sound: {e}')
        except Exception as e:
          print(f'Error trying to join a voicechannel: {e}')

async def setup(bot):
  await bot.add_cog(Sounds(bot))
