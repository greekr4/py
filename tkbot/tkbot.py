import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)
    
bot.run('MTAyMTkyOTA4OTM2OTYzNjkwNQ.GdOD0k.ejzEZHT5BsVyB0jx-0s19Kt3z3acEEvD2eGG5o')
