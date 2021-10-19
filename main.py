import discord
import random
import requests
import json
import time
import datetime
from discord.ext import commands
from alive import keep_alive

bot = commands.Bot(command_prefix="!")

user_reply = ['hi', 'hello', 'wassup', 'hey', 'how r u']
bot_reply = ['hi', 'hello', 'wassup', 'hey', 'how r u']

api = "https://opentdb.com/api.php?amount=1&category=18"

words = ['bad', 'guys', 'guy']

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(word in message.content.lower() for word in user_reply):     # 1
        await message.channel.send(random.choice(bot_reply))

    if message.content.lower() == 'time':                               # 2
        t = datetime.datetime.now().strftime("%I:%M:%S  %p")
        await message.channel.send(t)

    if message.content.lower() == 'trivia':                             # api
        res = requests.get(api)
        data = res.json()
        ques = data['results'][0]['question']
        ans = data['results'][0]['correct_answer']
        await message.channel.send(ques)
        time.sleep(10)
        await message.channel.send(ans)

    if message.content.lower() == 'tri':                                # embeding
        res = requests.get(api)
        data = res.json()
        ques = data['results'][0]['question']
        ans = data['results'][0]['correct_answer']
        emb = discord.Embed(title="Q." + ques, description="Ans." + ans, colour=discord.Colour.random())
        emb.add_field(name='Addition field 1', value='This is a addition field 1', inline=True)
        emb.add_field(name=':blush:', value='[Insta](https://www.instagram.com/)', inline=True)
        emb.set_image(url='https://www.net-aware.org.uk/siteassets/images-and-icons/application-icons/app-icons-discord.png?w=585&scale=down')
        await message.channel.send(embed=emb)

    msg = message.content.lower()
    new = msg.split(" ")

    if any(word in new for word in words):                              # deleting specific message
        await message.delete()
        await message.channel.send("Don't use this type of words")


@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if ctx.author.id == 704582931221577770:
        await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@bot.command()
async def unban(ctx, member : discord.Member, *, reason=None):
    await member.unban(reason=reason)


keep_alive()
bot.run("Your_Bot_Token")
