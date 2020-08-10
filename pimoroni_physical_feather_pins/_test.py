# SPDX-FileCopyrightText: 2019 @Septolum, written for Pimoroni Ltd
# SPDX-FileCopyrightText: Copyright (c) 2020 Philip Howard, written for Pimoroni Ltd
#
# SPDX-License-Identifier: MIT
# pylint: disable=exec-used,unused-import,broad-except,line-too-long,missing-docstring
from time import sleep
import digitalio
import pimoroni_physical_feather_pins

for i in range(0, 30):
    try:
        exec(
            "pin{index} = digitalio.DigitalInOut(pimoroni_physical_feather_pins.pin{index}())".format(
                index=i
            )
        )
        exec("pin{}.switch_to_output()".format(i))
    except Exception as error:
        print(error)

while True:
    for i in range(1, 29):
        if "pin{}".format(i) in globals().keys():
            exec("pin{}.value = True".format(i))
            sleep(0.5)
            exec("pin{}.value = False".format(i))

    for i in range(1, 29):
        if "pin{}".format(i) in globals().keys():
            exec("pin{}.value = True".format(i))

    sleep(1)

    for i in range(1, 29):
        if "pin{}".format(i) in globals().keys():
            exec("pin{}.value = False".format(i))
