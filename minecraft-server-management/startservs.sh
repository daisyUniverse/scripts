#!/bin/bash

cd release/
screen -d -m -S release java -cp MineOnline.jar gg.codie.mineonline.Server server.jar -Xms1G -Xmx2G
cd ../beta/
screen -d -m -S beta java -cp MineOnline.jar gg.codie.mineonline.Server craftbukkit1-7-3.jar -Xms1G -Xmx2G
cd ../alpha/
screen -d -m -S alpha java -cp MineOnline.jar gg.codie.mineonline.Server server.jar -Xms512M -Xmx1G
cd ../classic/
screen -d -m -S classic java -cp MineOnline.jar gg.codie.mineonline.Server minecraft-server.jar -Xms512M -Xmx512M
cd ../cloth/
screen -d -m -S cloth java -cp MineOnline.jar gg.codie.mineonline.Server Server.jar -Xms1G -Xmx2G
