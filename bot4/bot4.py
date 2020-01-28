import discord
import time
from discord import Status
from discord import FFmpegPCMAudio
from discord.ext import tasks, commands
from discord.utils import get

client = commands.Bot(command_prefix = "!")

online_members = []

# TODO: Add a function to update online_members list

## FUNCTIONS
def play_sound(ctx, mp3):
  channel = ctx.message.author.voice.channel
  voice = get(client.voice_clients, guild = ctx.guild)
  source = FFmpegPCMAudio(mp3)
  player = voice.play(source)
  
  
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
  if "Erq" in online_members:
    print("  Erq is online")
  if "PAN" in online_members:
    print("  PAN is online")


## DISCORD EVENTS

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  current_guild = client.guilds[0]
  user_count = current_guild.member_count
  current_members = current_guild.members
  current_channels = current_guild.channels
  # Get list of users
  for m in current_members:
    if m.status != discord.Status.offline and not m.bot:
      print(m.name)
      online_members.append(m.name)
  # Get list of channels
  for c in current_channels:
    print(c.name, "of category", c.type)
  print('Client logged in on', current_guild.name, "with", len(online_members), "users online out of", user_count)
  list_online.start()
  # Automatically join a voice channel
  general_vchan = current_guild.get_channel(351062875827077123)
  print("Using", general_vchan.name, "voice")
  voice = await general_vchan.connect() #voice is class VoiceState
  source = FFmpegPCMAudio('sounds/mlghorn.mp3')
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
    source = FFmpegPCMAudio('sounds/mlghorn.mp3')
    player = voice.play(source)

@client.command(pass_context=True)
async def son(ctx, son):
  """
  Le gros son du 2-2
  """
  mp3 = 'sounds/'+son
  play_sound(ctx, mp3)


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
