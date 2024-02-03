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
