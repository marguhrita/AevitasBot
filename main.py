#pip install git+https://github.com/Rapptz/discord.py

#from discord.ui import button, Button, View
##from discord.interactions import Interaction
from discord.activity import CustomActivity
from discord.ext import commands
import discord, os


intents = discord.Intents.all()
"""intents.guilds = True
#intents.messages = True
intents.members = True
#intents.voice_states = True
intents.presences = True
intents.emojis = True
intents.reactions = True"""


#, activity=discord.Game("aevitasmc.com")

client = commands.Bot(command_prefix='#', intents = intents, activity=discord.Game("aevitasmc.com"))
client.huh = "yuh"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_update(before, after):
  channel = client.get_channel(867340695723311135)
  if "Streaming" in str(after.activities):
    await channel.send(f"{str(after)} STARTED STREAMMING !?!!?!")


@client.event
async def on_message(message):

  
  #allows us to use commands as well as the on_message event
  await client.process_commands(message)



#X1pe0 Was here :)

#<----------------------------------------------------->

#client.load_extension("cogs.Admin")

for extension in os.listdir("./cogs/"):
  print("loading cogs..")
  if extension.endswith(".py"):
    client.load_extension(f"cogs.{extension[:-3]}")


#runs the discord bot
#aevitasMC
#client.run("OTIyNTY2NTYyMzY2NDg4NTg3.YcDVEA.32iM_ap3d-eeWljuohEndmKKMB0")
#aevitas
with open("token.txt", "r") as f:
  token = f.read().rstrip()
  client.run(token)






