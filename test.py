#!/usr/bin/env python

import asyncio
from canoremote import CanoRemote, Button, Mode

MODE=Mode.Immediate
#MODE=Mode.Delay
#MODE=Mode.Movie

async def run():
    # Enter the MAC address of your camera here. You can found at Wireless communication settings on your camera.
    async with CanoRemote("XX:XX:XX:XX:XX:XX", timeout=5) as cr:

        await cr.initialize()
        print("Initialized") 

        # If you need focus. May be you select manuel focus then there's no need for that.
        print("Focus Start") 
        # Press the "focus" button for 600ms
        await cr.state(MODE, Button.Focus)
        await asyncio.sleep(0.6)
        await cr.state(MODE)
        print("Focus End") 

        print("sleep Start")
        # wait for 4 seconds
        await asyncio.sleep(4)

        # Press the "shutter" button for 500ms 
        print("Shutter Start")
        await cr.state(MODE, Button.Release)
        await asyncio.sleep(0.5)
        await cr.state(MODE)
        print("Shutter End")
        await asyncio.sleep(0.5)

        # Press the "shutter" button for 500ms 
        print("Shutter Start")
        await cr.state(MODE, Button.Release)
        await asyncio.sleep(0.5)
        await cr.state(MODE)
        print("Shutter End")

        # wait another second
        await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
