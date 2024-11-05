import discord
import pandas as pd
import yfinance as yf
from discord.ext import commands, tasks


class Stock(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def stock(self, ctx, ticker = ""):
    """
    Fetch stock price 
    """
    author = ctx.author.name
    print(f'{author} checking stock price for {ticker}')
    yftick = yf.Ticker(ticker)
    data = yftick.history(period = "1d")
    stock_open = data["Open"].iloc[0]
    stock_close = data["Close"].iloc[0]
    stock_date = pd.to_datetime(str(data.index.values[0])).strftime('%Y-%m-%d')
    stock_message = ticker + " Open on " + stock_date + " at " + str(stock_open.round(3)) + "; Close at " + str(stock_close.round(3))
    print(stock_message)
    await ctx.send(stock_message)

async def setup(bot):
  await bot.add_cog(Stock(bot))
