import tkinter as tk
from tkinter import ttk
import app_logic  # Assuming app_logic handles the logic for button presses

class ShowerControlPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Shower Control Panel")
        
        # Initial desired temperature
        self.desired_temperature = 98.6

        # GUI Setup
        self.setup_ui()

    def setup_ui(self):
        # Current Temperature Display
        self.current_temp_label = ttk.Label(self.root, text="Current Temp: --°F")
        self.current_temp_label.grid(row=0, columnspan=2, pady=10)

        # Desired Temperature Control
        ttk.Button(self.root, text="-", command=self.decrease_temp).grid(row=1, column=0, sticky=tk.W+tk.E, padx=5)
        self.desired_temp_label = ttk.Label(self.root, text=f"Desired Temp: {self.desired_temperature}°F")
        self.desired_temp_label.grid(row=1, column=1)
        ttk.Button(self.root, text="+", command=self.increase_temp).grid(row=1, column=2, sticky=tk.W+tk.E, padx=5)

        # Water Pressure Control
        ttk.Button(self.root, text="High", command=lambda: app_logic.set_water_pressure("High")).grid(row=2, column=0, sticky=tk.W+tk.E, padx=5, pady=10)
        ttk.Button(self.root, text="Low", command=lambda: app_logic.set_water_pressure("Low")).grid(row=2, column=2, sticky=tk.W+tk.E, padx=5, pady=10)

    def increase_temp(self):
        self.desired_temperature += 1.0  # Increase temperature
        self.update_desired_temp_label()
        app_logic.set_desired_temperature(self.desired_temperature)

    def decrease_temp(self):
        self.desired_temperature -= 1.0  # Decrease temperature
        self.update_desired_temp_label()
        app_logic.set_desired_temperature(self.desired_temperature)

    def update_desired_temp_label(self):
        self.desired_temp_label.config(text=f"Desired Temp: {self.desired_temperature}°F")

    def update_current_temperature(self, temperature):
        self.current_temp_label.config(text=f"Current Temp: {temperature}°F")

# Main function to run the application
def run_app():
    root = tk.Tk()
    app = ShowerControlPanel(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
