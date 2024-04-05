import discord
from discord.message import Message

from eticgpt.client import OllamaAPI
from eticgpt.models import OllamaPrompt , OllamaResponse

intents= discord.Intents.default()

client = discord.Client(intents=intents)

OllamaAPI = OllamaAPI()


@client.event
async def on_connect():
    print("i'm connecting...")

@client.event
async def on_ready():
    print('connected!!')

@client.event
async def on_message(message: Message):
    assert message
    
    if message.author == client.user:
        
        if message.content.startswith("/ask"):
            question=OllamaPrompt(
                prompt=message.content.split("/ask")[-1]
            )
            response: OllamaResponse= OllamaAPI.prompt(prompt=question)
            
            if not response.done:
                await message.channel.send(":poop_ops!")
            else:
                await message.channel.send(response.response)
