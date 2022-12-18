import os
import discord
from discord.ext import commands
from random import *

intents = discord.Intents.all()
client = commands.Bot(command_prefix='~', intents=intents)

kevin_id = 336153574088376331
my_id = 378212274084773889
user_kevin = client.get_user(kevin_id)


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    print("")


@client.event
async def on_member_join(member):
    pass


@client.event
async def on_member_leave(member):

    await user_kevin.send("Member: " + member.name + " Has Left The Server")


@client.command()
async def ping(ctx):
    await my_id.send("hi")


@client.command()
async def rollDice(ctx):
    await ctx.send(randint(1 , 100))

client.run("MTA1MzczMDcyNTUwNzEyMTE3Mg.G3MGCW.bXwlFlIOH-G2rHwKqeLfBMhX0QI3yUvCAXlOag")
