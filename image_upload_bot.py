import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await self.get_channel(1093806443829928027).send(discord.File('./images/0.jpg'))


    async def on_message(self, message):
        # don't respond to ourselves
        
        print(message.content)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA5MzgwMzA5NzM2MjUzODU3Nw.G4KY6r.dNGXvmI7KiqPtiOky_8B2tA0C64hlnVQlDAAR0')