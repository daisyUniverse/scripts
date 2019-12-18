# My Scripts

Hi, I'm Eli. Here are some scripts and config files for my systems. These are kept mostly intact from how I normally use them, so if you want to use them, it may take some tweaking for specific directories and removed credentials if applicable, but there is some useful stuff in here...



## obs-control

This hooks into the Web Request plugin API for OBS, and can be used to control OBS locally or potentially over a network ( untested! ) Currently, only scene and profile switching is supported since that's what I needed it for

`obs-ctrl --scene Webcam`

Needs: **python, obswsrc, asyncio, argparse** 

## spotify-to-discord

This uses dbus to capture the currently playing artist and track name, searches for that on Youtube, and posts the first result to discord using [Discho](https://github.com/Evshaddock/discho)

Needs: **python, jq, discho, python-dbus**

## mc-afk-fisher

Finds the Minecraft window ID and sends it a continuous right click to allow you to AFK fish while using your system for other things

Needs: **xdotool**

## twitch-chat-reader

This ones a bit more complicated as it's a little bit of a multitasker. here are its main functions..

- Display each message sent in a stream text chat in the terminal window with randomized name colors
- Read out each message using a random per-user voice using [Acapyla](https://github.com/maddoxdragon/acapyla)
- Read the currently playing Spotify track, and write it to a file every time a new track starts (to show OBS)
- Automatically censor slurs and especially naughty words using a word block list

and probably some other bits and bobs. This one has a lot of hard-coded directories, so it will take some tweaking to get working on your end, and it kind of relies on an exploit of a website for the audio to work at all, so it could actually just blow up at any moment. use at your own discretion

Needs: **python, twitch, wordfilter, Spotify** (it has to be running before you start the script), **gi, SoX**, probably other stuff. just keep starting it and installing things until it stops complaining lmfao