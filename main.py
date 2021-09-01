import discord
from discord.ext import commands
import json
with open('setting.json' , 'r',encoding="utf8") as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def 空幹(ctx):
    pic = (jdata['空幹'])
    await ctx.send(pic)

bot.run(jdata['token'])