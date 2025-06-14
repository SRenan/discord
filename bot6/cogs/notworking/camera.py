import discord
import os
import asyncio
import time
import opencv as cv2
import dlib
import numpy as np
#from mtcnn.mtcnn import MTCNN
from discord import Status
from discord.ext import tasks, commands
from discord.utils import get
from utils import utils

cascade_dir="/home/pi/programs/opencv/data/haarcascades/"
model_dir="/home/pi/programs/models/"

def detect_dlib(img):
  detector = dlib.get_frontal_face_detector()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = detector(gray, 1) # result
  #to draw faces on image
  for result in faces:
    x = result.left()
    y = result.top()
    x1 = result.right()
    y1 = result.bottom()
    cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
  return(faces)

def detect_dnn(img):
  modelFile  = model_dir + "res10_300x300_ssd_iter_140000.caffemodel"
  configFile = model_dir + "deploy.prototxt.txt"
  net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
  h, w = img.shape[:2]
  blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
  net.setInput(blob)
  faces = net.forward()
  #to draw faces on image
  for i in range(faces.shape[2]):
    confidence = faces[0, 0, i, 2]
    if confidence > 0.5:
      box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
      (x, y, x1, y1) = box.astype("int")
      cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
  return(faces)

  


class Camera(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.homies = utils.homies()

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
  async def detect(self, ctx, model = "dlib", echo = False):
    model = model.lower()
    print("Detecting ppl")
    fname = "/home/srenan/shared/wcam0.jpg"
    cmd = "fswebcam -r 1280x720 --no-banner " + fname
    os.system(cmd)
    # openCV
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #elif model == "mtcnn":
    #  detector = MTCNN()
    #  faces = detector.detect_faces(img)
    #  for result in faces:
    #      x, y, w, h = result['box']
    #      x1, y1 = x + w, y + h
    #      cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
    #  msg = "Detected: " + str(len(faces))+ " faces"
    if model == "dlib":
      faces = detect_dlib(img)
      #detector = dlib.get_frontal_face_detector()
      #faces = detector(gray, 1) # result
      ##to draw faces on image
      #for result in faces:
      #    x = result.left()
      #    y = result.top()
      #    x1 = result.right()
      #    y1 = result.bottom()
      #    cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
      msg = "Detected: " + str(len(faces))+ " faces with " + model
    if model == "dnn":
      faces = detect_dnn(img)
      #modelFile  = model_dir + "res10_300x300_ssd_iter_140000.caffemodel"
      #configFile = model_dir + "deploy.prototxt.txt"
      #net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
      #h, w = img.shape[:2]
      #blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
      #net.setInput(blob)
      #faces = net.forward()
      ##to draw faces on image
      #for i in range(faces.shape[2]):
      #        confidence = faces[0, 0, i, 2]
      #        if confidence > 0.5:
      #            box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
      #            (x, y, x1, y1) = box.astype("int")
      #            cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
      # TODO: faces is a different object. Need to find number of detected faces
      msg = "Detected: " + str(len(faces))+ " faces with " + model
    elif model == "haar":
      face_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_frontalface_default.xml')
      eye_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_eye.xml')
      ubody_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_upperbody.xml')
      fbody_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_fullbody.xml')
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
      msg = "Detected: " + str(len(faces))+ " faces, " + \
                           str(len(eyes)) + " eyes, " + \
                           str(len(ubody)) + " upper bodies, " + \
                           str(len(fbody)) + " full bodies."
    else:
      msg = "Model should be 'dnn', 'dlib' or 'haar'"
    cv2.imwrite(fname, img)
    # Post picture on discord if user has permission
    author = ctx.author
    author_name = author.name
    role_names = [r.name for r in author.roles]
    print("Roles:", role_names)
    if 'snap' in role_names:
      print(f'{author_name} taking a picture')
      if echo:
        discord_file = discord.File(fname, filename="image.jpg")
        await ctx.channel.send(file=discord_file, delete_after=10)
    else:
      print(f'{author_name} does not have permission to take picture')
    await ctx.send(msg)

  @commands.command()
  async def detect_haar(self, ctx, echo = False):
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
      if echo:
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
    

async def setup(bot):
  await bot.add_cog(Camera(bot))
