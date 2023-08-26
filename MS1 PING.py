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

    if message.channel.id == 1138145290218643476 and not pinged:
        role = discord.utils.get(message.guild.roles, name='Free UGC Limited Game')
        if role is not None:
            await message.channel.send(f'{role.mention} NEW Free limited !')
            pinged = True
            print(f"Message envoyé dans le channel : {message.channel.name}")
    else:
        pinged = False

client.run('MTE0NDYyMzE2ODUxMDc3NTM0Ng.GmJP52.oDlKITVq8nFm78mwbPcadAdgj9UuCmOdgERIsk')