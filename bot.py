import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8')as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def kevin好帥(ctx):
    await ctx.send('真的挺帥的')

@bot.command()
async def 是吧(ctx):
    await ctx.send('是阿')

@bot.command()
async def 對吧(ctx):
    await ctx.send('對阿')

@bot.command()
async def 羊又騎請我吃早餐(ctx):
    await ctx.send('羊又騎請他吃早餐')


@bot.command()
async def 欠錢還錢(ctx):
    await ctx.send('曾士恩欠我200')

@bot.command()
async def 你出(ctx):
    await ctx.send('曾士恩出')



@bot.event
async def on_ready():
    print('>>Bot is online<<')

bot.run(jdata['TOKEN'])
