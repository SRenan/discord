import discord
from discord import Status
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = "!")


def play_sound(ctx, mp3):
  channel = ctx.message.author.voice.channel
  voice = get(client.voice_clients, guild = ctx.guild)
  source = FFmpegPCMAudio(mp3)
  player = voice.play(source)
  
  

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

TOKEN = 'NjAzMDUxOTI1MjY4ODU2ODQx.XTZx9g.y_dSVCtzTeuK3JTN14Q021GVOqI'
client.run(TOKEN)
