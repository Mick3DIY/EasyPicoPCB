# EasyPicoPCB with JoystickXL

A simple PCB with Raspberry Pi Pico, 3 LEDs, 3 push buttons, 3 potentiometers and a code example in **CircuitPython** with **JoystickXL**. 

This is a updated version of the original code project : [https://github.com/Mick3DIY/EasyPicoPCB](https://github.com/Mick3DIY/EasyPicoPCB)

First of all, read carefully these chapters from JoystickXL documentation : Requirements, Limitations, Host OS/Software Compatibility in [https://circuitpython-joystickxl.readthedocs.io/en/latest/](https://circuitpython-joystickxl.readthedocs.io/en/latest/)

Then jump to the 'Getting Started' section : [https://circuitpython-joystickxl.readthedocs.io/en/latest/start.html](https://circuitpython-joystickxl.readthedocs.io/en/latest/start.html)

After verifying compatibility and checking all axes and buttons, adapt the file *boot.py* with this code :

```python
""" EasyPicoPCB and JoystickXL standard boot.py."""

import usb_hid  # type: ignore (this is a CircuitPython built-in)
from joystick_xl.hid import create_joystick

# This will enable all of the standard CircuitPython USB HID devices along with a
# USB HID joystick.
usb_hid.enable(
    (
        usb_hid.Device.KEYBOARD,
        usb_hid.Device.MOUSE,
        usb_hid.Device.CONSUMER_CONTROL,
        create_joystick(axes=3, buttons=3, hats=0),
    )
)
```

**Don't forget to reboot the Raspberry Pi Pico after create this file !**

Then create a new file *code.py* in the Pico board with Thonny IDE with the code below :

![](assets/EasyPicoPCB_joystickXL_directories.png)

[EasyPicoPCB_JoystickXL.py](EasyPicoPCB_JoystickXL.py)

Finally run this code to see some values :

![](assets/EasyPicoPCB_joystickXL_thonny.png)

Testing the board in Windows 11 with CircuitPython HID :

![](assets/EasyPicoPCB_joystickXL_w11.png)

Or with a browser in the website : [https://hardwaretester.com/gamepad](https://hardwaretester.com/gamepad)

![](assets/EasyPicoPCB_joystickXL_gamepad.png)

Happy coding & have fun ! :partying_face:
