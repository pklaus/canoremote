#!/usr/bin/env python

import asyncio
from canoremote import CanoRemote, Button, Mode

MODE=Mode.Immediate
#MODE=Mode.Delay
#MODE=Mode.Movie

async def run():
    async with CanoRemote("DC:EF:CA:AC:57:33", timeout=5) as cr:

        await cr.initialize()

        # Press the "focus" button for 600ms
        await cr.state(MODE, Button.Focus)
        await asyncio.sleep(0.6)
        await cr.state(MODE)

        # wait for 4 seconds
        await asyncio.sleep(4)

        # Press the "shutter" button for 500ms
        await cr.state(MODE, Button.Release)
        await asyncio.sleep(0.5)
        await cr.state(MODE)

        # wait another second
        await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
