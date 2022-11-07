#read token
#from ast import alias
import os
import json
#from unicodedata import name
import asyncio

#for logging
from colorama import Back,Fore,Style
import time
import platform
import datetime

#discord timing
import discord
from discord.ext import commands


with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]


client = commands.Bot(command_prefix='.',  activity=discord.Activity(type=discord.ActivityType.listening, name="music"), intents=discord.Intents.all())

#On Ready
@client.event
async def on_ready():
    synced = await client.tree.sync()
    pfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.RESET + Style.BRIGHT)
    print(pfx + " Logged in as " + Fore.YELLOW + client.user.name)
    print(pfx + " Bot ID " + Fore.YELLOW + str(client.user.id))
    print(pfx + " Discord version : "+ Fore.YELLOW + discord.__version__)
    print(pfx + " Python version : "+ Fore.YELLOW + str(platform.python_version()))
    print(pfx + " Slash commands synced " + Fore.YELLOW + str(len(synced))+ " commands")
#Commands


# @client.tree.command(name = "shutdown", description= "Shutting down bot")
# async def shutdown(interaction: discord.Interaction):
#     await interaction.response.send_message(content="Shutting down")
#     await client.close()




async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await client.load_extension(f'cogs.{file[:-3]}')

            



async def main():
    await load()
    await client.start(token)





     
asyncio.run(main())