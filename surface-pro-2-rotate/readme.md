# Surface Pro 2 Auto Screen Rotate Script



Reads the accelerometer and flips the screen + reorients the touch screen when a new orientation is detected. Shell script + desktop file allow for it to be toggled from most start menus

## Requires:

python, xorg-xinput, iio-sensor-proxy, inotify-tools, xrandr

# Setup:

First you need to make sure that you `sudo systemctl start iio-sensor-proxy` before you try to run the script. it won't work without that.

Then, you have a few options for running it. you can either run `python rotate.py` directly, or you can run `./rotate.sh install` to copy the needed files to get the desktop icon toggle working.