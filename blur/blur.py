import os
import sys
import subprocess
from pathlib import Path

pipe = sys.stdin.read()
home = str(Path.home())
if pipe:
    window_class = pipe.replace('"','').strip()
    opacity = hex(int(sys.argv[(len(sys.argv) - 1)]))
else:
    window_class = str(sys.argv[(len(sys.argv) - 2)])
    opacity = hex(int(sys.argv[(len(sys.argv) - 1)]))

args = '( if \n( contains ( window_class ) "' + window_class + '" )\n( begin\n( spawn_async (str "xprop -id " (window_xid) " -f _KDE_NET_WM_BLUR_BEHIND_REGION 32c -set _KDE_NET_WM_BLUR_BEHIND_REGION 0 ") ) \n( spawn_async (str "xprop -id " (window_xid) " -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY ' + opacity + 'ffffff") ) \n) \n)'

f = open(home + '/.devilspie/' + window_class + '.ds','w+')
f.write(args)
f.close
