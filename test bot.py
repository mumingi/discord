import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("무민기 봇")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!무민기"):
        await message.channel.send("우주최강귀여미")

    if message.content.startswith("/s"):
        channel = message.content[3:21]
        msg = message.content [22:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("/dm"):
       author = message.guild.get_member(int(message.content[4:22]))
       msg = message.content[23:]
       await message.author.send(msg)

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
