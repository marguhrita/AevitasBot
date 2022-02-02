from discord.ext import commands
import discord

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "stream", hidden = True)
    @commands.has_permissions(administrator = True)
    async def streamingStatus(self, ctx):
        await self.client.change_presence(activity=discord.Streaming(name="yuh", url="https://twitch.tv/aevitas"))
        
    @commands.command(name = "avatar")
    async def getAvatar(self, ctx):
        avatarUrl = ctx.author.avatar
        await ctx.send(avatarUrl)

    @commands.command(name = "msg", hidden = True)
    @commands.has_permissions(administrator = True)
    async def privateMessage(self, ctx, user:discord.User, message):
        await user.send(message)


def setup(client):
    client.add_cog(Utility(client))