import pimoroni_physical_feather_pins, digitalio
from time import sleep

for i in range(0,30):
    try:
        exec("pin{} = digitalio.DigitalInOut(pimoroni_physical_feather_pins.pin{}())".format(i,i))
        exec("pin{}.switch_to_output()".format(i))
    except Exception as Error:
        print(Error)

while True:
    for i in range(1,29):
        if "pin{}".format(i) in globals().keys():
            exec("pin{}.value = True".format(i))
            sleep(0.5)
            exec("pin{}.value = False".format(i))
    
    for i in range(1,29):
        if "pin{}".format(i) in globals().keys():
            exec("pin{}.value = True".format(i))

    sleep(1)

    for i in range(1,29):
        if "pin{}".format(i) in globals().keys():
            exec("pin{}.value = False".format(i))
