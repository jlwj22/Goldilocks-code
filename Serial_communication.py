import serial
import time

# Attempt to establish a serial connection
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    time.sleep(2)  # Give some time for the connection to be established
except serial.SerialException as e:
    print(f"Failed to establish serial connection: {e}")

def send_serial_data(command):
    """Sends command to the serial device."""
    try:
        ser.write(command.encode())
    except serial.SerialException as e:
        print(f"Error sending data: {e}")
    except NameError:
        print("Serial connection not established.")

def read_serial_data():
    """Reads data from the serial device."""
    try:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            return data
    except serial.SerialException as e:
        print(f"Error reading data: {e}")
    except NameError:
        print("Serial connection not established.")
    return None


# # Import necessary libraries
# import serial
# import time
# miwsomr

# # Attempt to establish a serial connection
# try:
#     ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#     time.sleep(2)  # Give some time for the connection to be established
# except serial.SerialException as e:
#     print(f"Failed to establish serial connection: {e}")

# def send_serial_data(command):
#     """Sends command to the serial device."""
#     try:
#         ser.write(command.encode())
#     except serial.SerialException as e:
#         print(f"Error sending data: {e}")
#     except NameError:
#         print("Serial connection not established.")

# def read_serial_data():
#     """Reads data from the serial device."""
#     try:
#         if ser.in_waiting > 0:
#             data = ser.readline().decode('utf-8').strip()
#             return data
#     except serial.SerialException as e:
#         print(f"Error reading data: {e}")
#     except NameError:
#         print("Serial connection not established.")
#     return None


# Import necessary libraries
import serial # pyserial library for s
import threading

class SerialCommunication:
    def __init__(self, port='/dev/ttyACM0', baudrate=9600):
        # Initialize the serial port with given parameters
        self.ser = serial.Serial(port, baudrate, timeout=1)
        # Start a daemon thread to continuously read from serial port
        self.read_thread = threading.Thread(target=self.read_from_serial)
        self.read_thread.daemon = True
        self.read_thread.start()
        # For now, print a message to the console
    def read_from_serial(self):
        # Continuously read data from the serial port
        while True:
            if self.ser.in_waiting > 0:
                data = self.ser.readline().decode().strip()
                # For now, print received data to the console
                # Ideally, this should update the GUI or call a callback
                print(data)

    def write_to_serial(self, command):
        # Send a command to the serial port
        self.ser.write(command.encode())
        # For now, print the sent command to the console
