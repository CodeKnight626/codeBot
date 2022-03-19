import discord
import os.path


# Leemos la variable de sistema del sistema operativo
CODEBOT_TOKEN = os.environ['CODEBOT_TOKEN']

client = discord.Client()

# Evento que se llama cuando el bot inicia sesión
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Evento que se llama cuando se recibe un mensaje
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello')

client.run(CODEBOT_TOKEN)