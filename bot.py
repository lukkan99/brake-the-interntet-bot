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
        await client.edit_message(tmp, "you're isp has blocked the use of this bot, sorry!, go look at here for the current ISP pricing plans for discord.")
        await asyncio.sleep(2)
        await client.send_message(message.channel, "If you wouldn't like this to become a reality, please visit https://battleforthenet.com/")

client.run(token)
