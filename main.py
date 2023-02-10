import asyncio
import discord
import random
from discord import app_commands
from discord.ext import commands
from discord.app_commands.commands import Command
from config import TOKEN
from messages import *

bot = commands.Bot(command_prefix='', intents = discord.Intents.all())
shotsTotal = 0

@bot.event
async def on_ready():
    print('Bot is ready')
    try: 
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hey(ctx):
    await ctx.send(random.choice(heyList))

@bot.command()
async def hello(ctx):
    await ctx.send(random.choice(heyList))

@bot.command()
async def yo(ctx):
    await ctx.send(random.choice(heyList))

@bot.command()
async def hi(ctx):
    await ctx.send(random.choice(heyList))

@bot.command()
async def bitch(ctx):
    await ctx.send("wow")



@bot.tree.command(name='giveshot')
@app_commands.describe(type = "What type of alcohol?", name = "What is the name of the shot?")
async def shot(interaction: discord.Interaction, type: str, name: str):
    global shotsTotal
    if shotsTotal < 25:
        shotsTotal += 1
        embed = discord.Embed(description=f'Drunk Zeta has been given a `{type}` shot called `{name}` from {interaction.user.mention}. 🍻')
        embed.add_field(name="Drunk Zeta's shot total:", value=f'`{shotsTotal}` shot(s). {shotEffects[shotsTotal-1]}')
    else:
        embed = discord.Embed(description=f'{interaction.user.mention}, you have given Drunk Zeta too many shots. 🍻')
        embed.add_field(name="Drunk Zeta's shot total:", value=f'`{shotsTotal}` shot(s). {shotEffects[24]}')
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='totalshots')
async def totalshots(interaction: discord.Interaction):
    embed = discord.Embed(title=f'Drunk Zeta\'s shot total is `{shotsTotal}` shots.', description=f'{shotEffects[shotsTotal-1]}')
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='exist')
async def exist(interaction: discord.Interaction):
    await interaction.response.send_message(embed=discord.Embed(title=random.choice(existences), color=random.randint(0, 0xFFFFFF)))

@bot.tree.command(name='help')
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title='Drunk Zeta\'s help menu', description='Drunk Zeta is a bot that needs your help getting drunk.')
    embed.add_field(name='/giveshot', value='Give Drunk Zeta a shot. 🍻', inline=False)
    embed.add_field(name='/totalshots', value='See how many shots Drunk Zeta has had.', inline=False)
    embed.add_field(name='/exist', value='Ask Drunk Zeta to exist.', inline=False)
    embed.add_field(name='/help', value='See this menu.', inline=False)
    await interaction.response.send_message(embed=embed)

# If command is not found, it will be handled by this event
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        raise error

bot.run(TOKEN)