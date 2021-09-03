import discord
from discord.ext import commands
import json
with open('setting.json' , 'r',encoding="utf8") as jfile:
    jdata = json.load(jfile)
with open('herodata.json' , 'r',encoding="utf8") as hero_file:
    hero_data = json.load(hero_file)

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
        await ctx.send('這麼高分7414好嗎')

@bot.command()
async def CS(ctx, hero, ATK, HP , DEF ,SPD, CC , CD , EF , ER , right_1,right_2,right_3, equip_BF1, equip_BF2,equip_BF3):
    list_equip = [equip_BF1 , equip_BF2 , equip_BF3]
    list_right = [right_1 , right_2, right_3]
    hero_equip_data = hero_data[hero]               #backup how equip_bf hero have
    for equip_BF in list_equip:
        if(equip_BF == '攻擊套'):
            hero_equip_data['攻擊力']*=1.45
        elif (equip_BF == '防禦套'):
            hero_equip_data['防禦力']*=1.2
        elif (equip_BF == '生命套'):
            hero_equip_data['生命力']*=1.2
        elif (equip_BF == '速度套'):
            hero_equip_data['速度']*=1.25
        elif (equip_BF == '暴擊套'):
            hero_equip_data['暴擊']+=12
        elif (equip_BF == '破滅套'):
            hero_equip_data['暴傷']+=40
        elif (equip_BF == '命中套'):
            hero_equip_data['效命']+=20
        elif (equip_BF == '抵抗套'):
            hero_equip_data['效抗']+=20
        elif (equip_BF == '復仇套'):
            hero_equip_data['速度']*=1.12
                                                    #-------------------------------
    #right set
    CD_SC = CC_SC = ATK_SC = DEF_SC = HP_SC = SPD_SC =EF_SC = ER_SC =0
    for right in list_right:
        if(right == '暴傷'):
            CD_SC -= jdata['right_set']['暴傷']
        elif(right == '暴擊率'):
            CC_SC -= jdata['right_set']['暴擊率']
        elif(right == '攻擊%'):
            ATK_SC -= jdata['right_set']['攻擊%']
        elif(right == '防禦%'):
            DEF_SC -= jdata['right_set']['防禦%']
        elif(right == '生命%'):
            HP_SC -= jdata['right_set']['生命%']
        elif(right == '速度'):
            SPD_SC -= jdata['right_set']['速度']
        elif(right == '效命'):
            EF_SC -= jdata['right_set']['效命']
        elif(right == '效抗'):
            ER_SC -= jdata['right_set']['效抗']
        elif(right == '攻擊'):
            #ATK_SC -= jdata['right_set']['攻擊']
            hero_equip_data['攻擊力'] *= 2
        elif(right == '防禦%'):
            #DEF_SC -= jdata['right_set']['防禦']
            hero_equip_data['防禦力'] *= 2
        elif(right == '生命%'):
            #HP_SC -= jdata['right_set']['生命']
            hero_equip_data['生命力'] *= 2
    #caculate score
    ATK_SC += (((int(ATK) - hero_equip_data['攻擊力'] + hero_data[hero]['攻擊力'] - 525) / hero_data[hero]['攻擊力'])-1) *100 #525
    HP_SC += ((( int(HP) - hero_equip_data['生命力'] + hero_data[hero]['生命力'] - 2835) / hero_data[hero]['生命力'])-1)*100
    DEF_SC += ((( int(DEF) - hero_equip_data['防禦力'] + hero_data[hero]['防禦力'] - 310) / hero_data[hero]['防禦力'])-1) *100
    SPD_SC += (int(SPD) - hero_equip_data['速度'])
    CC_SC += ( int(CC) - hero_equip_data['暴擊'])
    CD_SC += ( int(CD) - hero_equip_data['暴傷']) 
    EF_SC += ( int(EF) - hero_equip_data['效命'])
    ER_SC += ( int(ER) - hero_equip_data['效抗'])

    await ctx.send('裝備總共:\n攻擊:'+str(round(ATK_SC,3))+'\n生命:'+str(round(HP_SC,3))+'\n防禦:'+str(round(DEF_SC,3))
    +'\n速度:'+str(round(SPD_SC,3))+'\n暴擊:'+str(round(CC_SC,3))+'\n暴傷:'+str(round(CD_SC,3))+'\n效命:'+str(round(EF_SC,3))+'\n效抗:'+str(round(ER_SC,3)))
bot.run(jdata['token'])