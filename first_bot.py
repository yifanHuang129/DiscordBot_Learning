import discord


intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))

@bot.event
async def on_message(message):

    if message.content == 'ping':
        await message.channel.send('pong')

token = open('token.txt', 'r').read()
bot.run(token)