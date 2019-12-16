from discord.ext import commands

class Events:
  def __init__(self, bot):
    self.bot = bot

  async def fdp(ctx):
    await ctx.send("Ta mere!")

def setup(bot):
  bot.add_cog(Events(bot))
