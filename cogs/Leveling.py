from discord.ext import commands
import discord, requests, json, levelcard, time, random

def randomXp():
  return random.randint(15,25)

def levelBoundary(entry):
  return 5 * (entry['level'] ^ 2) + (50 * entry['level']) + 100 - entry['totalxp']

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


class Leveling(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="rank", aliases = ["level"])
    async def rank(self, ctx, user : discord.User):
        #gets avatar profile picture
        r = requests.get(user.avatar)
  
        #saves profile picture to current directory
        with open("assets/profilepicture.png", "wb") as f:
            f.write(r.content)

        #opens levels.json and loads the contents as a python dictionary list
        with open("levels.json") as f:
            data = json.load(f)

            #loops for each user in the list, and creates the level card where the user id matches the one in the list
            for member in data['data']:
                if str(self.client.get_user(member['user'])) == str(user):
                    levelcard.createCard(str(user), member["totalxp"], levelBoundary(member), member["level"])


        #sends the generated level card to discord channel
        await ctx.send(file=discord.File("assets/levelcard.png"))

    @rank.error
    async def rankError(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingRequiredArgument):
            await self.rank(ctx, ctx.author)
            #await ctx.send(message, delete_after=5)

    @commands.command(name = "asay")
    async def say(self, ctx, msg):
        #channel = self.client.get_channel(910287456182603836)
        channel = self.client.get_channel(910287456182603836)
        #troubleShootingChannel = self.client.get_channel(867340695723311135)

        #await ctx.send(str(channel))
        #msg = await channel.fetch_message(925888009977614486)
        #users = await msg.reactions[0].users().flatten()
        #users.remove(self.client.get_user(921913569132564491))
        #await ctx.send(f"Congratulations {random.choice(users).mention}, you have won the giveaway for: ")
        await channel.send(f"Congratulations {self.client.get_user(819702929115447327).mention}, you have won the giveaway for: ")
        #await ctx.send(msg)


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user or message.author.bot or message.author == self.client.get_user(867339991847403550):
            return

        troubleShootingChannel = self.client.get_channel(867340695723311135)

        #loads json file
        with open("levels.json") as f:
            data = json.load(f)

        #checks if user is *not* already in json file
        if not userInLevelsFile(data, message.author.id):

            #appends user to list
            addUserToLevelsFile(data, message.author.id, 0, time.time(), 0)

            #notifying message once a user has been added
            await troubleShootingChannel.send(f"User {str(message.author)} added")

            #updates levels.json file
            updateLevelsFile(data)

        else:
            #loops through each entry in json file
            for entry in data['data']:
            
                if entry['totalxp'] > levelBoundary(entry) and str(entry['user']) == str(message.author.id):

                    entry['totalxp'] = 0
                    entry['level'] += 1

                    #stores the server the message was sent in
                    guild = message.author.guild

                    #pattern matches for levels we wanna give roles for
                    match entry['level']:
                        case 1:
                            await message.author.add_roles(guild.get_role(922485879631675394))
                        case 5:
                            await message.author.add_roles(guild.get_role(915319942587502642))
                        case 10:
                            await message.author.add_roles(guild.get_role(915319940528087071))
                        case 20:
                            await message.author.add_roles(guild.get_role(915319938930077716))
                        case 30:
                            await message.author.add_roles(guild.get_role(915319936296054844))
                        case 40:
                            await message.author.add_roles(guild.get_role(915319933133533205))
                        case 50:
                            await message.author.add_roles(guild.get_role(915319929891344395))
                        case  _:
                            pass

                    #send message detailing user level up to troubleshooting channel
                    await troubleShootingChannel.send("user {user} is now level {level}".format(user = str(self.client.get_user(message.author.id)), level = str(entry['level'])))

                    #updates json file
                    updateLevelsFile(data)

                else:
        
                    if str(entry['user']) == str(message.author.id) and time.time()-entry['lastmessage'] > 30:

                        entry['totalxp']+=randomXp()

                    #records time of the message
                    entry['lastmessage'] = time.time()

            updateLevelsFile(data)
    
    @commands.command(aliases = ["ranktop, leveltop", "top", "leaderboard"])
    async def ranktop(self, ctx):

        with open("levels.json") as f:
            data = json.load(f)

        for i in range(1,len(data['data'])):
            itemToInsert = data['data'][i]
            j = i-1

            while j>=0 and itemToInsert['level']>data['data'][j]['level']:
                data['data'][j+1] = data['data'][j]
                j-=1
            
            data['data'][j+1] = itemToInsert


        content = ""
        for c in range(10):
            #await ctx.send(f"{c}. {client.get_user(data['data'][c]['user'])} {data['data'][c]['level']}")
            content += f"{c+1}. {self.client.get_user(data['data'][c]['user'])} {data['data'][c]['level']}\n"

        embedvar=discord.Embed(title="Aevitas Leaderboard", description=content, color=0xc368eb)
        await ctx.send(embed = embedvar)

        updateLevelsFile(data)


def setup(client):
    client.add_cog(Leveling(client))