# import tkinter as tk
# from tkinter import ttk
# import app_logic  # Assuming app_logic handles the logic for button presses

# class ShowerControlPanel:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Shower Control Panel")
        
#         # Initial desired temperature
#         self.desired_temperature = 98.6

#         # GUI Setup
#         self.setup_ui()

#     def setup_ui(self):
#         # Current Temperature Display
#         self.current_temp_label = ttk.Label(self.root, text="Current Temp: --°F")
#         self.current_temp_label.grid(row=0, columnspan=2, pady=10)

#         # Desired Temperature Control
#         ttk.Button(self.root, text="-", command=self.decrease_temp).grid(row=1, column=0, sticky=tk.W+tk.E, padx=5)
#         self.desired_temp_label = ttk.Label(self.root, text=f"Desired Temp: {self.desired_temperature}°F")
#         self.desired_temp_label.grid(row=1, column=1)
#         ttk.Button(self.root, text="+", command=self.increase_temp).grid(row=1, column=2, sticky=tk.W+tk.E, padx=5)

#         # Water Pressure Control
#         ttk.Button(self.root, text="High", command=lambda: app_logic.set_water_pressure("High")).grid(row=2, column=0, sticky=tk.W+tk.E, padx=5, pady=10)
#         ttk.Button(self.root, text="Low", command=lambda: app_logic.set_water_pressure("Low")).grid(row=2, column=2, sticky=tk.W+tk.E, padx=5, pady=10)

#     def increase_temp(self):
#         self.desired_temperature += 1.0  # Increase temperature
#         self.update_desired_temp_label()
#         app_logic.set_desired_temperature(self.desired_temperature)

#     def decrease_temp(self):
#         self.desired_temperature -= 1.0  # Decrease temperature
#         self.update_desired_temp_label()
#         app_logic.set_desired_temperature(self.desired_temperature)

#     def update_desired_temp_label(self):
#         self.desired_temp_label.config(text=f"Desired Temp: {self.desired_temperature}°F")

#     def update_current_temperature(self, temperature):
#         self.current_temp_label.config(text=f"Current Temp: {temperature}°F")

# # Main function to run the application
# def run_app():
#     root = tk.Tk()
#     app = ShowerControlPanel(root)
#     root.mainloop()

# if __name__ == "__main__":
#     run_app()

# Import necessary libraries
import tkinter as tk
# Import the send_command_to_arduino function from app_logic.py
from app_logic import send_command_to_arduino

# Function called when the button is pressed
def on_button_press():
    # Example command to send
    send_command_to_arduino("H")

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Serial Communication Example")

# Create a button widget
# When pressed, it calls the on_button_press function
button = tk.Button(root, text="Send Command", command=on_button_press)
button.pack()

# Start the Tkinter event loop
root.mainloop()
# The button will send a command to the Arduino when pressed. The command is sent using the send_command_to_arduino function, which is a wrapper around the SerialCommunication class's write_to_serial method. The SerialCommunication class is responsible for handling the serial communication with the Arduino. The Tkinter GUI is set up to call the on_button_press function when the button is pressed. This function sends a command to the Arduino. The Tkinter event loop is started to handle user interactions with the GUI.