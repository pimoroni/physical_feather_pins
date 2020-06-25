from . import pin_error
#import board
import microcontroller

def pin3():
#   This is 3V
    raise NotImplementedError

def pin5():
#    return board.A0
    return microcontroller.pin.PA04

def pin6():
#    return board.A1
    return microcontroller.pin.PA05

def pin7():
#    return board.A2
    return microcontroller.pin.PA06

def pin8():
#    return board.A3
    return microcontroller.pin.PA07

def pin9():
#    return board.A4
    return microcontroller.pin.PC04

def pin10():
#    return board.A5
    return microcontroller.pin.PC05

def pin11():
#    return board.SCK
    return microcontroller.pin.PB13

def pin12():
#    return board.MOSI
    return microcontroller.pin.PB15

def pin13():
#    return board.MISO
    return microcontroller.pin.PB14

def pin14():
#    return board.RX
    return microcontroller.pin.PB11

def pin15():
#    return board.TX
    return microcontroller.pin.PB10

def pin16():
#   This is B0
    raise NotImplementedError

def pin17():
#    return board.SDA
    return microcontroller.pin.PB07

def pin18():
#    return board.SCL
    return microcontroller.pin.PB06

def pin19():
#    return board.D5
    return microcontroller.pin.PC07

def pin20():
#    return board.D6
    return microcontroller.pin.PC06

def pin21():
#    return board.D9
    return microcontroller.pin.PB08

def pin22():
#    return board.D10
    return microcontroller.pin.PB09

def pin23():
#    return board.D11
    return microcontroller.pin.PC03

def pin24():
#    return board.D12
    return microcontroller.pin.PC02

def pin25():
#    return board.D13
    return microcontroller.pin.PC01

def init(scope):
    """Pull the pin definitions into the main module namespace"""
    for key in globals().keys():
        if key.startswith('pin'):
            scope[key] = globals()[key]