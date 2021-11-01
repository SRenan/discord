import discord
from discord.ext import commands, tasks
from utils import utils


class Dotabuff(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.homies = utils.homies()

  @commands.command(aliases = ["db", "DB"])
  async def dotabuff(self, ctx, playerid = 0):
    """
    Fetch dotabuff profile
    usage: !db [playerid]
    """
    author = ctx.author.name
    print(f'{author} checking dotabuff')
    if playerid != 0:
      message = "https://www.dotabuff.com/players/"+str(playerid)
    else:
      homies_names = [ item['name'] for item in self.homies["homies"]]
      if author in homies_names:
        homie = next(item for item in self.homies["homies"] if item["name"] == author)
        message = homie["dotabuff"]
        #if author == "Loukkk":
        #  message = "https://www.dotabuff.com/players/54758529"
        #elif author == "Erq":
        #  message = "https://www.dotabuff.com/players/34116323"
        #elif author == "PAN":
        #  message = "https://www.dotabuff.com/players/57013635"
      else:
        message = "Unknown user"
    await ctx.send(message)


def setup(bot):
  bot.add_cog(Dotabuff(bot))
