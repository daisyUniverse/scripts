#!/bin/bash

latest=$(curl -s "https://api.github.com/repos/codieradical/MineOnline/releases/latest" | jq -r '.tag_name')
current=$(cat MOV)

if [ "$current" != "$latest" ]
then
	echo "Detected version difference, updating MineOnline version $current to $latest..."
	sleep 1s
	wget "https://github.com/codieradical/MineOnline/releases/download/$latest/MineOnline.jar"
	chmod +x MineOnline.jar
	parallel cp MineOnline.jar ::: release/ beta/ alpha/ classic/ cloth/
	rm MineOnline.jar
	echo $latest > MOV
	echo "MineOnline updated to version: $latest"
else
	echo "You already have the latest version: $current"
fi
