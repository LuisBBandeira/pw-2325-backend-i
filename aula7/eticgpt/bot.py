import discord
from discord.message import Message


intents= discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_connect():
    pass

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message: Message):
    pass