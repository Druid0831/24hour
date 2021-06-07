import discord
import os
import asyncio

client = discord.Client()

token = "access_token"

@client.event
async def on_ready():

    print(client.user.name)
    print('준비완료')
    game = discord.Game('League of Legends')
    await client.change_presence(status=discord.Status.online, activity=game)

    @client.event
    async def on_message(message):
        if message.content == "!아지르":
            embed = discord.Embed(title="아지르, 사막의 황제", description="Azir, the Emperor of the Sands", color=0x000000)
            embed.set_footer(text="'슈리마여, 너의 황제가 돌아왔다!'")
            await message.channel.send(embed=embed)

        if message.content == "!볼리베어":
            embed = discord.Embed(title="볼리베어, 무자비한 폭풍", description="Volibear, the Relentless Storm", color=0x000000)
            embed.set_footer(text="'야생의 힘이다!'")
            await message.channel.send(embed=embed)
        
        if message.content == "!티모":
            await message.channel.send("날쌘 정찰병")

        if message.content == "!유미":
            await message.channel.send("마법 고양이")

        if message.content == "!나르":
            embed = discord.Embed(title="나르, 잃어버린 고리", description="Gnar, the Missing Link", color=0x000000)
            embed.set_footer(text="'나르! 가댜!'")
            await message.channel.send(embed=embed)
            
        if message.content == "!가렌":
            await message.channel.send("데마시아의 힘")

        if message.content == "!케넨":
            await message.channel.send("폭풍의 심장")

        if message.content == "!쉔":
            await message.channel.send("황혼의 눈")

        if message.content == "!이즈리얼":
            await message.channel.send("무모한 탐험가")

        if message.content == "!모데카이저":
            await message.channel.send("강철의 망령")

        if message.content == "!다리우스":
            await message.channel.send("녹서스의 실력자")

        if message.content == "!바루스":
            await message.channel.send("응징의 화살")

        if message.content == "!헤카림":
            await message.channel.send("전쟁의 전조")

        if message.content == "!나서스":
            await message.channel.send("사막의 관리자")

        if message.content == "!마스터 이":
            await message.channel.send("우주 검사")

        if message.content == "!야스오":
            embed = discord.Embed(title="야스오, 용서받지 못한 자", description="Yasuo, the Unforgiven", color=0x000000)
            embed.set_footer(text="'죽음은 바람과 같지. 늘 내 곁에 있으니.'")
            await message.channel.send(embed=embed)

        if message.content == "!비에고":
            await message.channel.send("몰락한 왕")

        if message.content == "!아트록스":
           await message.channel.send("다르킨의 검")

        if message.content == "!워윅":
            embed = discord.Embed(title="워윅, 자운의 고삐 풀린 분노", description="Warwick, The Uncaged Wrath of Zaun", color=0x000000)
            embed.set_footer(text="'피비린내다! 도망쳐라...'")
            await message.channel.send(embed=embed)

        if message.content == "!요네":
            embed = discord.Embed(title="요네, 잊히지 못한 자", description="Yone, the Unforgotten", color=0x000000)
            embed.set_footer(text="'하나로 베고, 다른 하나로 봉인하리.'")
            await message.channel.send(embed=embed)
            
access_token = os.environ["BOT_TOKEN"]            
client.run(token)
