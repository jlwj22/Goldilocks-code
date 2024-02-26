import serial
import threading
import logging
import time

# Configure logging
logging.basicConfig(filename='serial_errors.log', level=logging.WARNING)

class SerialCommunication:
    def __init__(self, port='/dev/ttyACM0', baudrate=9600):
        self.ser = None
        self.port = port
        self.baudrate = baudrate
        self.read_thread = None
        self.data_received_callback = None
        self.is_connected = False  # Flag to check connection status
        self.keep_reading = True  # Flag to control the read loop

    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
            self.is_connected = True
            self.keep_reading = True
            self.read_thread = threading.Thread(target=self.read_from_serial)
            self.read_thread.daemon = True
            self.read_thread.start()
            logging.info("Serial connection established.")
        except serial.SerialException as e:
            logging.error(f"Serial connection error: {e}")
            self.is_connected = False

    def read_from_serial(self):
        while self.keep_reading:
            try:
                if self.ser.in_waiting > 0:
                    data = self.ser.readline().decode().strip()
                    if self.data_received_callback:
                        self.data_received_callback(data)
            except serial.SerialException as e:
                logging.error(f"Error reading serial data: {e}")
                self.keep_reading = False  # Consider stopping on serial error
            time.sleep(0.1)

    def write_to_serial(self, command):
        if not self.is_connected:
            logging.warning("Attempted to write to serial without an active connection.")
            return
        try:
            self.ser.write(command.encode())  
            logging.info(f"Command sent: {command}")
        except serial.SerialException as e:
            logging.error(f"Error sending serial data: {e}")

    def set_data_received_callback(self, callback_function):
        self.data_received_callback = callback_function 

    def disconnect(self):
        self.keep_reading = False  # Signal the read thread to stop
        if self.read_thread.is_alive():
            self.read_thread.join()
        if self.ser:
            self.ser.close()
        self.is_connected = False
        logging.info("Serial connection closed.")
