# Physical Feather Pins

A library to provide consistent pin access between different feathers.

<img src="./Feather Generic Pinout.svg">
(Modification of https://github.com/ATMakersOrg/HoldingArea/blob/master/FeatherTemplate.svg)

# Example

Original Code:
```python
import board, digitalio
pin16 = digitalio.DigitalInOut(board.D4) # works on M4, but not M0 or nRF52840
pin16.switch_to_output()
pin16.value = True
```

Using Physical Feather Pins:
```python
import pimoroni_physical_feather_pins, digitalio
pin16 = digitalio.DigitalInOut(pimoroni_physical_feather_pins.pin16())
# works on all feathers with a gpio there, gives a verbose error on M0 for example, note the parentheses
pin16.switch_to_output()
pin16.value = True
```

## Tested
* M4 Express
* M0 Express
* nRF52840 Express
* Feather STM32F405 Express
* Feather S2

## Untested but should work
* Adafruit Feather M0 Adalogger
* Adafruit Feather M0 Basic
* Adafruit Feather M0 RFM69
* Adafruit Feather M0 RFM9x
