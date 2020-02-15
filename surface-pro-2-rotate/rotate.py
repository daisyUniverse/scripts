from subprocess import Popen, PIPE
import os

def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line

if __name__ == "__main__":
    for path in run("monitor-sensor"):
        path = str(path).replace("b'","").replace("'","")
        if "normal" in path:
            os.system('xrandr --output eDP-1 --rotate normal && xinput set-prop "Atmel Atmel maXTouch Digitizer" --type=float "Coordinate Transformation Matrix" 0 0 0 0 0 0 0 0 0')
            print("Screen rotated to NORMAL")
        if "bottom-up" in path:
            os.system('xrandr --output eDP-1 --rotate inverted && xinput set-prop "Atmel Atmel maXTouch Digitizer" --type=float "Coordinate Transformation Matrix" -1 0 1 0 -1 1 0 0 1')
            print("Screen rotated UPSIDE DOWN")
        if "right-up" in path:
            os.system('xrandr --output eDP-1 --rotate right && xinput set-prop "Atmel Atmel maXTouch Digitizer" --type=float "Coordinate Transformation Matrix" 0 1 0 -1 0 1 0 0 1')
            print("Screen rotated RIGHT-UP")
        if "left-up" in path:
            os.system('xrandr --output eDP-1 --rotate left && xinput set-prop "Atmel Atmel maXTouch Digitizer" --type=float "Coordinate Transformation Matrix" 0 -1 1 1 0 0 0 0 1')
            print("Screen rotated LEFT-UP")