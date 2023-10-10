import discord
import time
import random

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

videoData = ["dQw4w9WgXcQ","O2Yzui5PrYE",
"BKblrXHumDk","85OLkAFOlYM",
"dr6NMg069xo","pFgUluV_00s",
"M7szcadThQc","zpVEZJ7jYPM",
"wuUATtb7Bv4&t","aoCmdBbcrWE",
"Y6BREbEztjM","Ci_zad39Uhw",
"SvFPHjAXHo8","DnOzG0rCGi0",
"XyE_TPj4l0Q","EHBFKhLUVig",
"hZFBTnzKa54","shs0rAiwsGQ",
"dHXC_ahjtEE","v_uIrtBZXEk",
"nTSyswJjxfY","jXpgf_K1m_g",
"yVaeEsxpidA","jD9XIM7C7UM",
"w8yweCungCE","LYWP8HtgeLQ"]
pictureData = ["ERGceX8","kzYh1D1",
"owXWke4","8hW0yL0",
"bBEwm9x","6nl6JQ4",
"F2cU80D"]

@client.event
async def on_ready():
    print("機器人已連接到伺服器")

@client.event
async def on_message(message):
    if message.content == ("我們的救世主是誰?"):
        await message.channel.send("許昭文!")
    elif message.content == ("原神，啟動!"):
        await message.channel.send("原來你也玩原神")
    elif message.content == ("八十萬對六十萬"):
        await message.channel.send("優勢在我")
    elif message.content == ("好喔"):
        await message.channel.send("喔三小")
    elif message.content == ("<@1152790079497056356>"):
        await message.channel.send("怎麼了嗎?主人喵~")
    elif message.content == ("你是只會說確實這三個字嗎?"):
        await message.channel.send("你也沒好上多少")
    elif message.content == ("幹你娘"):
        await message.channel.send("我沒娘")
    elif message.content == ("他媽的"):
        await message.channel.send("https://w.wiki/7hPG")
    if message.content == ("開始<:smile:1150129717391925358>"):
        while True:
            await message.channel.send("<:smile:1150129717391925358>")
            time.sleep(5)
    if message.content == ("提及edison_lin"):
        提及edison_lin = True
        if message.content == ("stop提及edison_lin"):
            提及edison_lin = False
        while 提及edison_lin:
            await message.channel.send("<@1019985653422891108>")
            time.sleep(1)
        
    if message.content == ("開始_1"):
        while True:
            await message.channel.send("阿菖扶他")
            time.sleep(5)
    if message.content == ("提及qaq2.0"):
        while True:
            await message.channel.send("<@879300609763856435>")
            time.sleep(1)
    if message.content == ("開始_2"):
        while True:
            await message.channel.send("<:cylan:1139877598311231558> <:scaryzhaowen:1142437846565802104> <:iron_cross:1143174282764099664> <:Zhe_ren:1143534490317242420> <:achang2:1143584837970702466> <:achang3:1143585415245336676> <:fuck_money:1143588576685207674> <:love:1143589148284944556> <:ming_feng:1143589515068448818> <:empire_of_zhaowen_sun_flag:1143590947423260783> <:achang4:1143592135803817995> <:hitler_angry:1143592170733969418> <:Acorus:1143592827650060339> <:bitch:1143594095407792279> <:stalin_angry:1143599406151647342> <:__:1143604064194666602> <:bocchi:1143981475809742878> <:sorry_bro:1144003098851942482><:cylan:1139877598311231558> <:scaryzhaowen:1142437846565802104> <:iron_cross:1143174282764099664> <:Zhe_ren:1143534490317242420> <:achang2:1143584837970702466> <:achang3:1143585415245336676> <:fuck_money:1143588576685207674> <:love:1143589148284944556> <:ming_feng:1143589515068448818> <:empire_of_zhaowen_sun_flag:1143590947423260783> <:achang4:1143592135803817995> <:hitler_angry:1143592170733969418> <:Acorus:1143592827650060339> <:bitch:1143594095407792279> <:stalin_angry:1143599406151647342> <:__:1143604064194666602> <:bocchi:1143981475809742878> <:sorry_bro:1144003098851942482><:cylan:1139877598311231558> <:scaryzhaowen:1142437846565802104> <:iron_cross:1143174282764099664> <:Zhe_ren:1143534490317242420> <:achang2:1143584837970702466> <:achang3:1143585415245336676> <:fuck_money:1143588576685207674> <:love:1143589148284944556> <:ming_feng:1143589515068448818> <:empire_of_zhaowen_sun_flag:1143590947423260783> <:achang4:1143592135803817995> <:hitler_angry:1143592170733969418> <:Acorus:1143592827650060339> <:bitch:1143594095407792279> <:stalin_angry:1143599406151647342> <:__:1143604064194666602> <:bocchi:1143981475809742878> <:sorry_bro:1144003098851942482><:cylan:1139877598311231558> <:scaryzhaowen:1142437846565802104> <:iron_cross:1143174282764099664> <:Zhe_ren:1143534490317242420> <:achang2:1143584837970702466> <:achang3:1143585415245336676> <:fuck_money:1143588576685207674>")
            time.sleep(2)
    if message.content == ("<@1152790079497056356> 給我一個影片"):
        video = random.choice(videoData)
        await message.channel.send(f"https://youtu.be/{video}")
    if message.content == ("<@1152790079497056356> 給我一張圖片"):
        picture = random.choice(pictureData)
        await message.channel.send(f"https://imgur.com/{picture}")
    if message.content == ("123"):
        role = message.guild.get_role(1154497333447372882)
        member = message.author
        member.add_roles(role)
        
        
        
@client.event
async def on_ready():
    # 加入語音頻道
    voice_channel = client.get_channel(1141778513985273877)
    await voice_channel.connect()
    voice_channel = client.get_channel(1108064601431621683)
    await voice_channel.connect()


client.run("MTE1Mjc5MDA3OTQ5NzA1NjM1Ng.GDC8wI.shFgt_9NctAAbkK5NgOh40eT5u1HcjHSaHH6J4")