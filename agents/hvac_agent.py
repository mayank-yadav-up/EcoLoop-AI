class HVACAgent:

    def decide(self, sensor):

        temp = sensor["Indoor Temp (°C)"]
        people = sensor["Occupancy"]

        if temp > 26 and people > 10:
            action = "Increase Cooling"
            saving = 8

        elif temp < 22:
            action = "Reduce Cooling"
            saving = 12

        else:
            action = "Maintain Current Setting"
            saving = 5

        return {
            "Action": action,
            "Estimated Saving (%)": saving
        }