import discord
from discord.ext import commands
import datetime
import atexit

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("[SUCCES  ] ONLINE ") # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
    channel = bot.get_channel(1234567890) # ------------------------------------- EDIT THIS LINE : Replace 1234567890 with your channel ID (Required) -------------------------------------
    embed = discord.Embed(
        title='🟢 Bot Online', # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
        description='[V2.2.3] ONLINE', # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
        color=discord.Color.green()
    )
    await channel.send(embed=embed)

@bot.command()
async def stop(ctx):
    if ctx.message.channel.id == 1234567890:  # ------------------------------------- EDIT THIS LINE : Replace 1234567890 with your channel ID (Required) -------------------------------------
        embed = discord.Embed(
            title='🔴 Bot Offline', # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
            description='[V2.2.3] STOPED', # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        await bot.close()
    else:
        await ctx.send('You cannot use this command in this channel.') # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.name == 'CHANNEL NAME': # ------------------------------------- EDIT THIS LINE (Required) -------------------------------------
        role = discord.utils.get(message.guild.roles, name="ROLE NAME") # ------------------------------------- EDIT THIS LINE (Required) -------------------------------------
        if role:
            reply = await message.reply(f'{role.mention} Successfully pinged ! ') # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
            await message.add_reaction('👍') # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
            await message.add_reaction('❤') # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
            print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCES  ] Successfully pinged in : {message.channel.name} {message.guild.name}") # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
        else:
            await message.channel.send('Role not found.') # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------

    if message.channel.name == 'CHANNEL NAME': # ------------------------------------- EDIT THIS LINE (Required) -------------------------------------
        role = discord.utils.get(message.guild.roles, name="ROLE NAME") # ------------------------------------- EDIT THIS LINE (Required) -------------------------------------
        if role:
            reply = await message.reply(f'{role.mention} Successfully pinged ! ') # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
            await message.add_reaction('👍') # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
            await message.add_reaction('❤') # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
            print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCES  ] Successfully pinged in : {message.channel.name} {message.guild.name}") # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------
        else:
            await message.channel.send('Role not found.') # ------------------------------------- EDIT THIS LINE (Not required) -------------------------------------

atexit.register(bot.close)
bot.run('BOT TOKEN HERE') # ------------------------------------- EDIT THIS LINE (Required) -------------------------------------
