import subprocess
import dbus
import os

def getPlaying():                                        # Gets info from Spotify
    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                         "/org/mpris/MediaPlayer2")
    spotify_properties = dbus.Interface(spotify_bus,
                                        "org.freedesktop.DBus.Properties")
    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

    return metadata

search = (str(getPlaying()['xesam:title']) + " " + str(getPlaying()['xesam:albumArtist']).replace("dbus.Array([dbus.String('","").replace("')], signature=dbus.Signature('s'), variant_level=1)",""))
#search = search.join([i if ord(i) < 128 else ' ' for i in search])
search = search.replace(" ","+")
#os.system('echo "https://youtube.com/watch?v=`youtube-dl --get-id --no-warnings "ytsearch:'+search+'"`" | discho -c general &')
#extension = os.system('~/.bin/keebie/scripts/yt.sh "' + search + '"')
extension = subprocess.check_output('~/.bin/keebie/scripts/yt.sh "' + search + '"', shell=True)
ext = extension.decode("utf-8")
os.system('echo https://youtube.com/watch?v=' + ext + ' | discho -c general &')