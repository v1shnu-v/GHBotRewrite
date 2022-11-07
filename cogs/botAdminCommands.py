import discord
from discord.ext import commands
from discord import app_commands

#for logging
from colorama import Back,Fore,Style
import time
import datetime

class botAdminCommands(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        pfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.RESET + Style.BRIGHT)
        print(pfx + Fore.YELLOW + " Bot Admin Commands"+ Fore.RESET +" Cog Loaded")


    @app_commands.command(name="hello", description="Says hello back")
    async def hello(self,interaction: discord.Interaction):
        await interaction.response.send_message(content="hello!")


async def setup(client):
    await client.add_cog(botAdminCommands(client))














