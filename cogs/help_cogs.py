import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(Self):
        print("help.py is connected successfully") 
            
    @commands.command()
    async def help(self,ctx,arg1=None):
        if arg1==None:
            embeds = discord.Embed(
                colour=discord.Colour.blue(),title="Help Desk for Waste Bot",type='rich',
                description="A brief description on all the commands available in the bot",timestamp=None)
            embeds.add_field(name="!help", value="Shows this message", inline=False)
            embeds.add_field(name="!ping", value="Shows the latency", inline=False)
            embeds.add_field(name="!ar", value="Used to add or remove autoreactions", inline=False)
            embeds.add_field(name="!translate",value="Used to translate any message to english",inline=False)
            embeds.add_field(name="!echo",value="Used to echo/send any message to any channel using the bot",inline=False)
            embeds.set_footer(text="!help <command> for more info on a command")
        elif arg1.lower()=="ar":
            embeds = discord.Embed(title="!ar",description="Used to add or remove autoreactions",type='rich',colour=discord.Colour.blue())
            embeds.add_field(name="Subcommands",value="```!ar add <word> <emoji>```\nTo add any AutoReaction",inline=False)
            embeds.set_footer
        await ctx.send(embed=embeds)
        
async def setup(client):
    await client.add_cog(HelpCommand(client))