import discord
from discord import Status
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get

from bot_funcs import *



TOKEN = 'NjAzMDUxOTI1MjY4ODU2ODQx.XTZx9g.y_dSVCtzTeuK3JTN14Q021GVOqI'
client = commands.Bot(command_prefix = ".")

#def play_sound(ctx, mp3):
#  channel = ctx.message.author.voice.channel
#  voice = get(client.voice_clients, guild = ctx.guild)
#  source = FFmpegPCMAudio(mp3)
#  player = voice.play(source)
  
  

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# Command to make the bot join a voice channel
# Call .join in a channel
@client.command(pass_context=True)
async def join(ctx):
  global voice
  channel = ctx.message.author.voice.channel
  if not channel:
    await ctx.send("Not connected to a voice channel")
  voice = get(client.voice_clients, guild = ctx.guild)
  if voice and voice.is_connected():
    await voice.move_to(channel)
  else:
    voice = await channel.connect()
    source = FFmpegPCMAudio('sounds/mlghorn.mp3')
    player = voice.play(source)

@client.command(pass_context=True)
async def coco(ctx):
  await ctx.send("L'homme, l'hermite, la legende!")
  
@client.command(pass_context=True)
async def pan(ctx):
  await ctx.send("PAN!")
  channel = ctx.message.author.voice.channel
  if not channel:
    await ctx.send("Not connected to a voice channel")
  voice = get(client.voice_clients, guild = ctx.guild)
  source = FFmpegPCMAudio('sounds/shotgun.mp3')
  player = voice.play(source)
  
@client.command(pass_context=True)
async def stfu(ctx):
  play_sound(ctx, 'sounds/stfu.mp3')

@client.command(pass_context=True)
async def gotcha(ctx):
  play_sound(ctx, 'sounds/gotcha.mp3')

@client.command(pass_context=True)
async def no(ctx):
  play_sound(ctx, 'sounds/hellno.mp3')

@client.command(pass_context=True)
async def shackles(ctx):
  play_sound(ctx, 'sounds/dota/shackles1.mp3')

@client.command(pass_context=True)
async def cagette(ctx):
  play_sound(ctx, 'sounds/dota/shackles2.mp3')

@client.command(pass_context=True)
async def lakad(ctx):
  play_sound(ctx, 'sounds/dota/lakad.mp3')

@client.command(pass_context=True)
async def chinanumba1(ctx):
  play_sound(ctx, 'sounds/dota/china_tuyoda.mp3')

@client.command(pass_context=True)
async def oof(ctx):
  play_sound(ctx, 'sounds/oof.mp3')

@client.command(pass_context=True)
async def nutz(ctx):
  await ctx.send("HA!")
  play_sound(ctx, 'sounds/deeznutz.mp3')

@client.command(pass_context=True)
async def xfiles(ctx):
  play_sound(ctx, 'sounds/illuminati.mp3')

@client.command(pass_context=True)
async def gay(ctx):
  play_sound(ctx, 'sounds/gay.mp3')

@client.command(pass_context=True)
async def normies(ctx):
  play_sound(ctx, 'sounds/normies.mp3')

@client.command(pass_context=True)
async def cut(ctx):
  """
  Cut cut cut cut
  """
  play_sound(ctx, 'sounds/dota/cut.mp3')

@client.command(pass_context=True)
async def bag(ctx):
  play_sound(ctx, 'sounds/dota/timber_bag.mp3')

@client.command(pass_context=True)
async def jex(ctx):
  play_sound(ctx, 'sounds/dota/jex.mp3')

@client.command(pass_context=True)
async def welcome(ctx):
  play_sound(ctx, 'sounds/dota/dp_ladies.mp3')

@client.command(pass_context=True)
async def kundalini(ctx):
  play_sound(ctx, 'sounds/dota/Keep_chakramagic_02.mp3')

@client.command(pass_context=True)
async def haha(ctx):
  play_sound(ctx, 'sounds/dota/Dpro_levelup_16.mp3')

@client.command(pass_context=True)
async def hihi(ctx):
  play_sound(ctx, 'sounds/dota/Keep_laugh_06.mp3')

@client.command(pass_context=True)
async def son(ctx, son):
  """
  Le gros son du 2-2
  """
  mp3 = 'sounds/'+son
  play_sound(ctx, mp3)

# Online/Offline
@client.event
async def on_member_update(before, after):
    if str(after.status) == "offline":
        print("{} has gone {}.".format(after.name,after.status))
    if str(after.status) == "online":
        print("{} has gone {}.".format(after.name,after.status))
        if after.name == "Loukkk":
          print("Playing sound for Loukkk")
          voice = get(client.voice_clients, guild = after.guild)
          source = FFmpegPCMAudio('sounds/dota/sky_inthebag.mp3')
          player = voice.play(source)
        elif after.name == "PAN":
          print("Playing sound for PAN")
          voice = get(client.voice_clients, guild = after.guild)
          source = FFmpegPCMAudio('sounds/geazy.mp3')
          player = voice.play(source)
        elif after.name == "Erq":
          print("Playing sound for Erq")
          voice = get(client.voice_clients, guild = after.guild)
          source = FFmpegPCMAudio('sounds/didiersuper.mp3')
          player = voice.play(source)
        elif after.name == "tslt":
          print("Playing sound for Abhaal")
          voice = get(client.voice_clients, guild = after.guild)
          source = FFmpegPCMAudio('sounds/dota/Keep_laugh_06.mp3')
          player = voice.play(source)
  


client.run(TOKEN)
