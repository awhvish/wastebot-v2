import discord
from machinetranslations import translator
from discord.ext import commands
import os
import asyncio

# Starting the Bot
with open("token.txt",'r') as f:
    TOKEN = f.read()


# Initial Settings
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
client = commands.Bot(command_prefix="!", intents = intents,help_command=None)



# Commands
@client.event
async def on_ready():
    print(f'Logged on as {client.user}')

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
                

async def main():
    async with client:
        await load()
        await client.start(TOKEN)
        
asyncio.run(main())