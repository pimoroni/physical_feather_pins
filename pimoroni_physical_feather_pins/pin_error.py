# SPDX-FileCopyrightText: 2019 @Septolum, written for Pimoroni Ltd
# SPDX-FileCopyrightText: Copyright (c) 2020 Philip Howard, written for Pimoroni Ltd
#
# SPDX-License-Identifier: MIT
# pylint: disable=missing-docstring


class PinNotAddressableError(Exception):
    def __init__(self, *args, **kwargs):
        default_message = "Pin is not addressable"

        if not (args or kwargs):
            args = (default_message,)

        super().__init__(*args, **kwargs)


class PinDoesNotExistError(Exception):
    def __init__(self, *args, **kwargs):
        default_message = "Pin does not exist"

        if not (args or kwargs):
            args = (default_message,)

        super().__init__(*args, **kwargs)
