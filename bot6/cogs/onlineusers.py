import discord
import time
import RPi.GPIO as GPIO
from discord.ext import commands, tasks

## GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)


def led_blink(uptime = 1):
  GPIO.output(8, GPIO.HIGH)
  time.sleep(uptime)
  GPIO.output(8, GPIO.LOW)


class online_users(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.list_onvoice.start()

  #@tasks.loop(seconds = 15.0)
  #async def list_onvoice(self):
  #  try:
  #    for vc in self.bot.guilds[0].voice_channels:
  #      vc_mnames = [m.name for m in vc.members]
  #      if any(x in vc_mnames for x in ["PAN","Erq"]):
  #        print("Homies online")
  #        led_blink(1)
  #  except Exception as e:
  #    print(f'Error: {e}')

  @tasks.loop(seconds = 15.0)
  async def list_onvoice(self):
    guilds = self.bot.guilds
    for vc in guilds[0].voice_channels:
      vc_mnames = [m.name for m in vc.members]
      if any(x in vc_mnames for x in ["PAN","Erq"]):
        print("Homies online")
        led_blink(1)



  #Because self.bot.guilds is empty until bot is readu
  @list_onvoice.before_loop
  async def before_list_onvoice(self):
    print('waiting...')
    await self.bot.wait_until_ready()

  @commands.command()
  async def ping(self, ctx):
    await ctx.send("pong")


def setup(bot):
  bot.add_cog(online_users(bot))
