import discord
from discord import Status
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get 

def play_sound(ctx, mp3):
  channel = ctx.message.author.voice.channel
  voice = get(client.voice_clients, guild = ctx.guild)
  source = FFmpegPCMAudio(mp3)
  player = voice.play(source)


