import discord
import time
from discord.ext import commands, tasks
#import keyboard
#from pynput import keyboard
import sys

# NOTE: I can get create_task to work but it doesn't recognize functions within cogs
def test():
  print("Test")


# pynput
#def on_press(key):
#    try:
#        print('alphanumeric key {0} pressed'.format(
#            key.char))
#    except AttributeError:
#        print('special key {0} pressed'.format(
#            key))



class keyboard_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  

  async def keypress_detector():
    print("Looping")
    #while True:
    #  try:  
    #    if keyboard.is_pressed('z'):
    #      print("Pressed")
    #      #await bot.get_channel('dev').send("PRESS")
    #    else:
    #      pass
    #  except Exception as ex:
    #    return print(str(ex))

  @commands.command()
  async def listen_kb(self, ctx):
    print("Listening")
    #while 1:
    #  x=sys.stdin.read(1)[0]
    #  print("You pressed", x)
    #  if x == "r":
    #    print("If condition is met")
    #print(self.bot.loop)
    #await self.bot.loop.create_task(keypress_detector())
    #while True:
    #  try:  
    #    if keyboard.is_pressed('z'):
    #      print("Pressed")
    #      #await bot.get_channel('dev').send("PRESS")
    #    else:
    #      pass
    #  except Exception as ex:
    #    return print(str(ex))

def setup(bot):
  bot.add_cog(keyboard_cog(bot))
