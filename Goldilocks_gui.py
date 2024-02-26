import tkinter as tk
from tkinter import ttk
import time

# Assuming app_logic handles the logic for button presses
import app_logic

class ShowerControlPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Shower Control Panel")
        
        self.desired_temperature = 98.6  # Initial desired temperature
        self.pressure_high = False  # Initial pressure state
        self.start_time = None  # Track start time of shower
        self.timer_running = False

        self.setup_ui()

    def setup_ui(self):
        # Configuration of the grid layout
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        # Current Temperature Display
        self.current_temp_label = ttk.Label(self.root, text="Current Temp: --°F")
        self.current_temp_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Desired Temperature Control
        ttk.Button(self.root, text="-", command=self.decrease_temp).grid(row=1, column=0, sticky=tk.W+tk.E, padx=5)
        self.desired_temp_label = ttk.Label(self.root, text=f"Desired Temp: {self.desired_temperature}°F")
        self.desired_temp_label.grid(row=1, column=1)
        ttk.Button(self.root, text="+", command=self.increase_temp).grid(row=1, column=2, sticky=tk.W+tk.E, padx=5)

        # Water Pressure Control
        self.pressure_button = ttk.Button(self.root, text="Toggle Pressure", command=self.toggle_pressure)
        self.pressure_button.grid(row=2, column=0, columnspan=3, pady=10, sticky=tk.W+tk.E)

        # Shower Start Button
        ttk.Button(self.root, text="Start Shower", command=self.start_shower).grid(row=3, column=0, columnspan=3, sticky=tk.W+tk.E, pady=10)

        # Timer Display
        self.timer_label = ttk.Label(self.root, text="Shower Time: 0s")
        self.timer_label.grid(row=4, column=0, columnspan=3, pady=10)

        # Stop Shower Button
        self.stop_button = ttk.Button(self.root, text="Stop Shower", command=self.stop_shower)
        self.stop_button.grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, pady=10)

    def toggle_pressure(self):
        self.pressure_high = not self.pressure_high
        pressure_text = "High" if self.pressure_high else "Low"
        print(self.pressure_high)
        self.pressure_button.config(text=f"Pressure: {pressure_text}")
        app_logic.set_water_pressure(pressure_text)

    def start_shower(self):
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()

    def stop_shower(self):
        self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Shower Time: {elapsed_time}s")
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Shower Time: 0s")

    def increase_temp(self):
        self.desired_temperature += 1.0
        self.update_desired_temp_label()

    def decrease_temp(self):
        self.desired_temperature -= 1.0
        self.update_desired_temp_label()

    def update_desired_temp_label(self):
        self.desired_temp_label.config(text=f"Desired Temp: {self.desired_temperature}°F")

def run_app():
    root = tk.Tk()
    app = ShowerControlPanel(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
