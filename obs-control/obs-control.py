import asyncio
import argparse
import subprocess
from obswsrc import OBSWS
from obswsrc.requests import SetCurrentSceneRequest
from obswsrc.types import Stream, StreamSettings
from obswsrc.requests import ResponseStatus, StartStreamingRequest, StopStreamingRequest

parser = argparse.ArgumentParser()
parser.add_argument("--scene", "-s", help="Change active OBS Scene")
parser.add_argument("--profile", "-p", help="Change active OBS Profile")
parser.add_argument("--port", help="Change web request port", default=4444)
parser.add_argument("--host", help="Change web request host", default='localhost')
parser.add_argument("--silent", "-q", help="Do not print confirmation in terminal or send notifications", action='store_false')

args = parser.parse_args()

async def main():
    async with OBSWS(args.host, args.port) as obsws:
        if args.scene:
            response = await obsws.require(SetCurrentSceneRequest(scene_name=args.scene))
            if args.silent:
                subprocess.Popen(["notify-send", "OBS Scene changed to " + args.scene], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
                print ("Scene changed to " + args.scene)
        if args.profile:
            response = await obsws.require(SetCurrentProfileRequest(profile_name=args.profile))
            if args.silent:
                subprocess.Popen(["notify-send", "OBS Profile changed to " + args.scene], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
                print ("Profile changed to " + args.scene)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()