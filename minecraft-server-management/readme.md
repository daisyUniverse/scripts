# Minecraft Server Management Scripts

These are all the scripts I have keeping my MineOnline minecraft servers up and running smoothly



## Announce

Usage `bash announce "Message you would like sent to all servers"`

This sends a specified message to all running servers



## startservs.sh

This will start all servers in their own named screens. Run this and then use `screen -r` to check available screens. then use `screen -r [name]` to connect to a specified servers screen



## stopservs.sh

This will attempt to gracefully shut down all running minecraft servers by sending a STOP command to each of their screens, except for the classic server, which cannot be shut down gracefully, which is just shut down normally



## updateMO.sh

this will check `MOV` for the current version of MineOnline. if the latest release available does not match the one currently being used, it will download the latest version of MineOnline.jar and copy them to each of the servers folders



## updateRestart.sh

This will gracefully shut down every server, make sure the servers are shut down, and then check for a new version of MineOnline, if there is one, it will be downloaded and copied to each minecraft version folder, after this is finished, it will start all of the servers it it's own screen again.



# cloth

[Cloth](https://github.com/Luminoso-256/Cloth-Server) is a server mod for a1.2.6 by [Luminoso-256](https://github.com/Luminoso-256/) that is under heavy development. Right now I am running a test server for them, and I have written a script to keep it running smoothly with minimal interference

## clothServer

**usage:** 

`bash clothServer -u`  or `--update` 
Checks to see if the latest release of Cloth matches the current version. If there is a newer version, send a warning to the server, and then shut down and download the latest version and relaunch. This is made to be run on a cronjob and check automatically



`bash clothServer -s` or `--start` 
Starts the server if it is not already running



`bash clothServer -r` or `--restart` 
Restarts the server gracefully



`bash clothServer -q`  or `--stop` 
Stops the server gracefully

