from . import pin_error
import microcontroller

def pin3():
    return microcontroller.pin.PA03

def pin5():
    return microcontroller.pin.PA02

def pin6():
    return microcontroller.pin.PA05

def pin7():
    return microcontroller.pin.PB08

def pin8():
    return microcontroller.pin.PB09

def pin9():
    return microcontroller.pin.PA04

def pin10():
    return microcontroller.pin.PA06

def pin11():
    return microcontroller.pin.PA17

def pin12():
    return microcontroller.pin.PB23

def pin13():
    return microcontroller.pin.PB22

def pin14():
    return microcontroller.pin.PB17

def pin15():
    return microcontroller.pin.PB16

def pin16():
    return microcontroller.pin.PA14

def pin17():
    return microcontroller.pin.PA12

def pin18():
    return microcontroller.pin.PA13

def pin19():
    return microcontroller.pin.PA16

def pin20():
    return microcontroller.pin.PA18

def pin21():
    return microcontroller.pin.PA19

def pin22():
    return microcontroller.pin.PA20

def pin23():
    return microcontroller.pin.PA21

def pin24():
    return microcontroller.pin.PA22

def pin25():
    return microcontroller.pin.PA23

def init(scope):
    """Pull the pin definitions into the main module namespace"""
    for key in globals().keys():
        if key.startswith('pin'):
            scope[key] = globals()[key]