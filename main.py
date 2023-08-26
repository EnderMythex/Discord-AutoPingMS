import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

pinged = False  # Variable pour garder une trace de l'état du ping

@client.event
async def on_ready():
    print('Bot connecté')

@client.event
async def on_message(message):
    global pinged

    if message.channel.id == CHANNEL ID and not pinged:
        role = discord.utils.get(message.guild.roles, name='ROLE TO PING')
        if role is not None:
            await message.channel.send(f'{role.mention} Hello')
            pinged = True
            print(f"Message envoyé dans le channel : {message.channel.name}")
    else:
        pinged = False

client.run('BOT TOKEN')
