import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8')as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')#your bot ping

@bot.command()
async def inputdirectives(ctx):
    await ctx.send('What do you want the robot to say')

@bot.command()
async def inputdirectives(ctx):
    await ctx.send('What do you want the robot to say')

@bot.command()
async def inputdirectives(ctx):
    await ctx.send('What do you want the robot to say')

@bot.command()
async def inputdirectives(ctx):
    await ctx.send('What do you want the robot to say')


@bot.command()
async def inputdirectives(ctx):
    await ctx.send('What do you want the robot to say')

@bot.command()
async def inputdirectives(ctx):
    await ctx.send('What do you want the robot to say')



@bot.event
async def on_ready():
    print('>>Bot is online<<')#press F5 to start robot

bot.run(jdata['TOKEN'])
