import random
import pandas as pd

class BuildingSimulator:
    def __init__(self):
        self.outdoor_temp = 35
        self.indoor_temp = 25
        self.humidity = 55
        self.co2 = 600
        self.occupancy = 20
        self.energy = 120

    def update(self):
        self.outdoor_temp += random.randint(-2, 2)
        self.indoor_temp += random.uniform(-0.5, 0.5)
        self.humidity += random.randint(-2, 2)
        self.co2 += random.randint(-20, 20)
        self.occupancy = max(0, self.occupancy + random.randint(-3, 3))
        self.energy += random.randint(-8, 8)

        return {
            "Outdoor Temp (°C)": round(self.outdoor_temp, 1),
            "Indoor Temp (°C)": round(self.indoor_temp, 1),
            "Humidity (%)": self.humidity,
            "CO₂ (ppm)": self.co2,
            "Occupancy": self.occupancy,
            "Energy (kWh)": self.energy
        }