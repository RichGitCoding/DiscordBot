
import discord
import random
from discord.ext import commands
import asyncio
import webserver as f1
import os
from flask import Flask
from threading import Thread


#DISCORD_BOT_SECRET = TOKEN, in .env file located in same directory

TOKEN = 'Your token Here'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return
    
    if message.channel.name == 'mod-chat'or 'vids'or 'self-promo' or 'feed-the-bots' or 'vids' or 'announcements' or 'the-deep':
        if user_message.lower()=='hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower()=='bye':
            await message.channel.send(f'Ara Ara  {username}!')
            return
        elif user_message.lower()=='!random':
            response = f'Random Number: {random.randrange(1000000)}' 
            await message.channel.send(response)
            return
    
f1.keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)




