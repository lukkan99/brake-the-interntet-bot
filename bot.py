import discord
import asyncio
token = "bot token hare"
prefix = "prefix hare"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    type = discord.Status.online
    game = discord.Game(name="https://www.battleforthenet.com/")
    await client.change_presence(status=type, game=game)

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        counter = 0
        tmp = await client.send_message(message.channel, 'running cmd. culd be slow as host ips slowing down connation to discord api')
        await asyncio.sleep(5)
        await client.edit_message(tmp, "you're ips has blocked the use this bot sorry! go look at hare current plans for discord.")
        await client.send_message(message.channel, 'dont make this reallty check this out. https://www.battleforthenet.com/')

client.run(token)
