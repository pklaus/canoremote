#!/usr/bin/env python3

import bleak, enum

DEVICE_NAME = "canoremote"

class Mode(enum.IntEnum):
    Immediate = 0b00001100
    Delay     = 0b00000100
    Movie     = 0b00001000

class Button(enum.IntEnum):
    Release = 0b10000000
    Focus   = 0b01000000
    Tele    = 0b00100000
    Wide    = 0b00010000

class IntCharacteristic(enum.IntEnum):
    Pairing = 0xf503
    Event   = 0xf505

class StrEnum(str, enum.Enum):
    pass

class UUIDCharacteristic(StrEnum):
    Pairing = "00050002-0000-1000-0000-d8492fffa821"
    Event   = "00050003-0000-1000-0000-d8492fffa821"

class CanoRemote(bleak.BleakClient):

    async def initialize(self):
        await self.connect()
        self.services = await self.get_services()
        data = bytearray([3, ] + list(map(ord, DEVICE_NAME)))
        await self.write_gatt_char(IntCharacteristic.Pairing, data, response=False)
        #await self.write_gatt_char("00050002-0000-1000-0000-d8492fffa821", data, response=False)


    async def state(self, mode: Mode, button: Button = 0):
        data = bytearray([mode | button])
        await self.write_gatt_char(IntCharacteristic.Event, data, response=False)
        #await self.write_gatt_char("00050003-0000-1000-0000-d8492fffa821", data, response=False)
