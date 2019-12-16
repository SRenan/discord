from discord.ext import commands

TOKEN = 'NjAzMDUxOTI1MjY4ODU2ODQx.XTZx9g.y_dSVCtzTeuK3JTN14Q021GVOqI'


bot = commands.Bot(command_prefix='!')
bot.add_cog(Maincog(bot))
bot.run(TOKEN)
