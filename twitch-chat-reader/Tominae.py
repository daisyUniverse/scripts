import socket
import os
import subprocess
import sys
import random
import twitch
import wordfilter

import gi
gi.require_version('Playerctl', '2.0')

from gi.repository import Playerctl, GLib
from subprocess import Popen
from pathlib import Path
from acapyla import acapyla

defs = str(Path.home()) + "/.dominae/defs/"
SOUNDS = '/home/evshaddock/.dominae/out/tts/'
cwd = str(Path.home()) + "/.dominae"
SH = cwd + "/sh"
player = Playerctl.Player()

def on_track_change(player, e):  # Writes to a file when my spotify track changes, to display it on stream
    track_info = '{artist} - {title}'.format(artist=player.get_artist(), title=player.get_title())
    f = open(cwd + "/txt/playing", "w")
    f.write(track_info)
    f.close() 

player.on('metadata', on_track_change)

a = 0
HOST = "irc.twitch.tv"
PORT = 6667
NICK = NICK GOES HERE
PASS = OAUTH GOES HERE

voiceslist = ["willbadguy", "willfromafar", 
              "willhappy", "willlittlecreature", "willoldman", "willsad", "willupclose" ]

consolecolors = [ "\u001b[31m", "\u001b[32m", "\u001b[33m", "\u001b[34m", "\u001b[35m", # for console text chat
                  "\u001b[36m", "\u001b[31;1m", "\u001b[32;1m", "\u001b[33;1m", 
                  "\u001b[34;1m", "\u001b[35;1m", "\u001b[36;1m" ]

random.shuffle(voiceslist) # Randomly shuffles voice list on each startup to avoid getting stuck with lame voices
random.shuffle(consolecolors) # same

print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
print("Welcome to the " + random.choice(consolecolors) + "Eli Stream \u001b[0m :)")
print("(Twitch Chat Handler by \u001b[35mMaddox \u001b[0m+ \u001b[31mEli)")
print("Mid-Stream TTS Disabler by \u001b[35mSUPER EPIC MADDOX\u001b[0m")

def handle_message(message: twitch.chat.Message) -> None:

    try:
        with open(defs + message.sender + '.txt','r') as deffile:
            voiceid = deffile.read()
    except FileNotFoundError:
        random.seed(message.sender)
        voiceid = random.choice(voiceslist)
    random.seed(message.sender)
    color = random.choice(consolecolors) + "\u001b[1m"
    print(color +  message.sender + "\u001b[0m : "+ message.text)
    with open(defs + "nospeak" + '.txt','r') as speakfile:
        nospeak = speakfile.read()

    if wordfilter.blacklisted(message.text) == False:
        if message.text.startswith('Eli, '):
            try:
                fn = acapyla(message.text, voiceid)
            except:
                fn = acapyla("COMMAND ERROR IN PHONEME", voiceid)
            subprocess.Popen(['play', SOUNDS + fn + '.mp3'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            subprocess.Popen([SH + "/sdischo.sh", message.sender+": "+message.text], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            subprocess.Popen(["notify-send", message.sender+": "+message.text], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        elif message.text.startswith('$voice'):
            rest = message.text.replace('$voice ','')
            if rest in voiceslist:
                with open(defs + message.sender + '.txt','w') as deffile:
                    deffile.write(rest)
                message.chat.send('Voice for ' + message.sender + ' changed to ' + rest + "!")
            else:
                message.chat.send('Invalid voice!')
        elif message.text.startswith('$nospeak'): # Please make this permission-based
            if message.sender == "eli_tv" or message.sender == "maddoxdragon":
                with open(defs + "nospeak" + '.txt','w') as speakfile:
                    speakfile.write("True")
                message.chat.send('TTS Disabled!')
        elif message.text.startswith('$speak'):
            if message.sender == "eli_tv" or message.sender == "maddoxdragon":
                with open(defs + "nospeak" + '.txt','w') as speakfile:
                    speakfile.write("False")
                message.chat.send('TTS Enabled!')
        elif message.text.startswith('$restart'):
            if message.sender == "eli_tv" or message.sender == "maddoxdragon":
                os.execl(sys.executable, sys.executable, *sys.argv)
        elif nospeak == "True":
            subprocess.Popen([SH + "/sdischo.sh", message.sender+": "+message.text], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        else:
            message.text = message.text.replace("IT","it")
            try:
                fn = acapyla(message.text, voiceid)
            except:
                fn = acapyla("COMMAND ERROR IN PHONEME", voiceid)
            if message.text.startswith('!!'):
                subprocess.Popen(['play', SOUNDS + fn + '.mp3', "tempo", "2"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            else:
                subprocess.Popen(['play', SOUNDS + fn + '.mp3'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            subprocess.Popen([SH + "/sdischo.sh", message.sender+": "+message.text], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    else:
        message.chat.send("I'm not going to say that. Stop it.")

def main():
    chat = twitch.Chat(channel='#' + NICK,
                       nickname=NICK,
                       oauth=PASS,
                       helix=twitch.Helix(client_id=PASS, use_cache=True))
    chat.subscribe(handle_message)

if __name__ == '__main__':
    main()
    GLib.MainLoop().run()
