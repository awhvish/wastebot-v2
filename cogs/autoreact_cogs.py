import discord
import pandas as pd
from discord.ext import commands



# Writing the File
def insert_into_csv(trig,react):
    dic = pd.DataFrame({"words":trig,"reactions":react})
    dic.to_csv("ar_words.csv")
    

class AutoReactions(commands.Cog):
    def __init__(self,client):
        self.client = client

    commands.Cog.listener()
    async def on_ready(self):
        print("autoreact_cogs.py loaded successfully")
            
    @commands.command()
    async def ar(self,ctx,arg1=None,arg2=None,arg3=None):
        if arg1 == "add":
            if arg2==None or arg3==None:
                await ctx.send("Incorrect Syntax.")
            else:
                df = pd.read_csv("ar_words.csv")
                triggers = df["words"].to_list()
                reactions = df["reactions"].to_list()
                
                if arg2 not in triggers: 
                    triggers.append(arg2.lower())
                    reactions.append(arg3)
                    insert_into_csv(triggers,reactions)
                    await ctx.send("Successfully added autoreaction!")
                else:
                    await ctx.send("Autoreaction already exists.")

            
        elif arg1 == "remove":
            try:
                df = pd.read_csv("ar_words.csv")
                triggers = df["words"].to_list()
                reactions = df["reactions"].to_list()  
                df.index = triggers
                triggers.remove(arg2)
                reactions.remove(df.loc[arg2,"reactions"])
                insert_into_csv(triggers,reactions)
                await ctx.send("Successfully removed autoreaction!") 
            except ValueError:
                await ctx.send("No such reactions found")
            
        elif arg1 == "list":
            df = pd.read_csv("ar_words.csv")
            triggers = df["words"].to_list()
            await ctx.send('\n'.join(triggers))        
            
        elif arg1 == None:
            await ctx.send("!ar <add/remove/list> [word] [reaction]")
        
        
    @commands.Cog.listener('on_message')
    async def on_message(self,message):
        df = pd.read_csv("ar_words.csv")
        triggers = df["words"].to_list()
        df.index = triggers
        for i in triggers:
            if i in message.content:
                await message.add_reaction(df.loc[i,"reactions"])
                

async def setup(client):
    await client.add_cog(AutoReactions(client))
