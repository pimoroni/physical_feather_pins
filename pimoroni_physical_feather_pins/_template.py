from . import pin_error
import microcontroller

def pin3():
    raise NotImplementedError

def pin5():
    raise NotImplementedError

def pin6():
    raise NotImplementedError

def pin7():
    raise NotImplementedError

def pin8():
    raise NotImplementedError

def pin9():
    raise NotImplementedError

def pin10():
    raise NotImplementedError

def pin11():
    raise NotImplementedError

def pin12():
    raise NotImplementedError

def pin13():
    raise NotImplementedError

def pin14():
    raise NotImplementedError

def pin15():
    raise NotImplementedError

def pin16():
    raise NotImplementedError

def pin17():
    raise NotImplementedError

def pin18():
    raise NotImplementedError

def pin19():
    raise NotImplementedError

def pin20():
    raise NotImplementedError

def pin21():
    raise NotImplementedError

def pin22():
    raise NotImplementedError

def pin23():
    raise NotImplementedError

def pin24():
    raise NotImplementedError

def pin25():
    raise NotImplementedError

def init(scope):
    """Pull the pin definitions into the main module namespace"""
    for key in globals().keys():
        if key.startswith('pin'):
            scope[key] = globals()[key]