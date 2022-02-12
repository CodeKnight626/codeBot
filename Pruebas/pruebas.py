import discord
import os.path

CODEBOT_TOKEN = os.environ['CODEBOT_TOKEN']

intent = discord.Intents(messages=True, guilds=True, members=True)

client = discord.Client(intents=intent)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello')

@client.event
async def on_member_join(member):
    channel = client.get_channel(936508852650786897)
    image = discord.File("Hola.gif", filename="hola.gif")
    await channel.send("Bienvenido " + member.mention)
    await channel.send(file=image)


client.run(CODEBOT_TOKEN)