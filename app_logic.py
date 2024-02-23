# import Serial_communication

# def set_desired_temperature(temperature):
#     """Sends the desired temperature setting over serial."""
#     command = f"TEMP {temperature}"
#     Serial_communication.send_serial_data(command)

# def set_water_pressure(pressure):
#     """Sends the water pressure setting over serial."""
#     command = f"PRESSURE {pressure.upper()}"
#     Serial_communication.send_serial_data(command)

def fetch_current_temperature():
    """Requests the current temperature from the device."""
    Serial_communication.send_serial_data("GET TEMP")
    temp = Serial_communication.read_serial_data()
    if temp:
        try:
            # Assuming the temperature comes back in a format that needs parsing
            temperature = float(temp.split(':')[1].strip('°F'))
            return temperature
        except (ValueError, IndexError):
            print("Error parsing temperature")
            return None


# Import the SerialCommunication class from Serial_communication.py
from Serial_communication import SerialCommunication

# Create an instance of the SerialCommunication class
serial_comm = SerialCommunication()

def send_command_to_arduino(command):
    # This function sends a command to the Arduino
    # It's a wrapper around SerialCommunication's write_to_serial method
    serial_comm.write_to_serial(command)
# The rest of the code can now use the send_command_to_arduino function to send commands to the Arduino.