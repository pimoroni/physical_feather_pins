from . import pin_error
import board


def pin3():    
    raise pin_error.PinNotAddressableError("3V3")

def pin5():
    return board.A0

def pin6():
    return board.A1

def pin7():
    return board.A2

def pin8():
    return board.A3

def pin9():
    return board.D24

def pin10():
    return board.D25

def pin11():
    return board.SCK

def pin12():
    return board.MISO

def pin13():
    return board.MOSI

def pin14():
    return board.RX

def pin15():
    return board.TX

def pin16():
    return board.D4

def pin17():
    return board.SDA

def pin18():
    return board.SCL

def pin19():
    return board.D5

def pin20():
    return board.D6

def pin21():
    return board.D9

def pin22():
    return board.D10

def pin23():
    return board.D11

def pin24():
    return board.D12

def pin25():
    return board.D13

def init(scope):
    """Pull the pin definitions into the main module namespace"""    
    for key in globals().keys():
        if key.startswith('pin'):
            scope[key] = globals()[key]