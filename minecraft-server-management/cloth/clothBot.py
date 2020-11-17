import discord
import asyncio
import requests
import os
import sys
import math
import subprocess

prefix = '>>'

commands = { # Command names, change these to change the command trigger
    "reload"   : "reload",
    "start"    : "start",
    "restart"  : "restart",
    "update"   : "update",
    "stop"     : "stop",
    "wipe"     : "wipe",
    "announce" : "announce",
    "config"   : "config",
    "help"     : "help",
    "command"  : "command",
    "killworld": "killworld",
    "version"  : "version",
    "repo"     : "repo"
}

allowedUsers = ["128423195366785024","719545123096231956","537334651631435826","766496300140593152"]

async def log(text, user, loglevel):
    if loglevel == 'LOW':
        print(user + ": " + text + "\033[0m")
    elif loglevel == 'MED':
        print('\033[93m[MED] ' + user + ": "+  text + "\033[0m")
    elif loglevel == 'HIGH':
        print('\033[31m[HIGH] ' + user + ": "+  text + "\033[0m")

async def autoUpdater():
    while True:
        channel = client.get_channel(776542321981390859)
        URL = ("https://api.github.com/repos/Luminoso-256/Cloth-Server/releases/latest")
        try:
            r = requests.get(url = URL)
            if r.ok:
                data = r.json()
                latest = (data['name'])

                with open("PCV", "r") as f: 
                    current = f.read()

                if current != data['tag_name']:
                    with open("PCV", "w") as f: 
                        f.write(data['tag_name'])

                    await log("Updated server to " + data['tag_name'] + " from " + current, "Auto", "HIGH")
                    await channel.edit(topic=(latest))
                    await channel.send("A new update of cloth was detected: **" + data['tag_name'] + "**, updating from the current version **" + current + "**")
                    subprocess.Popen(["bash","clothServer","-u"])   
            else:
                await log("Tried to check for an update for the server but didn't get a 200 OK response from Github \n" + str(r.json()), "[AUTO]", "HIGH")
        except Exception as e:
            print(traceback.format_exc())
            if hasattr(e, 'message'):
                await channel.send("```python\nError on line " + str(sys.exc_info()[-1].tb_lineno) + "\n" + str(e.message) + "```")
            else:
                await channel.send("```python\nError on line " + str(sys.exc_info()[-1].tb_lineno) + "\n" + str(e) + "```")

        await asyncio.sleep(300)


class MyClient(discord.Client):
    async def on_ready(self):
      print ('\033[1mWelcome to the Cloth Server Manager by \33[31mRobin Universe\033[0m')
      print ('Bot core loaded as user:', self.user)
      await autoUpdater()

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
                        await message.channel.send("Wiping the userdata of " + msgCaps.split(" ")[1])
                        os.system('bash clothServer -w ' + msgCaps.split(" ")[1])

                    if msg.startswith(commands['announce']):
                        await log(commands['announce'] + " command used", str(message.author), "LOW")
                        await message.channel.send("Sent to the server")
                        os.system('bash clothServer -a "' + msgCaps[len(commands['announce'])+3:] + '"')

                    if msg.startswith(commands['killworld']):
                        await log(commands['killworld'] + " command used", str(message.author), "HIGH")
                        await message.channel.send("Deleting world and restarting the server...")
                        os.system('bash clothServer --DESTROY')

                    if msg.startswith(commands['version']):
                        await log(commands['version'] + " command used", str(message.author), "LOW")
                        with open("PCV", "r") as f: 
                            current = f.read()
                        await message.channel.send("The current running version of Cloth is " + current)

                    if msg.startswith(commands['repo']):
                        await log(commands['repo'] + " command used", str(message.author), "LOW")
                        await message.channel.send("https://github.com/Luminoso-256/Cloth-Server")

                    if msg.startswith(commands['command']):
                        await log("server command " + msgCaps[len(commands['announce'])+2:] + " used", str(message.author), "MED")
                        await message.channel.send("Executing command `" + msgCaps[len(commands['announce'])+2:] + "` on server")
                        output = subprocess.check_output('bash clothServer -c "' + msgCaps[len(commands['announce'])+2:] + '"', shell=True)
                        await message.channel.send("**SERVER:** `" + output.decode('ascii', errors='ignore') + "`")

                    if msg.startswith(commands['config']):
                        file = msg.split(" ")[1]
                        rest = msg[len( commands['announce']) + len(file):]
                        prop = rest.split("=")[0]
                        oldval = " "
                        oldline = " "
                        newline = ""
                        val  = rest[len(rest.split("=")[1])+1:]

                        with open(file, "r") as f: 
                            config = f.readlines()

                        for line_index, lines in enumerate(config):
                            if lines.split("=")[0] == prop:
                                oldval = lines.split("=")[1]
                                oldline = lines
                                newline = (prop+"="+val.split("=")[1]+"\n")
                                config[line_index] = newline

                        with open(file, "w") as f: 
                            f.writelines(config)
                            await message.channel.send("Config file `" + file + "` updated property `" + prop + "`. changed value `" + oldval + "` to `" + val.split("=")[1] + "`")

                        await log(commands['config'] + " command used", str(message.author), "MED")
                        
                    if msg.startswith(commands['help']):
                        await log(commands['help'] + " command used", str(message.author), "LOW")
                        await message.channel.send(
                            "`"+prefix + "reload` Restarts the bot component" + "\n" +
                            "`"+prefix + "start` Starts the cloth server" + "\n" +
                            "`"+prefix + "restart` Restarts the cloth server" + "\n" +
                            "`"+prefix + "update` Shuts down the cloth server, pulls latest release of cloth, and starts it again" + "\n" +
                            "`"+prefix + "stop` Stops the cloth server" + "\n" +
                            "`"+prefix + "wipe <username>` wipes the playerdata" + "\n" +
                            "`"+prefix + "announce <text>` will do a say command (eventualy)" + "\n" +
			                "`"+prefix + "command <command>` will do a command" + "\n" +
                            "`"+prefix + "killworld` Deletes the world. This is not reversable." + "\n" +
                            "`"+prefix + "config <property.file> <property=newvalue>` updates a property in a file" + "\n" +
                            "`"+prefix + "version` Shows the version of Cloth Server the server is currently running" + "\n" +
                            "`"+prefix + "repo` links the github repo" + "\n" +
                            "`"+prefix + "help` take a wild fuckin guess buddy" + "\n")

                except Exception as e: # returns error meesages to discord in a python codeblock for debugging
                    print(traceback.format_exc())
                    if hasattr(e, 'message'):
                        await channel.send("```python\nError on line " + str(sys.exc_info()[-1].tb_lineno) + "\n" + str(e.message) + "```")
                    else:
                        await channel.send("```python\nError on line " + str(sys.exc_info()[-1].tb_lineno) + "\n" + str(e) + "```")

client = MyClient()
client.run('PUT YOUR TOKEN HERE')
