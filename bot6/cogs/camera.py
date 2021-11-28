import discord
import os
import asyncio
import time
import cv2
from discord import Status
from discord.ext import tasks, commands
from discord.utils import get
from utils import utils

cascade_dir="/home/srenan/programs/opencv/data/haarcascades/"


class Camera(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.homise = utils.homies()

  @commands.command()
  async def snapshot(self, ctx):
    print("Taking pic")
    fname = "/home/srenan/shared/wcam0.jpg"
    cmd = "fswebcam -r 1280x720 --no-banner " + fname
    os.system(cmd)
    # Post picture on discord if user has permission
    author = ctx.author
    author_name = author.name
    role_names = [r.name for r in author.roles]
    print("Roles:", role_names)
    if 'snap' in role_names:
      print(f'{author_name} taking a picture')
      discord_file = discord.File(fname, filename="image.jpg")
      await ctx.channel.send(file=discord_file, delete_after=10)
    else:
      print(f'{author_name} does not have permission to take picture')


  @commands.command()
  async def detect(self, ctx):
    face_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_eye.xml')
    ubody_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_upperbody.xml')
    fbody_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_fullbody.xml')
    print("Detecting ppl")
    fname = "/home/srenan/shared/wcam0.jpg"
    cmd = "fswebcam -r 1280x720 --no-banner " + fname
    os.system(cmd)
    # openCV
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
    ubody = ubody_cascade.detectMultiScale(gray, 1.1, 4)
    fbody = fbody_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
       cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    for (x, y, w, h) in eyes:
       cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    for (x, y, w, h) in ubody: #
       cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
    for (x, y, w, h) in fbody: #black
       cv2.rectangle(img, (x, y), (x+w, y+h), (1, 1, 1), 2)
    cv2.imwrite(fname, img)
    # Post picture on discord if user has permission
    author = ctx.author
    author_name = author.name
    role_names = [r.name for r in author.roles]
    print("Roles:", role_names)
    if 'snap' in role_names:
      print(f'{author_name} taking a picture')
      discord_file = discord.File(fname, filename="image.jpg")
      await ctx.channel.send(file=discord_file, delete_after=10)
    else:
      print(f'{author_name} does not have permission to take picture')
    msg = "Detected: " + str(len(faces))+ " faces, " + \
                         str(len(eyes)) + " eyes, " + \
                         str(len(ubody)) + " upper bodies, " + \
                         str(len(fbody)) + " full bodies."
    await ctx.send(msg)


  @commands.command()
  async def test_cmd(self, ctx):
    author = ctx.author
    author_name = author.name
    print(f'{author} testing')
    roles = author.roles
    print(roles)
    role_names = [r.name for r in roles]
    print(role_names)
    if 'snap' in role_names:
      print(f'{author_name} taking a picture')
    else:
      print(f'{author_name} does not have permission to take picture')
    

def setup(bot):
  bot.add_cog(Camera(bot))
