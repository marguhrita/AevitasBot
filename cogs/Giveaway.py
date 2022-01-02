from discord.components import ActionRow
from discord.embeds import Embed
from discord.ext import commands
import discord, random, asyncio
from discord.ui import Button
from discord.ui.view import View

#Creates view object which makes a confirmation menu
class Confirm(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.value = None
        
        @discord.ui.button(label = "Confirm", style = discord.ButtonStyle.green)
        async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.send_message("Giveaway creation confirmed.", ephemeral=True)
            self.value = True
            self.stop()

        @discord.ui.button(label = "Cancel", style = discord.ButtonStyle.red)
        async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.send_message("Giveaway creation cancelled.", ephemeral=True)
            self.value = False
            self.stop()

def timeParser(time):
  splitTime = time.split(":")
  
  hours = splitTime[0]
  minutes = splitTime[1]
  seconds = splitTime[2]
  return int(hours)*3600 + int(minutes) * 60 + int(seconds)


class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open("giveaway.txt", "r") as f:
            giveawayMessageId = f.read().rstrip()
        self.giveawayMessage = giveawayMessageId

    """@commands.command(name = "fetchgiveaway")
    async def fetchGiveawayMessage(self, ctx, message : discord.Message):

        #channel = self.client.get_channel(867340695723311135)
        for channel in ctx.guild.channels:
            await ctx.send(str(channel))
            if "announcements" in channel.name:
                wanted_channel = channel

        await ctx.send(wanted_channel)

        #msg = wanted_channel.fetch_message(message)
        #users = await msg.reactions[0].users().flatten()
        ##users.remove(self.client.get_user(921913569132564491))
        #await ctx.send(f"Congratulations {random.choice(users).mention}, you have won the giveaway for: ")
"""


    @commands.command(name = "giveaway")
    @commands.has_permissions(administrator = True)
    async def giveaway(self, ctx : commands.Context, content, duration):
        print(self.giveawayMessage)

        with open("giveaway.txt", "w") as f:
                f.write("")

        if self.giveawayMessage == "":
            view = Confirm()
            embed = await ctx.send(f"Confirm creating this giveaway for duration {duration}?", embed = discord.Embed(title="Giveaway Creation", description=content, colour = 0xED4245, timestamp = ctx.message.created_at), view=view)
        else:
            view = Confirm()
            embed = await ctx.send(embed = discord.Embed(title="Giveaway Creation", description="A giveaway already exists, do you want to overwrite the last one?", colour = 0xED4245, timestamp = ctx.message.created_at), view=view)


        await view.wait()
            
        if view.value is None:
            await ctx.send("Timed out...", duration = 10)
            await embed.delete()

        elif not view.value:
            await embed.delete()
            
        #actually creates giveaway
        else:
            await embed.delete()
            giveawayEmbed = await ctx.send(embed = discord.Embed(title="Giveaway", description=content, colour = 0xED4245, timestamp = ctx.message.created_at))


            with open("giveaway.txt", "w") as f:
                f.write(str(giveawayEmbed.id))
                
                
            msg = discord.utils.get(self.client.cached_messages, id=giveawayEmbed.id)

            for emoji in self.client.emojis:
                if str(emoji.name) == "aevitas":
                    await msg.add_reaction(self.client.get_emoji(emoji.id))

            await asyncio.sleep(int(duration))

            users = await msg.reactions[0].users().flatten()
            users.remove(self.client.get_user(921913569132564491))
            await ctx.send(f"Congratulations {random.choice(users).mention}, you have won the giveaway for: {content}")

            """with open("giveaway.txt", "w") as f:
                f.write("")
        """



    
            
def setup(client):
    client.add_cog(Giveaway(client))