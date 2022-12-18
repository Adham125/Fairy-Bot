import os
import discord
from discord.ext import commands
from random import *

intents = discord.Intents.all()
client = commands.Bot(command_prefix='~', intents=intents)

kevin_id = 336153574088376331
my_id = 378212274084773889
welcome_ch = 1053502894290255946


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    print("")


@client.event
async def on_member_join(member):
    channel_welcome = client.get_channel(welcome_ch)
    await channel_welcome.send("Welcome " + member.name + " To The Server!")


@client.event
async def on_member_remove(member):
    user_kevin = client.get_user(kevin_id)
    await user_kevin.send("Member: " + member.name + " Has Left The Server")


@client.command()
async def ping(ctx):
    user_kevin = client.get_user(kevin_id)
    user_me = client.get_user(my_id)
    await user_kevin.send("test")
    await user_me.send("test")


@client.command()
async def roll(ctx, number=1):
    if number < 1:
        await ctx.send("輸入次數必須大於一!")
    elif number > 10:
        await ctx.send("每輪擲骰最多擲十次!")
    elif number == 1:
        await ctx.send("恭喜你骰到 " + str(randint(0, 100)))
    else:
        output = str(randint(0, 100))
        for i in range(number-2):
            output = output + ", " + str(randint(0, 100))
        output = output + " 跟 " + str(randint(0, 100))
        await ctx.send(output)


@roll.error()
async def roll_error(error, ctx):
    if isinstance(error, ValueError):
        await ctx.send("輸入次數必須為整數!")
client.run("MTA1MzczMDcyNTUwNzEyMTE3Mg.G3MGCW.bXwlFlIOH-G2rHwKqeLfBMhX0QI3yUvCAXlOag")
