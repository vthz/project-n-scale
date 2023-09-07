import keyboard
import serial
import time
from CommandsFile import command_list_v2 as command_list
import customtkinter

COM_PORT = "COM3"

SERIAL = serial.Serial(COM_PORT, baudrate=9600, timeout=1)
COMMAND_SET = set(item[0] for item in command_list)
time.sleep(0)  # Wait for 3 seconds

loop_flag = True
freestyle_mode = True

while loop_flag and not freestyle_mode:
    user_command = input("=->")

    if user_command == "X":
        loop_flag = False
        break
    elif user_command.lower() == "help":
        for single_command in command_list:
            print(single_command)
    elif user_command is not None and user_command in COMMAND_SET:
        print("=->" + user_command)
        SERIAL.write(user_command.encode())
        arduino_response = SERIAL.readline().decode().split("\r\n")
        print(arduino_response)
    else:
        print("Invalid Command!")

while loop_flag and freestyle_mode:
    key = keyboard.read_key()
    if key:
        print(key)
        if key.upper() == "X":
            loop_flag = False
            break
        elif key.upper() in COMMAND_SET:
            SERIAL.write(key.encode)
            pass
        else:
            print("Invalid Key")
