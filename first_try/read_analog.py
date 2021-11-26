from pyfirmata import Arduino
import pyfirmata
import time

port = "COM11" 
board = Arduino(port)

pin = board.get_pin('a:0:i"')

it = pyfirmata.util.Iterator(board)
it.start()

while True: 
    analog_val = pin.read()
    print(analog_val)
    time.sleep(0.1)