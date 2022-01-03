from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    #kicks a member
    @commands.command(name="kick")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member):
        await ctx.guild.kick(member)
        await ctx.send(str(member) + " was kicked")

    @kick.error
    async def kickError(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Insufficient Permissions: {error.name}")


    #bans a member
    @commands.command(name="ban")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member):

        await ctx.guild.ban(member)
        await ctx.send(str(member) + " was banned")

    @ban.error
    async def banError(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Insufficient Permissions: {error.name}")

    #unbans a member
    @commands.command(name = "unban")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, id : int):
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"succesfully unbanned {user}")

    @unban.error
    async def banError(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Insufficient Permissions: {error.name}")

def setup(client):
    client.add_cog(Moderation(client))