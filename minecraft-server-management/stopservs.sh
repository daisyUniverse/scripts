#!/bin/bash

stopAttempt(){
	echo "Sending STOP commands to all servers."
	screen -S release -p 0 -X stuff "stop^M"
	screen -S beta -p 0 -X stuff "stop^M"
	screen -S alpha -p 0 -X stuff "stop^M"
	screen -S cloth -p 0 -X stuff "stop^M"
	screen -S classic -X quit
	echo "Waiting for a few seconds to wait for all servers to finish shutting down gracefully"
	sleep 30s
}

if ! screen -list | grep -q "release|beta|alpha|classic"; then
    #in a perfect world this would check to see if everything is dead yet
    stopAttempt
else
	echo "Servers no longer detected. Shut down complete"
fi

