import discord
from discord.ext import commands
import os, random
from BOT_LOGIC import sampah_organik, sampah_anorganik, greetings



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
# GREETINGS/HELP
@bot.event
async def greet(ctx):
    await ctx.send(greetings)
# SAMPAH ORGANIK
@bot.event
async def organik(ctx):
    await ctx.send(sampah_organik)
# SAMPAH ANORGANIK
@bot.event
async def anorganik(ctx):
    await ctx.send(sampah_anorganik)
