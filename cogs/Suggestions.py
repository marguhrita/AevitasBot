from discord import file, user
from discord.ext import commands
import discord, asyncio
from discord.ui import Button
from discord.ui.view import View


class SuggestionMessage(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.createSuggestion = None
            self.sent = None
            self.user = None
            
        
        @discord.ui.button(label = "Create Suggestion", style = discord.ButtonStyle.green)
        async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.send_message("Please type your suggestion in the chat below", ephemeral=True)
            self.user = interaction.user
            self.createSuggestion = True
            self.stop()

        @discord.ui.button(label = "💬Discuss a suggestion", style = discord.ButtonStyle.red)
        async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.send_message("Please create a thread.\nhttps://imgur.com/a/KVn6E7n", ephemeral=True)
            
            self.createSuggestion = False
            #self.stop()


class Suggestions(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    
    
    async def createSuggestion(self, ctx):
        
        view = SuggestionMessage()
        suggestionEmbed = await ctx.send(embed = discord.Embed(title="Suggestions", description="Create a suggestion for Aevitas Networks", colour = 0xe980e6), view = view)

        await view.wait()

        if view.createSuggestion:
            perms = ctx.channel.overwrites_for(view.user)
            perms.send_messages = True
            try:
                
                msg = await self.client.wait_for("message", timeout = 300, check = lambda message: message.author == view.user and message.channel == ctx.channel)
                embedVar = discord.Embed(description=msg.content, color = 0xf6b9f2)
                embedVar.set_author(name = view.user.name, icon_url = view.user.avatar)
                await msg.delete()
                sentSuggestion = await ctx.send(embed = embedVar)
                
            
            except asyncio.TimeoutError:
                await ctx.send("Sorry, you timed out! Please create another suggestion")
            

            
            perms.send_messages = True
            await suggestionEmbed.delete()
            
            await sentSuggestion.add_reaction(self.client.get_emoji(922219274544762901))
            await sentSuggestion.add_reaction(self.client.get_emoji(922219274267930634))
            await self.createSuggestion(ctx)


    @commands.command(name = "createsuggestion", hidden = True)
    @commands.has_permissions(administrator = True)
    async def suggestionCommand(self, ctx):
        await ctx.message.delete()
        await self.createSuggestion(ctx)



    
def setup(client):
    client.add_cog(Suggestions(client))