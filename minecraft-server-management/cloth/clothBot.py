import discord
import asyncio
import requests
import os
import sys
import math

prefix = '>>'

commands = { # Command names, change these to change the command trigger
    "reload"   : "reload",
    "start"    : "start",
    "restart"  : "restart",
    "update"   : "update",
    "stop"     : "stop",
    "wipe"     : "wipe",
    "announce" : "announce"
}

allowedUsers = ["128423195366785024","719545123096231956"]

async def log(text, user, loglevel):
    if loglevel == 'LOW':
        print(user + ": " + text + "\033[0m")
    elif loglevel == 'MED':
        print('\033[93m[MED] ' + user + ": "+  text + "\033[0m")
    elif loglevel == 'HIGH':
        print('\033[31m[HIGH] ' + user + ": "+  text + "\033[0m")

class MyClient(discord.Client):
    async def on_ready(self):
      print ('\033[1mWelcome to the Cloth Server Manager by \33[31mRobin Universe\033[0m')
      print ('Bot core loaded as user:', self.user)

    async def on_message(self, message):
        msgCaps = message.content
        msg     = message.content.lower()

        if message.author == self.user:
            return

        if str(message.author.id) in allowedUsers: 
            if msg.startswith(prefix):
                try:
                    msg = msg[len(prefix):]

                    if msg.startswith(commands['reload']):
                        await log(commands['reload'] + " command used", str(message.author), "LOW")
                        await message.channel.send("Restarting Cloth Server Manager...")
                        os.execl(sys.executable, sys.executable, *sys.argv)

                    if msg.startswith(commands['start']):
                        await log(commands['start'] + " command used", str(message.author), "MED")
                        await message.channel.send("Starting the Cloth server...")
                        os.system('bash clothServer -s')

                    if msg.startswith(commands['stop']):
                        await log(commands['stop'] + " command used", str(message.author), "MED")
                        await message.channel.send("Stopping the Cloth server...")
                        os.system('bash clothServer -q')

                    if msg.startswith(commands['restart']):
                        await log(commands['restart'] + " command used", str(message.author), "MED")
                        await message.channel.send("Restarting the Cloth server...")
                        os.system('bash clothServer -r')

                    if msg.startswith(commands['update']):
                        await log(commands['update'] + " command used", str(message.author), "HIGH")
                        await message.channel.send("Updating the Cloth server...")
                        os.system('bash clothServer -u')

                    if msg.startswith(commands['wipe']):
                        await log(commands['wipe'] + " command used", str(message.author), "HIGH")
                        await message.channel.send("Wiping the userdata of " + msg[len(commands['wipe'])+1:] + " and restarting the server... ")
                        os.system('bash clothServer -w ' + msg[len(commands['wipe'])+1:])

                    if msg.startswith(commands['announce']):
                        await log(commands['announce'] + " command used", str(message.author), "LOW")
                        await message.channel.send("Updating the Cloth server...")
                        os.system('bash clothServer -a "' + msg[len(commands['announce'])+1:] + '"')

                except Exception as e: # returns error meesages to discord in a python codeblock for debugging
                    print(traceback.format_exc())
                    if hasattr(e, 'message'):
                        await channel.send("```python\nError on line " + str(sys.exc_info()[-1].tb_lineno) + "\n" + str(e.message) + "```")
                    else:
                        await channel.send("```python\nError on line " + str(sys.exc_info()[-1].tb_lineno) + "\n" + str(e) + "```")

client = MyClient()
client.run('PUT YOUR TOKEN HERE')
