import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands.commands import Command
from config import TOKEN

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())
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

@bot.tree.command(name='giveshot')
@app_commands.describe(type = "What type of alcohol?", name = "What is the name of the shot?")
async def shot(interaction: discord.Interaction, type: str, name: str):
    global shotsTotal
    shotEffects = [ #25
        'Drunk Zeta is feeling completely sober.',
        'Drunk Zeta is slightly buzzed.',
        'Drunk Zeta is feeling a little tipsy.',
        'Drunk Zeta has a feeling of relaxation and sociability.',
        'Drunk Zeta has increased confidence and talkativeness.',
        'Drunk Zeta has mild impairments in judgement and coordination.',
        'Drunk Zeta has increased likelihood of engaging in risky behavior.',
        'Drunk Zeta has mild to moderate impairments in memory and cognitive function.',
        'Drunk Zeta has slurred speech and difficulty walking.',
        'Drunk Zeta is starting to feel quite nauseous.',
        'Drunk Zeta has impaired balance and coordination.',
        'Drunk Zeta has extreme mood swings and emotional outbursts.',
        'Drunk Zeta now has blackouts and memory lapses.',
        'Drunk Zeta now has a severe loss of coordination and balance.',
        'Drunk Zeta now has possible alcohol poisoning.',
        'Drunk Zeta definitely now has alcohol poisoning.',
        'Drunk Zeta is now passed out on the floor.',
        'I\'m not sure what happened to Drunk Zeta, but I think he died.',
        'Drunk Zeta is now pronounced dead.',
        'Drunk Zeta is now a zombie.',
        'Drunk Zeta still manages to drink alcohol. Despite being a zombie.',
        'Drunk Zeta is now a black hole of alcohol.',
        'The Universe is now collapsing due to Drunk Zeta\'s alcohol consumption.',
        'The Universe has collapsed due to Drunk Zeta\'s alcohol consumption.',
        'You are no longer able to give Drunk Zeta any more shots, as there is no more Universe left.',
    ]
    if shotsTotal < 25:
        shotsTotal += 1
        embed = discord.Embed(description=f'Drunk Zeta has been given a `{type}` shot called `{name}` from {interaction.user.mention}. 🍻')
        embed.add_field(name="Drunk Zeta's shot total:", value=f'{shotsTotal} shot(s). {shotEffects[shotsTotal-1]}')
    else:
        embed = discord.Embed(description=f'{interaction.user.mention}, you have given Drunk Zeta too many shots. 🍻')
        embed.add_field(name="Drunk Zeta's shot total:", value=f'{shotsTotal} shot(s). {shotEffects[24]}')
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='totalshots')
async def totalshots(interaction: discord.Interaction):
    await interaction.response.send_message(f'Drunk Zeta\'s shot total is {shotsTotal} shots.')


# If command is not found, it will be handled by this event
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Command not found, {ctx.author.mention}")
    else:
        raise error

bot.run(TOKEN)