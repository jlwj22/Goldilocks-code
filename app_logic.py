import Serial_communication

def set_desired_temperature(temperature):
    """Sends the desired temperature setting over serial."""
    command = f"TEMP {temperature}"
    Serial_communication.send_serial_data(command)

def set_water_pressure(pressure):
    """Sends the water pressure setting over serial."""
    command = f"PRESSURE {pressure.upper()}"
    Serial_communication.send_serial_data(command)

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
