import asyncio
import discord
import sys
from discord.ext.commands import Bot
from discord.ext import commands

client = commands.Bot(command_prefix='>')

#clearbot - Purge your sins

tokenfile = open('token.txt','r')
token = tokenfile.read()
tokenfile.close()
channel = int(sys.argv[len(sys.argv)-1])
purged = 0

print("Purging Channel ID:" + str(channel) + " of all messages...")

@client.event
async def on_ready():
    async for msg in client.get_channel(channel).history():
        await msg.delete()
        global purged
        purged += 1
        print("Purged...")
    print(str(purged) + " messages have been purged. Have a nice day!")
    exit()

client.run(token)