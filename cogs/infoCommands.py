import discord
from discord.ext import commands
from discord import app_commands

#for logging
from colorama import Back,Fore,Style
import time
import datetime
from datetime import timezone


class infoCommands(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.RESET + Style.BRIGHT)
        print(pfx + Fore.YELLOW + " Info Commands"+ Fore.RESET +" Cog Loaded")
        
    

    @app_commands.command(name="userinfo", description="Shows information about the user")
    async def userinfo(self,interaction: discord.Interaction, member:discord.Member = None):
        if member == None:
            member = interaction.user
        roles = [role for role in member.roles]
        embed = discord.Embed(title = "User Info", description = f"{member.mention}'s user info", color = discord.Color.green())
        embed.set_thumbnail(url = member.avatar)
        embed.add_field(name = "ID", value = member.id)
        embed.add_field(name = "Name", value = f"{member.name}#{member.discriminator}")
        embed.add_field(name = "Status", value = member.status)
        embed.add_field(name = "Server Join Date", value = member.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
        embed.add_field(name = "Top role", value = member.top_role.mention)
        embed.add_field(name = f"Roles {len(roles)}",value = " ".join([role.mention for role in roles]) )
        embed.add_field(name = "Account Created Date", value = member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
        await interaction.response.send_message(embed = embed)


    
    @app_commands.command(name="serverinfo", description="Shows information about the server")
    async def serverinfo(self,interaction: discord.Interaction):
        embed = discord.Embed(title = "Server Info", description = interaction.guild.description , color = discord.Color.green())
        embed.set_thumbnail(url = interaction.guild.icon) 
        embed.add_field(name = "Member Count", value = interaction.guild.member_count)
        embed.add_field(name = "Channels", value = f"{len(interaction.guild.text_channels)} Text | {len(interaction.guild.voice_channels)} Voice")
        embed.add_field(name = "Created on", value = interaction.guild.created_at.strftime("%a, %B %#d, %Y, %I:%M %p"))
        await interaction.response.send_message(embed = embed)


async def setup(client):
    await client.add_cog(infoCommands(client))