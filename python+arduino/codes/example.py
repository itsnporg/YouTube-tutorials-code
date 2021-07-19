import pyfirmata
import time

board = pyfirmata.Arduino("COM5")  #arduino is connected in my laptop port name COM5, you can find your from ARDUINO IDE

#blinking 10 time
for blink in range(10):
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)