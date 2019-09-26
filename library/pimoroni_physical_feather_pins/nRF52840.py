from . import pin_error
import microcontroller

def pin3():
    return microcontroller.pin.P0_31

def pin5():
    return microcontroller.pin.P0_04

def pin6():
    return microcontroller.pin.P0_05

def pin7():
    return microcontroller.pin.P0_30

def pin8():
    return microcontroller.pin.P0_28

def pin9():
    return microcontroller.pin.P0_02

def pin10():
    return microcontroller.pin.P0_03

def pin11():
    return microcontroller.pin.P0_14

def pin12():
    return microcontroller.pin.P0_13

def pin13():
    return microcontroller.pin.P0_15

def pin14():
    return microcontroller.pin.P0_24

def pin15():
    return microcontroller.pin.P0_25

def pin16():
    return microcontroller.pin.P0_10

def pin17():
    return microcontroller.pin.P0_12

def pin18():
    return microcontroller.pin.P0_11

def pin19():
    return microcontroller.pin.P1_08

def pin20():
    return microcontroller.pin.P0_07

def pin21():
    return microcontroller.pin.P0_26

def pin22():
    return microcontroller.pin.P0_27

def pin23():
    return microcontroller.pin.P0_06

def pin24():
    return microcontroller.pin.P0_08

def pin25():
    return microcontroller.pin.P1_09

def init(scope):
    """Pull the pin definitions into the main module namespace"""
    for key in globals().keys():
        if key.startswith('pin'):
            scope[key] = globals()[key]