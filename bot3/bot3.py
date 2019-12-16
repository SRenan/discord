from discord.ext import commands

# Setup
bot = commands.Bot(command_prefix='!')
import bot_funcs

# Functions
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

# Startup
TOKEN = 'NjAzMDUxOTI1MjY4ODU2ODQx.XTZx9g.y_dSVCtzTeuK3JTN14Q021GVOqI'
bot.run(TOKEN)
