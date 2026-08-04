"""
analysis.py - Simulation Reporting & Summary Output
"""

def print_summary(aircraft_name: str, telemetry: dict, initial_fuel_mass: float, initial_fuel_volume: float):
    """Outputs text summary of completed mission telemetry."""
    fuel_remaining = telemetry["fuel_mass"][-1]
    fuel_burned = initial_fuel_mass - fuel_remaining
    final_distance = telemetry["distance"][-1]
    final_fuel_volume = telemetry["fuel_volume"][-1]
    avg_thrust = sum(telemetry["thrust"]) / len(telemetry["thrust"])
    avg_fuel_flow = sum(telemetry["fuel_flow"]) / len(telemetry["fuel_flow"])

    print(f"\n==================================================")
    print(f" HAPS MISSION SUMMARY: {aircraft_name.upper()}")
    print(f"==================================================")
    print(f"Initial Required Tank Volume: {initial_fuel_volume:10.2f} m^3")
    print(f"Mission Distance Completed : {final_distance:10.2f} km")
    print(f"Total Fuel Burned : {fuel_burned:10.2f} kg")
    print(f"Fuel Remaining at Terminus : {fuel_remaining:10.2f} kg")
    print(f"Final Remaining Fuel Volume : {final_fuel_volume:10.2f} m^3")
    print(f"Average Thrust Force : {avg_thrust / 1000.0:10.2f} kN")
    print(f"Average Mass Flow Rate : {avg_fuel_flow:10.4f} kg/s")
    print(f"==================================================\n")
