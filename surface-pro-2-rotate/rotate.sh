#!/bin/sh

if [[ $1 = "install" ]]; 
    then
        sudo cp rotate.sh /usr/bin/;
        echo "Copied rotate.sh to /usr/bin/";
        sudo cp rotate.py /usr/bin/;
        echo "Copied rotate.py to /usr/bin/";
        sudo cp rotate.desktop /usr/share/applications/;
        echo "Copied rotate.desktop to /usr/share/applications/";
        exit;

elif pgrep -f "python /usr/bin/rotate.py" &> /dev/null; 
    then 
        pkill -9 -f rotate.py;
        notify-send "Screen rotation disabled"
        exit;
    else
        notify-send "Screen rotation enabled"
        python /usr/bin/rotate.py;
fi

