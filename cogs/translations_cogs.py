import discord
from discord.ext import commands
from machinetranslations import translator


class translatory(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Translator.py is connected successfully")
        
    @commands.command()
    async def translate(self,ctx,*text):
        final_word = ""
        if text == None:
            await ctx.send("Incorrect Syntax. Try !translate <text>")
        else:
            final_word = ' '.join(text)
            translation = translator.TranslateToEnglish(final_word)
            embeds = discord.Embed(
            colour=discord.Colour.blue(),title="Waste-Translator",type='rich',
            description=f"Translating **{translator.language_detect(final_word)}** to **en**",timestamp=None)
            embeds.add_field(name="Original Text",value=' '.join(text),inline=True)
            embeds.add_field(name="Translated Text",value=translation,inline=True)
            await ctx.send(embed=embeds)

async def setup(client):
    await client.add_cog(translatory(client))