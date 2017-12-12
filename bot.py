import discord
import asyncio
token = "bot token hare
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
    await bot.change_presence(status=type, game=game)

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        counter = 0
        tmp = await client.send_message(message.channel, 'running command culd be slow as not on fastline at server ips')
         await asyncio.sleep(5)
        await client.edit_message(tmp, "youre ips has blocked this bot")
        await client.send_message(message.channel, 'https://www.battleforthenet.com/')

client.run(token)
