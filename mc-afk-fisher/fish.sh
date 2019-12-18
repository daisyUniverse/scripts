#!/bin/bash

WID=`xdotool search --class minecraft`
xdotool mousedown --window $WID 3
echo "Minecraft (Window ID $WID) Mousedown signal sent..." 
