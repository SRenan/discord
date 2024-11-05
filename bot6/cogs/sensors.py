import discord
from discord.ext import commands, tasks
import RPi.GPIO as GPIO
import time


class Sensors(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def photo(self, ctx):
    """
    Measure ambiant light
    """
    resistorPin = 7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(resistorPin, GPIO.OUT)
    GPIO.output(resistorPin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(resistorPin, GPIO.IN)
    currentTime = time.time()
    diff = 0
    # >2 = dark
    # 1500 = petite lumiere
    # 1400 = grande lumiere
    # 830 = 2 lumieres
    # ? = jour
    while(GPIO.input(resistorPin) == GPIO.LOW and diff < 2):
        diff  = time.time() - currentTime
    if(diff >= 2):
      msg = "Dark"
    else:
      msg = round(diff * 1000, 3) # Value in ms
    time.sleep(1)
    await ctx.send(msg)

async def setup(bot):
  await bot.add_cog(Sensors(bot))
