import discord


COWBOT_TOKEN = "Your token here"
#New addition for compatibility with new discord python api verison
intent = discord.Intents(messages=True, guilds=True)
intent.members = True # Subscribe to the privilged memebers intent.\

client = discord.Client(intents=intent)

#client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    channel = client.get_channel(936508852650786897)
    await channel.send("Hola ")

client.run(COWBOT_TOKEN)