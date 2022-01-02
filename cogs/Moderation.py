from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name="kick")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member):
       
        await ctx.guild.kick(member)
        await ctx.send(str(member) + " was kicked")


    @commands.command(name="ban")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member):

        await ctx.guild.ban(member)
        await ctx.send(str(member) + " was banned")
        


    @commands.command(name = "unban")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, id : int):
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"succesfully unbanned {user}")


def setup(client):
    client.add_cog(Moderation(client))