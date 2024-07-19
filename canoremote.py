#!/usr/bin/env python3

import bleak, enum

DEVICE_NAME = "AutoShutter"

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

    global pairingChar
    pairingChar = None
    global eventChar
    eventChar = None

    async def initialize(self):
        #await self.connect(timeout=2)  #It used to be necessary, now it's not.
        print("Services:")
        for service in self.services:
            print(service) 
            for char in service.characteristics:
                print("  ",char)
                if char.uuid == UUIDCharacteristic.Pairing:
                    pairingChar = char
                if char.uuid == UUIDCharacteristic.Event:
                    eventChar = char
 
        print("Matched Characteristics:")
        print(pairingChar)
        print(eventChar) 
        data = bytearray([3, ] + list(map(ord, DEVICE_NAME)))
        print(data)
        await self.write_gatt_char(IntCharacteristic.Pairing, data)


    async def state(self, mode: Mode, button: Button = 0):
        data = bytearray([mode | button])
        await self.write_gatt_char(IntCharacteristic.Event, data)
