from discord.ext import commands


def play_sound(ctx, mp3):
  channel = ctx.message.author.voice.channel
  voice = get(bot.voice_bots, guild = ctx.guild)
  source = FFmpegPCMAudio(mp3)
  player = voice.play(source)

# Command to make the bot join a voice channel
# Call .join in a channel
@bot.command(pass_context=True)
async def join(ctx):
  global voice
  channel = ctx.message.author.voice.channel
  if not channel:
    await ctx.send("Not connected to a voice channel")
  voice = get(bot.voice_bots, guild = ctx.guild)
  if voice and voice.is_connected():
    await voice.move_to(channel)
  else:
    voice = await channel.connect()
    source = FFmpegPCMAudio('sounds/mlghorn.mp3')
    player = voice.play(source)

