import nest_asyncio 
nest_asyncio.apply()

import random

import discord
from discord.ext import commands
from discord_buttons_plugin import  *


bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
buttons = ButtonsClient(bot)

@bot.command()
async def 경매(message, *, text):
    if text.isdigit():
        수수료1 = int(text) * 0.05
        분배금1 = (int(text) - int(text) *0.05) / 4
        손익분기점1 = int(text) - (int(text)*0.05) - 분배금1
        입찰적정가1 = 손익분기점1 / 1.1
        쌀먹입찰가1 = 입찰적정가1 / 1.1

        분배금2 = (int(text) - int(text) *0.05) / 8
        손익분기점2 = int(text) - (int(text)*0.05) - 분배금2
        입찰적정가2 = 손익분기점2 / 1.1
        쌀먹입찰가2 = 입찰적정가2 / 1.1
        

        await message.send(embed=discord.Embed(title="쌀먹계산기 "+format(int(text),',')+"G", description="4인 레이드\n수수료 : " 
        + str(format(round(수수료1),',')) + "G\n분배금 : "
        + str(format(round(분배금1),',')) + "G\n손익 분기점 : "
        + str(format(round(손익분기점1),',')) + "G\n입찰 적정가 : **"
        + str(format(round(입찰적정가1),',')) + "G**\n쌀먹입찰가 : **"
        + str(format(round(쌀먹입찰가1),',')) + "G**"
        ))
        await message.send(embed=discord.Embed(title="쌀먹계산기 "+format(int(text),',')+"G", description="8인 레이드\n수수료 : " 
        + str(format(round(수수료1),',')) + "G\n분배금 : "
        + str(format(round(분배금2),',')) + "G\n손익 분기점 : "
        + str(format(round(손익분기점2),',')) + "G\n입찰 적정가 : **"
        + str(format(round(입찰적정가2),',')) + "G**\n쌀먹입찰가 : **"
        + str(format(round(쌀먹입찰가2),',')) + "G**"
        ))

    else:
        await message.send(embed=discord.Embed(title="쌀먹계산기", description="숫자쳐써라"))



@bot.command()
async def test(message):
    await message.send('test')



@bot.command()
async def 테스트(message):
        await buttons.send(
        content = "아래쪽 버튼을 눌러주세요.", 
        channel = message.channel.id,
        components = [
            ActionRow([
                Button(
                    label="버튼입니다.", 
                    style=ButtonType().Primary, 
                    custom_id="button_one"       
                )
            ])
        ]
    )
    
@buttons.click
async def button_one(message):
    await message.reply("버튼이 눌렸습니다.")
    print('zz')

bot.run('MTAyMTkyOTA4OTM2OTYzNjkwNQ.GRy-a_.DbtswYSNiiTkTieoyzsfeKXDheZCzIYJ1uZ4ZM')
