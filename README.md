# canoremote

Python code emulating the behaviour of the Canon BR-E1 Bluetooth LE remote control.
The code is based on [bleak][], a cross-platform async BLE library for Python.

Should work with any of these:

* Canon EOS R, 6D Mark II, 77D, 800D, 200D, M50, RP, M200, Ra, 850D, R5, R6 or
* Canon PowerShot G7 X Mark III, G5 X Mark II

Tested to work on a Canon EOS 200D.

## Camera Setup

* Open the menu
* Enter "Wireless communication settings"
* Enter "Bluetooth function"
* Set "Bluetooth function" to "Remote"
* Enter "Pairing" mode (if greyed out, click "Check/clear connection info" and "Clear settings" & "OK", first)
* When "Pairing in progress" appears, run this tool (eg `./test.py` with adjusted MAC address).
* The screen will show "Paired with: canoremote"
* Click OK
* Exit the menu
* Open the image capture settings (via Q button or in the main menu)
* Enter "Drive mode"
* Select "remote" (or "self-timer/remote")
* Change to movie mode
* Enter the menu
* Set "Remote control" to "Enable"

## Resources

* https://iandouglasscott.com/2017/09/04/reverse-engineering-the-canon-t7i-s-bluetooth-work-in-progress/
* https://iandouglasscott.com/2018/07/04/canon-dslr-bluetooth-remote-protocol/
* https://github.com/iebyt/cbremote
* https://github.com/ArthurFDLR/BR-M5
* https://github.com/ids1024/cannon-bluetooth-remote

[bleak]: https://bleak.readthedocs.io
