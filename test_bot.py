import discord
from discord.ext import commands


TOKEN = 'NjAzMDUxOTI1MjY4ODU2ODQx.XTZx9g.y_dSVCtzTeuK3JTN14Q021GVOqI'
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('Hello!')

#@client.event
#async def on_member_join(member):
#  channel = member.server.get_channel(351062875827077123)
#  await @client.send_message

@client.command(pass_context=True)
async def join(ctx):
  channel = ctx.message.author.voice.voice_channel
  await client.join_voice_channel(channel)

#async def on_member_join(get_user(102487892823126016)):
#  await message.channel.send("@realRonaldTrump")
#async def on_member_join("584818782032363530"):
#  await message.channel.send("PAN!")
#
#async def on_member_join("212102090577805312"):
#  await message.channel.send("Erq: Le man! l'hermite! la legende!")
#

client.run(TOKEN)
