import Serial_communication.py 

def set_desired_temperature(temperature):
    """Sends the desired temperature setting over serial."""
    command = f"TEMP {temperature}"
    serial_comm.send_serial_data(command)

def set_water_pressure(pressure):
    """Sends the water pressure setting over serial."""
    # Assuming "High" and "Low" are the accepted commands for pressure
    command = f"PRESSURE {pressure.upper()}"
    serial_comm.send_serial_data(command)

def fetch_current_temperature():
    """Requests the current temperature from the device."""
    serial_comm.send_serial_data("GET TEMP")
    # Assuming the device sends back a temperature reading
    temp = serial_comm.read_serial_data()
    if temp:
        try:
            # Assuming the temperature comes back in a format that needs parsing
            # For example, TEMP:75.2°F, we just return the numeric part
            temperature = float(temp.split(':')[1].strip('°F'))
            return temperature
        except (ValueError, IndexError):
            print("Error parsing temperature")
            return None
