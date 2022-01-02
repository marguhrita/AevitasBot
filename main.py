#pip install git+https://github.com/Rapptz/discord.py

#from discord.ui import button, Button, View
##from discord.interactions import Interaction
from discord.activity import CustomActivity
from discord.ext import commands
import json, time, random, discord, requests, datetime
import asyncio, os


BLWords = ["nigger", "retard", "nigga", "卐", "faggot", "freetard", ".discord.gg", "discordapp.com/invite", "discord.me", "fag"]


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


#functions


def userInLevelsFile(data, userid):
  if userid in [x['user'] for x in data['data']]:
    return True
  else: return False

def addUserToLevelsFile(data, userid, xp, lastmessage, level):
  data['data'].append({"user":userid, "totalxp":xp, "lastmessage":lastmessage, "level":level})
  return data

def updateLevelsFile(data):
  with open ("levels.json", "w") as g:
    json.dump(data, g)


@client.command()
async def stream(ctx):
  await client.change_presence(activity=discord.Streaming(name="yuh", url="https://twitch.tv/aevitas"))
  

@client.command(name="avatar", aliases = ["pfp"])
async def getAvatar(ctx):
  
  avatarUrl = ctx.author.avatar
  await ctx.send(avatarUrl)




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    return

@client.event
async def on_member_update(before, after):
  channel = client.get_channel(867340695723311135)
  if "Streaming" in str(after.activities):
    await channel.send(f"{str(after)} STARTED STREAMMING !?!!?!")


@client.event
async def on_message(message):
  if message.author == client.user or message.author.bot or message.author == client.get_user(867339991847403550):
    return

  troubleShootingChannel = client.get_channel(867340695723311135)
  #loop for each word in "BLWords" list
  for word in BLWords:

    #deletes message if the word is found inside the message
    if word in message.content.lower():
      print("Blacklisted word found")
      await message.delete()

      #sends a private warning message to the sender of the message 
      await message.author.send(f"Langauge such as {word} is not permitted in the Aevitas server")
  
  

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






