from dotenv import load_dotenv
load_dotenv()
import os
import discord
from discord.ext import commands
token = os.getenv("TOKEN")
botrole = os.getenv("BOTROLE")
joinchannel = os.getenv("JOINCHANNEL")
chemrole = os.getenv("APCHEMROLE")
intents = discord.Intents.all()
client = commands.Bot(command_prefix="br-",intents=intents)
from flask import Flask
from threading import Thread
app = Flask("BrogreServer")

class Role(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="AP Chem",custom_id="APCHEM", style=discord.ButtonStyle.green)
    async def apchem(self,interaction:discord.Interaction,button):
        await interaction.response.send_message("brother", ephemeral=True)
        await interaction.user.add_roles(interaction.user.guild.get_role(int(chemrole)))

@client.event
async def on_ready():
  print("im up")
  try:
    synched = await client.tree.sync()
    print(f"Synched {len(synched)} commands")
    client.add_view(Role())
  except:
    print("sucks")
  await client.change_presence(activity=discord.Streaming(
    name='brogre', url='https://www.twitch.tv/advikg_'))
  
@client.tree.command(name="class_select")
async def classes(interaction: discord.Interaction):
    embed = discord.Embed(title="Class Selection Form", description="Click buttons to add roles")
    await interaction.response.send_message(embed=embed,view=Role(),ephemeral=True)
  
@client.event
async def on_member_join(member):
    channel = client.get_channel(int(joinchannel))
    if member.bot == True:
      await member.add_roles(botrole)
      return
    await channel.send(
        f"```js\nbrogreMemberList.push({member})\n```{member.mention} do /class_select once advik gives me perms"
    )


@client.event
async def on_member_remove(member):
    channel = client.get_channel(int(joinchannel))
    await channel.send(
        f"```js\nlet oldUser = brogreMemberList.indexOf({member});\nbrogreMemberList.splice(oldUser,1)\n```bye {member.mention}"
    )
    
@app.route('/')
def home():
    return "VividFusion's Server"

def run():
    client.run(token)
def startServer():  

    t = Thread(target=run)
    t.start()
startServer()
#app.run(host="0.0.0.0",port=6221) keep this line on local but not pythonanywhere

