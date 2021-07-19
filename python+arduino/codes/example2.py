import pyfirmata
board = pyfirmata.Arduino("COM5")  #arduino is connected in my laptop port name COM5, you can find your from ARDUINO IDE

#Taking input from user
while True:
    digital_signal = int(input("Input (1 for High and 0 For low): "))
    board.digital[13].write(digital_signal)