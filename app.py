from ast import Str
import serial
from time import sleep
#Can be Downloaded from this Link
#https://pypi.python.org/pypi/pyserial

#Global Variables
ser = 0

#Function to Initialize the Serial Port
def init_serial():
    global ser          #Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM7'   #COM Port Name Start from 0
    #ser.port = '/dev/ttyUSB0' #If Using Linux
    #Specify the TimeOut in seconds, so that SerialPort
    #Doesn't hangs
    ser.timeout = 10
    ser.open()          #Opens SerialPort
    # print port open or closed
    if ser.isOpen():
        print('Open: ' + ser.portstr)
#Function Ends Here

#Call the Serial Initilization Function, Main Program Starts from here
init_serial()
while 1:    
    bytes = ser.readline()  #Read from Serial Port
    bytes=str(bytes)
    print(bytes)
    if "AT" in bytes:
        if "AT+HTTPACTION=0" in bytes:
            sleep(0.03)
            ser.write(b'SUCESS\n')
            print("sending response for the http request")
        else:
            sleep(0.03)
            ser.write(b'OK\n')
            print("sending response through serial")
