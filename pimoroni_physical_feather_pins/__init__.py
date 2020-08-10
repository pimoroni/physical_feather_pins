# SPDX-FileCopyrightText: 2019 @Septolum, written for Pimoroni Ltd
# SPDX-FileCopyrightText: Copyright (c) 2020 Philip Howard, written for Pimoroni Ltd
#
# SPDX-License-Identifier: MIT
"""
`pimoroni_physical_feather_pins`
================================================================================

A library to provide consistent pin access between different feathers.

* Author(s): Philip Howard

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""
# pylint: disable=missing-docstring

import os as _os
from . import pin_error

# from . import m4, m0, nRF52840
# from . import _template


__version__ = "0.0.0-auto.0"
__repo__ = (
    "https://github.com/pimoroni/Pimoroni_CircuitPython_physical_feather_pins.git"
)


def __getattr__(name):
    raise pin_error.PinDoesNotExistError("Pin '%s' does not exist" % (name))


# region Consistent Pins


def pin1():
    raise pin_error.PinNotAddressableError(
        "Pin 1 is not addressable. To reset the board, use 'microcontroller.reset'"
    )


def pin2():
    raise pin_error.PinNotAddressableError("Pin 2 is not addressable.")


def pin4():
    raise pin_error.PinNotAddressableError("Pin 4 is not addressable.")


def pin26():
    raise pin_error.PinNotAddressableError("Pin 26 is not addressable.")


def pin27():
    raise pin_error.PinNotAddressableError("Pin 27 is not addressable.")


def pin28():
    raise pin_error.PinNotAddressableError("Pin 28 is not addressable.")


# endregion Consistent Pins

_MACHINE_NAMES = {
    "Adafruit Feather M4 Express with samd51j19": "m4",
    "Adafruit Feather M0 Express with samd21g18": "m0",
    "Adafruit Feather nRF52840 Express with nRF52840": "nRF52840",
    "Adafruit Feather M0 Adalogger with samd21g18": "m0",
    "Adafruit Feather M0 Basic with samd21g18": "m0",
    "Adafruit Feather M0 RFM69 with samd21g18": "m0",
    "Adafruit Feather M0 RFM9x with samd21g18": "m0",
    "x86_64": "m4",  # Hack for documentation to build until we can - potentially - spoof machine name?
}

_MACHINE = _os.uname().machine

# m4.init(globals())

try:
    module = __import__(
        _MACHINE_NAMES[_MACHINE], globals(), locals(), [None], 1
    )  # pylint: disable=invalid-name
    module.init(globals())
except KeyError:
    raise NotImplementedError("Sorry, '{}' is not supported currently".format(_MACHINE))
