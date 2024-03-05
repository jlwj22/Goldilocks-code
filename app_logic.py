# Import necessary libraries
import time
from Serial_communication import SerialCommunication

# Assuming SerialCommunication is correctly set up for serial communication
serial_comm = SerialCommunication()

def set_desired_temperature(temperature):
    """Sends the desired temperature setting over serial."""
    command = f"TEMP {temperature}"
    serial_comm.write_to_serial(command)

def set_water_pressure(pressure):
    """Sends the water pressure setting over serial."""
    command = f"PRESSURE {pressure.upper()}"
    serial_comm.write_to_serial(command)
    
def fetch_current_temperature():
    serial_comm.write_to_serial("GET TEMP")
    temp = serial_comm.read_serial_data()
    if temp:
        try:
            celcius = float(temp.split(':')[1].strip('°C'))
            
            fahrenheit = (celcius * 9/5) + 32
            return fahrenheit
        
        except ValueError:
            print("Error parsing temperature data.")
            return None
    else:
        print("No temperature data received.")
        return None
    
def start_shower():
    """Initiates the shower and prints 'shower start'."""
    print("Shower start")
    # Assuming there's a specific command to start the shower, if necessary
    # serial_comm.write_to_serial("START SHOWER")
    # Start the timer
    global start_time
    start_time = time.time()

def get_shower_duration():
    """Calculates and returns the shower's running time in seconds."""
    if 'start_time' in globals():
        return time.time() - start_time
    else:
        print("Shower has not started yet.")
        return 0 