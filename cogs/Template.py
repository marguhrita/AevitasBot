from discord.ext import commands
import discord

class Template(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Template(client))