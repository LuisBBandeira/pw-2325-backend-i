import discord
from discord.message import Message

intends= discord.Intends.default()

client = discord.Client(intends=intends)


@client.event
async def on_connect():
    pass

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message: Message):
    pass