import discord
import time
import os
import RPi.GPIO as GPIO
from functions import *
from discord import Status
from discord import FFmpegPCMAudio
from discord.ext import tasks, commands
from discord.utils import get

## GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

## DISCORD
intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!", intents = intents)

online_members = []

@tasks.loop(seconds=60.0)
async def list_online():
  # Recounting
  # Need to access some of the context there. I think client is exposed.
  recount_members = client.guilds[0].members
  online_members.clear()
  for m in recount_members:
    if m.status != discord.Status.offline and not m.bot:
      online_members.append(m.name)
  # Printing
  print("There are", len(online_members), "users online")

@tasks.loop(seconds=5.0)
async def list_onvoice():
  for vc in client.guilds[0].voice_channels:
    vc_mnames = [m.name for m in vc.members]
    #print(vc_mnames)
    if "Erq" in vc_mnames or "PAN" in vc_mnames or "Loukkk" in vc_mnames:
      led_blink(1)
  


## DISCORD EVENTS

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  current_guild = client.guilds[0]
  user_count = current_guild.member_count
  current_members = current_guild.members
  current_channels = current_guild.channels
  # Start loops
  list_online.start()
  list_onvoice.start()
  # Automatically join a voice channel
  general_vchan = current_guild.get_channel(351062875827077123)
  print("Using", general_vchan.name, "voice")
  voice = await general_vchan.connect() #voice is class VoiceState
  source = FFmpegPCMAudio('../sounds/mlghorn.mp3')
  player = voice.play(source)

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
    source = FFmpegPCMAudio('../sounds/mlghorn.mp3')
    player = voice.play(source)

@client.command(pass_context=True)
async def son(ctx, son):
  """
  Le gros son du 2-2
  """
  mp3 = '../sounds/'+son
  mp3_ext = os.path.splitext(mp3)[1]
  if(mp3_ext != ".mp3"):
    mp3 = mp3+'.mp3'
  play_sound(ctx, mp3)

@client.command(pass_context=True)
async def list_son(ctx):
  """
  List available audio files for !son
  """
  sons = [f for f in os.listdir('../sounds') if f.endswith('.mp3')]
  await ctx.channel.send(sons)
  


# When user joins channel
async def on_voice_state_update(member, before, after):
    if str(after.VoiceState) == None:
        print("{} has left the channel.".format(after.name))
    if str(after.VoiceState) != None:
        print("{} has joined the channel.".format(after.name))

# Online/Offline
@client.event
async def on_member_join(member):
  print(member.name, "joined", member.guild, "as", member.nick)

## RUN THE BOT
token_file = open("token.txt")
TOKEN = token_file.read().strip()
client.run(TOKEN)
