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

@bot.command()
async def score(ctx,sc1_type,sc1_score,sc2_type,sc2_score,sc3_type,sc3_score,sc4_type,sc4_score):

    total_score = jdata['Equip_rate'][sc1_type]*int(sc1_score) + jdata['Equip_rate'][sc2_type]*int(sc2_score) + jdata['Equip_rate'][sc3_type]*int(sc3_score) +jdata['Equip_rate'][sc4_type]*int(sc4_score)
    await ctx.send('裝備總分為:'+str(round(total_score,3)))
    if total_score > 70:
        await ctx.send('7414')


bot.run(jdata['token'])