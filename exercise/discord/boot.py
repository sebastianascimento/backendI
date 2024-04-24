import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_ready():
    print(f'Bot está pronto: {bot.user.name}')

bot.run('TOKEN')
