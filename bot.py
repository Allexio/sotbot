import os
import discord
import my_parser
KEYWORD = "sot"

client = discord.Client()

@client.event
async def on_ready():
    print('Bot has logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(KEYWORD):
        await message.channel.send(my_parser.parser(message.content.replace(KEYWORD, "")))

def startup():
    client.run(os.getenv("discord_sot_token"))

startup()