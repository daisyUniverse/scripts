#!/bin/bash

echo "Sending a warning message to all servers of restart"
screen -S release -p 0 -X stuff "say MineOnline Updating... Server restart in 15 Seconds^M"
screen -S beta -p 0 -X stuff "say MineOnline Updating... Server restart in 15 Seconds^M"
screen -S alpha -p 0 -X stuff "say MineOnline Updating... Server restart in 15 Seconds^M"
screen -S classic -p 0 -X stuff "say MineOnline Updating... Server restart in 15 Seconds^M"
screen -S cloth -p 0 -X stuff "say MineOnline Updating... Server restart in 15 Seconds^M"
echo "Waiting 15 seconds..."
sleep 15s
echo "Shutting down all servers."
bash stopservs.sh
echo "Verifying all servers are fully shut down"
bash stopservs.sh
echo "Updating MineOnline to latest Version"
bash updateMO.sh
echo "Starting all servers back up"
bash startservs.sh
echo "Servers have a fresh new copy of MineOnline and have been restarted!"
