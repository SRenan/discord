import discord
import time
import RPi.GPIO as GPIO
from discord.ext import commands, tasks

## GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.OUT) #Active buzzer


def led_blink(uptime = 1):
  GPIO.output(8, GPIO.HIGH)
  time.sleep(uptime)
  GPIO.output(8, GPIO.LOW)

def buzz(pin = 12, uptime = 0.5):
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(uptime)
  GPIO.output(pin, GPIO.LOW)


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
      if any(x in vc_mnames for x in ["PAN","Erq",".erq","pan2800"]):
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

  @commands.command()
  async def buzz(self, ctx):
    await ctx.send("bzzz")
    buzz(uptime = 0.5)


async def setup(bot):
  await bot.add_cog(online_users(bot))
