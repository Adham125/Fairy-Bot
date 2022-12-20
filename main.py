import os
import discord
from discord.ext import commands
from random import *

intents = discord.Intents.all()
client = commands.Bot(command_prefix='~', intents=intents)

bot_id = 1053730725507121172
kevin_id = 336153574088376331
my_id = 378212274084773889
welcome_ch = 1053502894290255946
react_ch = 1054767776230813737
emoji1 = '<:test:1054111690230345760>' #only custom emoji's have this format
emoji2 = ''


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    print("")
    Channel = client.get_channel(react_ch)
    await Channel.purge()
    msg = await Channel.send("React to this message to get a role you want")
    await msg.add_reaction(emoji1)


@client.event
async def on_member_join(member):
    channel_welcome = client.get_channel(welcome_ch)
    await channel_welcome.send("Welcome " + member.name + " To The Server!")


@client.event
async def on_member_remove(member):
    user_kevin = client.get_user(kevin_id)
    channel_welcome = client.get_channel(welcome_ch)
    await channel_welcome.send("成員離開:<@" + str(member.id) + "> 已離開群組")
    await user_kevin.send("成員離開:<@" + str(member.id) + "> 已離開群組")


@client.event
async def on_reaction_add(reaction, user):
    Channel = client.get_channel(react_ch)
    server = await client.fetch_guild(1053502894290255943)                            #server ID
    if reaction.message.channel.id != Channel.id or user.id == bot_id:
        return
    if str(reaction) == emoji1:
        Role = discord.utils.get(server.roles, name="test1")
        await user.add_roles(Role)


@client.event
async def on_reaction_remove(reaction, user):
    Channel = client.get_channel(react_ch)
    server = await client.fetch_guild(1053502894290255943)  # server ID
    if reaction.message.channel.id != Channel.id or user.id == bot_id:
        return
    if str(reaction) == emoji1:
        Role = discord.utils.get(server.roles, name="test1")
        await user.remove_roles(Role)


@client.command()
async def reaction_initialize(ctx):
    if ctx.user.id == kevin_id or ctx.user.id == my_id:
        Channel = client.get_channel(react_ch)
        await Channel.purge()
        msg = await Channel.send("React to this message to get a role you want")
        await msg.add_reaction(emoji1)


@client.command()
async def Q1(ctx):
    await ctx.send("A1")


@client.command()
async def Q2(ctx):
    await ctx.send("A2")


@client.command()
async def Q3(ctx):
    await ctx.send("A3")


@client.command()
async def Q4(ctx):
    await ctx.send("A4")


@client.command()
async def roll(ctx, number=1):
    if number < 1:
        await ctx.send("輸入次數必須大於一!")
    elif number > 10:
        await ctx.send("每輪擲骰最多擲十次!")
    elif number == 1:
        await ctx.send("恭喜你骰到 " + str(randint(0, 100)))
    else:
        output = "恭喜你骰到 " + str(randint(0, 100))
        for i in range(number-2):
            output = output + ", " + str(randint(0, 100))
        output = output + " 跟 " + str(randint(0, 100))
        await ctx.send(output)


@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.errors.BadArgument):
        await ctx.send("輸入次數必須為整數!")

client.run("MTA1MzczMDcyNTUwNzEyMTE3Mg.G3MGCW.bXwlFlIOH-G2rHwKqeLfBMhX0QI3yUvCAXlOag")
