import serial


class SerialComm:
    def __init__(self):
        self.com_port = "COM3"
        try:
            self.SERIAL = serial.Serial(self.com_port, baudrate=9600, timeout=1)
        except:
            print("COM port is not accessible!")

    def write_to_serial(self, value):
        try:
            self.SERIAL.write(value.encode)
        except:
            print("Serial Communication Error!")
