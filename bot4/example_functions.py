# Guild = Server
# Member seems to inherit from User

#######
# Text
#######
@client.command(pass_context=True)
async def coco(ctx):
  await ctx.send("L'homme, l'hermite, la legende!")

#######
# Son
#######
@client.command(pass_context=True)
async def pan(ctx):
  await ctx.send("PAN!")
  channel = ctx.message.author.voice.channel
  if not channel:
    await ctx.send("Not connected to a voice channel")
  voice = get(client.voice_clients, guild = ctx.guild)
  source = FFmpegPCMAudio('sounds/shotgun.mp3')
  player = voice.play(source)

#######
# Login
#######
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

