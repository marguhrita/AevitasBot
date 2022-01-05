from discord.ext import commands
import discord
import os

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    #reloads ONE cog in 
    @commands.command(name = "reloadcog", hidden = True)
    @commands.has_permissions(administrator = True)
    async def reloadcog(self, ctx, cog):

        try:
            await ctx.send("unloading cog..")
            self.client.unload_extension(f"cogs.{cog}")
            await ctx.send("loading cog..")
            self.client.load_extension(f"cogs.{cog}")
            await ctx.send(f"Cog {cog} succesfully reloaded!")

        except Exception as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")

    #reloads ALL cogs
    @commands.command(name = "reloadall", hidden = True)
    @commands.has_permissions(administrator = True)
    async def reload(self, ctx):
        async with ctx.typing():
            embed = discord.Embed(
            title = "Reloading cogs",
            timestamp=ctx.message.created_at
            )

            try:
                for extension in os.listdir("./cogs/"):
                    if extension.endswith(".py") and extension not in ["Admin.py", "levelcard.py"]:
                        print(extension)
                        self.client.unload_extension(f"cogs.{extension[:-3]}")
                        self.client.load_extension(f"cogs.{extension[:-3]}")
                        embed.add_field(
                        name = f"reloaded: '{extension}'",
                        value = "\uFEFF"
                        )

            except Exception as e:
                embed.add_field(
                name = f"Failed to reload : {extension}",
                value = e
                )
            await ctx.send(embed=embed)

    #checks if a cog is loaded
    @commands.command(name = "loaded",  hidden = True)
    @commands.has_permissions(administrator = True)
    async def showLoaded(self, ctx, cog: str):
        try:
            self.client.load_extension(f"cogs.{cog}")
        except commands.ExtensionAlreadyLoaded:
            await ctx.send("Cog is loaded")
        except commands.ExtensionNotFound:
            await ctx.send("Cog not found")
        else:
            await ctx.send("Cog is unloaded")
            self.client.unload_extension(f"cogs.{cog}")


    #loads one cog in particular    
    @commands.command(name = "loadcog", hidden = True)
    @commands.has_permissions(administrator = True)
    async def loadCog(self, ctx, cog : str):
        try:
            self.client.load_extension(f"cogs.{cog}")
        except commands.ExtensionAlreadyLoaded:
            await ctx.send("Cog already loaded")
        except commands.ExtensionNotFound:
            await ctx.send("Cog not found")
        else: await ctx.send("idk whats happened to the cog")
        

    #tries to load all cogs in cogs directory
    @commands.command(name = "loadallcogs", hidden = True)
    @commands.has_permissions(administrator = True)
    async def loadAllCogs(self, ctx):
        for extension in os.listdir("./cogs/"):
            try:
                if extension.endswith(".py"):
                    self.client.load_extension(f"cogs.{extension[:-3]}")
            except Exception as e:
                await ctx.send(f"{extension[:-3]} failed to load")
                


    #tells you if discord is down
    @commands.command(name="isdiscorddown")
    async def isDiscordDown(self, ctx):
        await ctx.send("No, its not")

    

def setup(client):
    client.add_cog(Admin(client))