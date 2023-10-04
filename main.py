#pip install git+https://github.com/Rapptz/discord.py
#from discord.ui import button, Button, View
##from discord.interactions import Interaction
from discord.activity import CustomActivity
from discord.ext import commands
import discord, os



"""intents.guilds = True
#intents.messages = True
intents.members = True
#intents.voice_states = True
intents.presences = True
intents.emojis = True
intents.reactions = True"""


#, activity=discord.Game("aevitasmc.com")

#client = commands.Bot(command_prefix='#', intents = intents, activity=discord.Game("aevitasmc.com"))


class MyClient(commands.Bot):

  async def on_ready(self):
    print('We have logged in as {0.user}'.format(client))
    for extension in os.listdir("./cogs/"):
      
      if extension.endswith(".py"):
        print(f"loading cog {extension}")
        self.load_extension(f"cogs.{extension[:-3]}")

  
  async def on_member_update(self, before, after):
    channel = client.get_channel(867340695723311135)
    if "Streaming" in str(after.activities):
      await channel.send(f"{str(after)} STARTED STREAMMING !?!!?!")


  
  async def on_message(self, message):

    #allows us to use commands as well as the on_message event
    await client.process_commands(message)



#X1pe0 Was here :)

#<----------------------------------------------------->


#runs the discord bot
#aevitasMC
#client.run("OTIyNTY2NTYyMzY2NDg4NTg3.YcDVEA.32iM_ap3d-eeWljuohEndmKKMB0")
#aevitas
with open("token.txt", "r") as f:
  token = f.read().rstrip()

  intents = discord.Intents.all()
  client = MyClient(command_prefix='#', intents = intents, activity=discord.Game("aevitasmc.com"))
  client.run(token)






