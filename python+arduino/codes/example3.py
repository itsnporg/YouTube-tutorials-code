import pyfirmata
import time

board = pyfirmata.Arduino("COM5")  #arduino is connected in my laptop port name COM5, you can find your from ARDUINO IDE

#how it works?

# board.digital[pin_number].write(1 or 0) 

board.digital[13].write(1) # it  high  voltage of pin number 13 (simply turn on pin 13)


board.digital[13].write(1) # it  low voltage of pin number 13 (simply turn of pin 13)
