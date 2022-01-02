from discord.ext import commands
import discord
import os

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(name = "reloadcog", hidden = True)
    @commands.has_permissions(administrator = True)
    async def reloadcog(self, ctx, cog):
        try:
            await ctx.send("unloading cog..")
            self.client.unload_extension(f"cogs.{cog}")
            await ctx.send("loading cog..")
            self.client.load_extension(f"cogs.{cog}")

        except Exception as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")


    @commands.command(name = "reload", hidden = True)
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

    @commands.command(name = "loadcog", hidden = True)
    @commands.has_permissions(administrator = True)
    async def loadCog(self, ctx, cog : str):
        try:
            self.client.load_extension(f"cogs.{cog}")
        except commands.ExtensionAlreadyLoaded:
            await ctx.send("Cog already loaded")
        except commands.ExtensionNotFound:
            await ctx.send("Cog not found")
        else: await ctx.send("idfk whats happened to the cog")
        

    @commands.command(name = "loadallcogs", hidden = True)
    @commands.has_permissions(administrator = True)
    async def loadAllCogs(self, ctx):
        for extension in os.listdir("./cogs/"):
            print("loading cogs..")
            if extension.endswith(".py"):
                self.client.load_extension(f"cogs.{extension[:-3]}")



    @commands.command(name="isdiscorddown")
    async def isDiscordDown(self, ctx):
        await ctx.send("No, its not")

    

def setup(client):
    client.add_cog(Admin(client))