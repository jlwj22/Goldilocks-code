import serial
import time

# Initialize the serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to be established

def send_serial_data(command):
    """Sends command to the serial device."""
    try:
        ser.write(command.encode())
    except serial.SerialException as e:
        print(f"Error sending data: {e}")

def read_serial_data():
    """Reads data from the serial device."""
    try:
        if ser.in_waiting > 0:
            return ser.readline().decode('utf-8').strip()
    except serial.SerialException as e:
        print(f"Error reading data: {e}")
        return None