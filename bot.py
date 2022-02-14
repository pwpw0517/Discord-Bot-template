import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('>>Bot is online<<')

bot.run('OTQyNzQ2NDE2NjU1MjY1ODEz.Ygo_BQ.Ix-SYfyl_i0nymfmNZcgYUPyoPQ')
