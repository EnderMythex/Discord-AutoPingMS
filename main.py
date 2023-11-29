import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  

    if message.channel.name == 'CHANNEL':
        role = discord.utils.get(message.guild.roles, name="ROLE NAME") # modify it
        if role:
            await message.channel.send(f'{role.mention} MESSAGE') # modify it
            await message.add_reaction('👍') 
            await message.add_reaction('❤')
            print(f"Message envoyé dans le channel : {message.channel.name}")
        else:
            await message.channel.send('Rôle non trouvé.')

    await bot.process_commands(message)

bot.run('BOT TOKEN HERE') # modify it
