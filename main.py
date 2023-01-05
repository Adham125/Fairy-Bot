import os
import discord
from discord.ext import commands
from random import *
import time

intents = discord.Intents.all()
client = commands.Bot(command_prefix='~', intents=intents)

bot_id = 1053730725507121172
kevin_id = 336153574088376331
my_id = 378212274084773889
welcome_ch = 958048038595723335
leave_ch = 1058046679712026696
react_ch = 1058049119102447806
apex = '<:APEX:1055351272296960010>' #only custom emoji's have this format
LOL = '<:LOL:1055350832423505950>'
pubg = '<:PUBG:1055351307659124870>'
naraka = '<:NARAKA:1055351297894776922>'
dbd = '<:DBD:1055351286083625001>'
blackdesert = '<:BLACKDESERT:1055348663267901461>'

berserker='<:berserker:1058394958266122280>'
paladin='<:paladin:1058395259555557438>'
gunlancer='<:gunlancer:1058395258288885770>'
destroyer='<:destroyer:1058394963521572965>'

striker='<:striker:1058395267407286403>'
wardancer='<:wardancer:1058394978373607474>'
scrapper='<:scrapper:1058394970945499157>'
soulfist='<:soulfist:1058395266048335933>'
glaivier='<:glaivier:1058394965627129906>'

gunslinger='<:gunslinger:1058394967623598150>'
artillerist='<:artillerist:1058394952142422038>'
deadeye='<:deadeye:1058394959931244565>'
sharpshooter='<:sharpshooter:1058395264819396639>'
scouter='<:scouter:1058395262055358555>'

bard='<:bard:1058394955862781992>'
sorceress='<:sorceress:1058394974636478474>'
arcana='<:arcana:1058394950896734228>'
summoner='<:summoner:1058395268942401556>'

shadowhunter='<:shadowhunter:1058395263473025154>'
deathblade='<:deathblade:1058394962078740531>'
reaper='<:reaper:1058395260839018596>'

lostarkartist='<:lostarkartist:1058394954084397138>'
aeromancer='<:aeromancer:1058394949772648528>'


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    print("")
    Channel = client.get_channel(react_ch)
    await Channel.purge()
    msg = await Channel.send("請在以下按反應選擇你有在遊玩的遊戲以獲取身份組\n\n▸ "+apex+"　Apex英雄 Apex Legends\n▸ "+LOL+"　英雄聯盟 League of Legends\n▸ "+pubg+"　絕地求生 PUBG: BATTLEGROUNDS\n▸ "+naraka+"　永劫無間 NARAKA: BLADEPOINT\n▸ "+dbd+"　黎明死線 Dead By Daylight\n▸ "+blackdesert+"　黑色沙漠 Black Desert\n")
    msg2 = await Channel.send(
        "ˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣ\n"
        "請在以下按反應選擇你有在遊玩的職業以獲取身份組\n\n"

        "【　戰士 Warrior　】\n\n"

        "<:berserker:1058394958266122280> 狂戰 Berserker\n"
        "<:paladin:1058395259555557438> 聖騎 Paladin\n"
        "<:gunlancer:1058395258288885770> 督軍 Ganlancer\n"
        "<:destroyer:1058394963521572965> 毀滅 Destroyer"
    )
    msg3 = await Channel.send(
        "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\n"
        "【　武鬥 Martial Artist　】\n\n"

        "<:striker:1058395267407286403> 決鬥 Striker\n"
        "<:wardancer:1058394978373607474> 格鬥 Wardancer\n"
        "<:scrapper:1058394970945499157> 拳霸 Scrapper\n"
        "<:soulfist:1058395266048335933> 氣功 Soulfist\n"
        "<:glaivier:1058394965627129906> 槍術 Glaivier"
    )
    msg4 = await Channel.send(
        "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\n"
        "【　射手 Hunter　】\n\n"

        "<:gunslinger:1058394967623598150> 女槍 Gunslinger\n"
        "<:artillerist:1058394952142422038> 槍炮 Artillerist\n"
        "<:deadeye:1058394959931244565> 男槍 Deadeye\n"
        "<:sharpshooter:1058395264819396639> 弓手 Sharpshooter\n"
        "<:scouter:1058395262055358555> 哨兵 Machinist"
    )
    msg5 = await Channel.send(
        "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\n"
        "【　法師 Mage　】\n\n"

        "<:bard:1058394955862781992> 詩人 Bard\n"
        "<:sorceress:1058394974636478474> 女巫 Sorceress\n"
        "<:arcana:1058394950896734228> 卡牌 Arcanist\n"
        "<:summoner:1058395268942401556> 召喚 Summoner"
    )
    msg6 = await Channel.send(
        "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\n"
        "【　刺客 Assassin　】\n\n"

        "<:shadowhunter:1058395263473025154> 半魔 Demonic\n"
        "<:deathblade:1058394962078740531> 刀鋒 Deathblade\n"
        "<:reaper:1058395260839018596> 死神 Reaper\n"
    )
    msg7 = await Channel.send(
        "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\n"
        "【　專家 Specialist　】\n\n"

        "<:lostarkartist:1058394954084397138> 畫家 Artist\n"
        "<:aeromancer:1058394949772648528> 氣象 Aeromancer"
    )
    await msg.add_reaction(apex)
    await msg.add_reaction(LOL)
    await msg.add_reaction(pubg)
    await msg.add_reaction(naraka)
    await msg.add_reaction(dbd)
    await msg.add_reaction(blackdesert)
    await msg2.add_reaction(berserker)
    await msg2.add_reaction(paladin)
    await msg2.add_reaction(gunlancer)
    await msg2.add_reaction(destroyer)
    await msg3.add_reaction(striker)
    await msg3.add_reaction(wardancer)
    await msg3.add_reaction(scrapper)
    await msg3.add_reaction(soulfist)
    await msg3.add_reaction(glaivier)
    await msg4.add_reaction(gunslinger)
    await msg4.add_reaction(artillerist)
    await msg4.add_reaction(deadeye)
    await msg4.add_reaction(sharpshooter)
    await msg4.add_reaction(scouter)
    await msg5.add_reaction(bard)
    await msg5.add_reaction(sorceress)
    await msg5.add_reaction(arcana)
    await msg5.add_reaction(summoner)
    await msg6.add_reaction(shadowhunter)
    await msg6.add_reaction(deathblade)
    await msg6.add_reaction(reaper)
    await msg7.add_reaction(lostarkartist)
    await msg7.add_reaction(aeromancer)


@client.event
async def on_member_join(member):
    time.sleep(2)
    channel_welcome = client.get_channel(welcome_ch)

    embed = discord.Embed(title='恭喜 {0} 成功抵達夢幻島！'.format(member.name),
                          description="NEVERLAND，有人譯作夢幻島、永無鄉…\n"
                                "衰老、哀傷、孤寂禁區，亦不存於世界之地。\n\n"

                                "夢幻島是出自小飛俠彼得潘中的一個海島，\n"
                                "島上的人不被時間推著前行，忘卻世間煩憂，\n"
                                "初衷在這不會被磨蝕；童心在這不會被吞噬。\n\n"
                                
                                "傳說中，迷失的孩子會走到夢幻島，\n"
                                "那是安全的避風港，在島上的孩子不會長大，\n"
                                "夢想都能夠實現，成為各自故事中的主人翁。\n\n"
                                
                                "縱使活著面對困苦挫敗，人們被逼往前踏著，\n"
                                "但至少在NEVERLAND，我們能夠拋下世俗，\n"
                                "以童心為筆，歡笑為墨，\n\n"
                                
                                "譜寫出屬於我們的冒險故事 ✿",
                          color=0xD4B9D4)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1058391685266149436/1058459830995660961/banner2.png")
    useravatar = member.display_avatar
    embed.set_thumbnail(url=useravatar.url)
    embed.set_author(name=f'{member}')
    await channel_welcome.send(embed=embed)


@client.event
async def on_member_remove(member):
    user_kevin = client.get_user(kevin_id)
    channel_leave = client.get_channel(leave_ch)
    await channel_leave.send("成員離開:<@" + str(member.id) + "> 已離開群組")
    await user_kevin.send("成員離開:<@" + str(member.id) + "> 已離開群組")


@client.event
async def on_reaction_add(reaction, user):
    Channel = client.get_channel(react_ch)
    server = await client.fetch_guild(958037063469522944)                            #server ID
    if reaction.message.channel.id != Channel.id or user.id == bot_id:
        return
    if str(reaction) == apex:
        Role = discord.utils.get(server.roles, name="APEX")
        await user.add_roles(Role)
    elif str(reaction) == LOL:
        Role = discord.utils.get(server.roles, name="LOL")
        await user.add_roles(Role)
    elif str(reaction) == pubg:
        Role = discord.utils.get(server.roles, name="PUBG")
        await user.add_roles(Role)
    elif str(reaction) == naraka:
        Role = discord.utils.get(server.roles, name="NARAKA")
        await user.add_roles(Role)
    elif str(reaction) == dbd:
        Role = discord.utils.get(server.roles, name="DBD")
        await user.add_roles(Role)
    elif str(reaction) == blackdesert:
        Role = discord.utils.get(server.roles, name="BLACK DESERT")
        await user.add_roles(Role)
    elif str(reaction) == berserker:
        Role = discord.utils.get(server.roles, name="狂戰")
        await user.add_roles(Role)
    elif str(reaction) == paladin:
        Role = discord.utils.get(server.roles, name="聖騎")
        await user.add_roles(Role)
    elif str(reaction) == gunlancer:
        Role = discord.utils.get(server.roles, name="督軍")
        await user.add_roles(Role)
    elif str(reaction) == destroyer:
        Role = discord.utils.get(server.roles, name="毀滅")
        await user.add_roles(Role)
    elif str(reaction) == striker:
        Role = discord.utils.get(server.roles, name="決鬥")
        await user.add_roles(Role)
    elif str(reaction) == wardancer:
        Role = discord.utils.get(server.roles, name="格鬥")
        await user.add_roles(Role)
    elif str(reaction) == scrapper:
        Role = discord.utils.get(server.roles, name="拳霸")
        await user.add_roles(Role)
    elif str(reaction) == soulfist:
        Role = discord.utils.get(server.roles, name="氣功")
        await user.add_roles(Role)
    elif str(reaction) == glaivier:
        Role = discord.utils.get(server.roles, name="槍術")
        await user.add_roles(Role)
    elif str(reaction) == gunslinger:
        Role = discord.utils.get(server.roles, name="女槍")
        await user.add_roles(Role)
    elif str(reaction) == artillerist:
        Role = discord.utils.get(server.roles, name="槍炮")
        await user.add_roles(Role)
    elif str(reaction) == deadeye:
        Role = discord.utils.get(server.roles, name="男槍")
        await user.add_roles(Role)
    elif str(reaction) == sharpshooter:
        Role = discord.utils.get(server.roles, name="弓手")
        await user.add_roles(Role)
    elif str(reaction) == scouter:
        Role = discord.utils.get(server.roles, name="哨兵")
        await user.add_roles(Role)
    elif str(reaction) == bard:
        Role = discord.utils.get(server.roles, name="詩人")
        await user.add_roles(Role)
    elif str(reaction) == sorceress:
        Role = discord.utils.get(server.roles, name="女巫")
        await user.add_roles(Role)
    elif str(reaction) == arcana:
        Role = discord.utils.get(server.roles, name="卡牌")
        await user.add_roles(Role)
    elif str(reaction) == summoner:
        Role = discord.utils.get(server.roles, name="召喚")
        await user.add_roles(Role)
    elif str(reaction) == shadowhunter:
        Role = discord.utils.get(server.roles, name="半魔")
        await user.add_roles(Role)
    elif str(reaction) == deathblade:
        Role = discord.utils.get(server.roles, name="刀鋒")
        await user.add_roles(Role)
    elif str(reaction) == reaper:
        Role = discord.utils.get(server.roles, name="死神")
        await user.add_roles(Role)
    elif str(reaction) == lostarkartist:
        Role = discord.utils.get(server.roles, name="畫家")
        await user.add_roles(Role)
    elif str(reaction) == aeromancer:
        Role = discord.utils.get(server.roles, name="氣象")
        await user.add_roles(Role)


@client.event
async def on_reaction_remove(reaction, user):
    Channel = client.get_channel(react_ch)
    server = await client.fetch_guild(958037063469522944)  # server ID
    if reaction.message.channel.id != Channel.id or user.id == bot_id:
        return
    if str(reaction) == apex:
        Role = discord.utils.get(server.roles, name="APEX")
        await user.remove_roles(Role)
    elif str(reaction) == LOL:
        Role = discord.utils.get(server.roles, name="LOL")
        await user.remove_roles(Role)
    elif str(reaction) == pubg:
        Role = discord.utils.get(server.roles, name="PUBG")
        await user.remove_roles(Role)
    elif str(reaction) == naraka:
        Role = discord.utils.get(server.roles, name="NARAKA")
        await user.remove_roles(Role)
    elif str(reaction) == dbd:
        Role = discord.utils.get(server.roles, name="DBD")
        await user.remove_roles(Role)
    elif str(reaction) == blackdesert:
        Role = discord.utils.get(server.roles, name="BLACK DESERT")
        await user.remove_roles(Role)
    elif str(reaction) == berserker:
        Role = discord.utils.get(server.roles, name="狂戰")
        await user.remove_roles(Role)
    elif str(reaction) == paladin:
        Role = discord.utils.get(server.roles, name="聖騎")
        await user.remove_roles(Role)
    elif str(reaction) == gunlancer:
        Role = discord.utils.get(server.roles, name="督軍")
        await user.remove_roles(Role)
    elif str(reaction) == destroyer:
        Role = discord.utils.get(server.roles, name="毀滅")
        await user.remove_roles(Role)
    elif str(reaction) == striker:
        Role = discord.utils.get(server.roles, name="決鬥")
        await user.remove_roles(Role)
    elif str(reaction) == wardancer:
        Role = discord.utils.get(server.roles, name="格鬥")
        await user.remove_roles(Role)
    elif str(reaction) == scrapper:
        Role = discord.utils.get(server.roles, name="拳霸")
        await user.remove_roles(Role)
    elif str(reaction) == soulfist:
        Role = discord.utils.get(server.roles, name="氣功")
        await user.remove_roles(Role)
    elif str(reaction) == glaivier:
        Role = discord.utils.get(server.roles, name="槍術")
        await user.remove_roles(Role)
    elif str(reaction) == gunslinger:
        Role = discord.utils.get(server.roles, name="女槍")
        await user.remove_roles(Role)
    elif str(reaction) == artillerist:
        Role = discord.utils.get(server.roles, name="槍炮")
        await user.remove_roles(Role)
    elif str(reaction) == deadeye:
        Role = discord.utils.get(server.roles, name="男槍")
        await user.remove_roles(Role)
    elif str(reaction) == sharpshooter:
        Role = discord.utils.get(server.roles, name="弓手")
        await user.remove_roles(Role)
    elif str(reaction) == scouter:
        Role = discord.utils.get(server.roles, name="哨兵")
        await user.remove_roles(Role)
    elif str(reaction) == bard:
        Role = discord.utils.get(server.roles, name="詩人")
        await user.remove_roles(Role)
    elif str(reaction) == sorceress:
        Role = discord.utils.get(server.roles, name="女巫")
        await user.remove_roles(Role)
    elif str(reaction) == arcana:
        Role = discord.utils.get(server.roles, name="卡牌")
        await user.remove_roles(Role)
    elif str(reaction) == summoner:
        Role = discord.utils.get(server.roles, name="召喚")
        await user.remove_roles(Role)
    elif str(reaction) == shadowhunter:
        Role = discord.utils.get(server.roles, name="半魔")
        await user.remove_roles(Role)
    elif str(reaction) == deathblade:
        Role = discord.utils.get(server.roles, name="刀鋒")
        await user.remove_roles(Role)
    elif str(reaction) == reaper:
        Role = discord.utils.get(server.roles, name="死神")
        await user.remove_roles(Role)
    elif str(reaction) == lostarkartist:
        Role = discord.utils.get(server.roles, name="畫家")
        await user.remove_roles(Role)
    elif str(reaction) == aeromancer:
        Role = discord.utils.get(server.roles, name="氣象")
        await user.remove_roles(Role)


@client.command()
async def reaction_reset(ctx):
    if ctx.author.id == kevin_id or ctx.author.id == my_id:
        Channel = client.get_channel(react_ch)
        await Channel.purge()
        msg = await Channel.send(
            "請在以下按反應選擇你有在遊玩的遊戲以獲取身份組\n\n▸ " + apex + "　Apex英雄 Apex Legends\n▸ " + LOL + "　英雄聯盟 League of Legends\n▸ " + pubg + "　絕地求生 PUBG: BATTLEGROUNDS\n▸ " + naraka + "　永劫無間 NARAKA: BLADEPOINT\n▸ " + dbd + "　黎明死線 Dead By Daylight\n▸ " + blackdesert + "　黑色沙漠 Black Desert\n")
        msg2 = await Channel.send(
            "ˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣˣ\n"
            "請在以下按反應選擇你有在遊玩的職業以獲取身份組\n\n"

            "【　戰士 Warrior　】\n\n"

            "<:berserker:1058394958266122280> 狂戰 Berserker\n"
            "<:paladin:1058395259555557438> 聖騎 Paladin\n"
            "<:gunlancer:1058395258288885770> 督軍 Ganlancer\n"
            "<:destroyer:1058394963521572965> 毀滅 Destroyer"
        )
        msg3 = await Channel.send(
            "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\n"
            "【　武鬥 Martial Artist　】\n\n"

            "<:striker:1058395267407286403> 決鬥 Striker\n"
            "<:wardancer:1058394978373607474> 格鬥 Wardancer\n"
            "<:scrapper:1058394970945499157> 拳霸 Scrapper\n"
            "<:soulfist:1058395266048335933> 氣功 Soulfist\n"
            "<:glaivier:1058394965627129906> 槍術 Glaivier"
        )
        msg4 = await Channel.send(
            "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\n"
            "【　射手 Hunter　】\n\n"

            "<:gunslinger:1058394967623598150> 女槍 Gunslinger\n"
            "<:artillerist:1058394952142422038> 槍炮 Artillerist\n"
            "<:deadeye:1058394959931244565> 男槍 Deadeye\n"
            "<:sharpshooter:1058395264819396639> 弓手 Sharpshooter\n"
            "<:scouter:1058395262055358555> 哨兵 Machinist"
        )
        msg5 = await Channel.send(
            "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\n"
            "【　法師 Mage　】\n\n"

            "<:bard:1058394955862781992> 詩人 Bard\n"
            "<:sorceress:1058394974636478474> 女巫 Sorceress\n"
            "<:arcana:1058394950896734228> 卡牌 Arcanist\n"
            "<:summoner:1058395268942401556> 召喚 Summoner"
        )
        msg6 = await Channel.send(
            "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\n"
            "【　刺客 Assassin　】\n\n"

            "<:shadowhunter:1058395263473025154> 半魔 Demonic\n"
            "<:deathblade:1058394962078740531> 刀鋒 Deathblade\n"
            "<:reaper:1058395260839018596> 死神 Reaper\n"
        )
        msg7 = await Channel.send(
            "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n\n"
            "【　專家 Specialist　】\n\n"

            "<:lostarkartist:1058394954084397138> 畫家 Artist\n"
            "<:aeromancer:1058394949772648528> 氣象 Aeromancer"
        )
        await msg.add_reaction(apex)
        await msg.add_reaction(LOL)
        await msg.add_reaction(pubg)
        await msg.add_reaction(naraka)
        await msg.add_reaction(dbd)
        await msg.add_reaction(blackdesert)
        await msg2.add_reaction(berserker)
        await msg2.add_reaction(paladin)
        await msg2.add_reaction(gunlancer)
        await msg2.add_reaction(destroyer)
        await msg3.add_reaction(striker)
        await msg3.add_reaction(wardancer)
        await msg3.add_reaction(scrapper)
        await msg3.add_reaction(soulfist)
        await msg3.add_reaction(glaivier)
        await msg4.add_reaction(gunslinger)
        await msg4.add_reaction(artillerist)
        await msg4.add_reaction(deadeye)
        await msg4.add_reaction(sharpshooter)
        await msg4.add_reaction(scouter)
        await msg5.add_reaction(bard)
        await msg5.add_reaction(sorceress)
        await msg5.add_reaction(arcana)
        await msg5.add_reaction(summoner)
        await msg6.add_reaction(shadowhunter)
        await msg6.add_reaction(deathblade)
        await msg6.add_reaction(reaper)
        await msg7.add_reaction(lostarkartist)
        await msg7.add_reaction(aeromancer)


@client.command()
async def Q1(ctx):
    channel = client.get_channel(958085366546583653)
    if ctx.channel.id == 1058047748206768180:
        await ctx.send(
            "［Neverland］創立是為了建築一個安全友善的遊戲環境，保障大家的遊戲體驗，並和大家共同進退。\n"
            "我們的發展方針是希望建立一個能夠讓大家有歸屬感的大家庭。\n\n"

            "夢幻島一共有兩個公會：\n"
            "［Neverland］是為了公會戰與排名而設立的總部，希望在總部的居民們可以一起為公會資源而奮鬥。\n"
            "而［夢幻島］是為休閒玩家設立的分部，讓不善戰的居民有一個安身之處，能放心體驗各種遊戲內容。\n\n"

            "如果想知道更多詳情，可至 {0} 查看".format(channel.mention)
        )


@client.command()
async def Q2(ctx):
    if ctx.channel.id == 1058047748206768180:
        await ctx.send(
            "夢幻島幹部成員\n\n"

            "男會長：小萌\n"
            "負責內容：所有事務\n\n"

            "女秘書：純\n"
            "負責內容：所有事務\n\n"

            "美術及活動組 - 女組長：茉然\n"
            "負責內容：美術及活動相關事務\n\n"

            "戰場及PVP組 - 男組長：CC\n"
            "負責內容：公會戰及PVP相關事務"
        )


@client.command()
async def Q3(ctx):
    if ctx.channel.id == 1058047748206768180:
        await ctx.send(
            "夢幻島幹部成員\n\n"

            "男會長：小萌\n"
            "負責內容：所有事務\n\n"
            
            "女秘書：純\n"
            "負責內容：所有事務\n\n"
            
            "美術及活動組 - 女組長：茉然\n"
            "負責內容：美術及活動相關事務\n\n"
            
            "戰場及PVP組 - 男組長：CC\n"
            "負責內容：公會戰及PVP相關事務\n\n"
            
            "生活輔導組 - 男組長：雞絲\n"
            "負責內容：休閒社區管理相關事務"
        )


@client.command()
async def Q4(ctx):
    if ctx.channel.id == 1058047748206768180:
        await ctx.send(
            "有意申請成為幹部的居民可以向有興趣領域的負責幹部或秘書直接提出申請。\n"
            "通過幹部審核後有機會成為幹部候補一起參與公會營運，然後通過觀察期後便可以正式成為夢幻島幹部一員。\n"
        )


@client.command()
async def Q5(ctx):
    if ctx.channel.id == 1058047748206768180:
        channel = client.get_channel(react_ch)
        await ctx.send(
            "若想要尋找或尋求職業攻略，須先到 {0} 選擇職業，獲得身份組後便可以在Discord頻道列表的 Build 類別下看到相關職業的資訊。 ".format(
                channel.mention)
        )


@client.command()
async def Q6(ctx):
    if ctx.channel.id == 1058047748206768180:
        channel = client.get_channel(1060376356480888832)
        await ctx.send(
            "若想要尋找或尋求副本攻略，可以前往Discord頻道列表的 Member 類別下 {0} 尋找相關副本的資訊。".format(
                channel.mention)
        )


@client.command()
async def Q7(ctx):
    if ctx.channel.id == 1058047748206768180:
        channel = client.get_channel(958085936531538001)
        await ctx.send(
            "若想要尋找或尋求收藏品攻略，可以前往Discord頻道列表的 Member 類別下 {0}  尋找相關收藏品的資訊。".format(
                channel.mention)
        )


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

client.remove_command('help')


@client.command(name="help", help="Displays all the available commands")
async def help(ctx):
    channel = client.get_channel(958037064102867016)
    help_msg = """
    ```
    您好，這裡是夢幻島的小幫手，專門來幫助迷路的小伙伴。
    如果你有遇到以下困難，可以在此頻道輸入以下指令（例：~Q1）

    ~Q1 ┈┈┈ 介紹公會
    ~Q2 ┈┈┈ 幹部簡介
    ~Q3 ┈┈┈ 尋求協助
    ~Q4 ┈┈┈ 申請幹部
    ~Q5 ┈┈┈ 職業攻略
    ~Q6 ┈┈┈ 副本攻略
    ~Q7 ┈┈┈ 收藏攻略

    如果尋求內容不包括在以上分類，或者以上內容未能協助解決問題，
    歡迎在 [𝑁𝑒𝑣𝑒𝑟𝑙𝑎𝑛𝑑-聊天] 或私下向幹部們提出。
    ```
    """

    await ctx.send(help_msg)


@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.errors.BadArgument):
        await ctx.send("輸入次數必須為整數!")


client.run("MTA1MzczMDcyNTUwNzEyMTE3Mg.G3MGCW.bXwlFlIOH-G2rHwKqeLfBMhX0QI3yUvCAXlOag")
