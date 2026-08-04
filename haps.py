"""
haps.py - HAPS Simulation Engine (discrete time-stepping loop)
"""
from aircraft import AircraftState
from constants import CRUISE_SPEED, TIME_STEP, DEFAULT_RESERVE_PERCENT


class HAPS:
    """
    Discrete-time integration loop executing trajectory performance steps.
    """
    def __init__(self, aircraft_state: AircraftState, reserve_percent: float = DEFAULT_RESERVE_PERCENT):
        self.aircraft = aircraft_state
        self.reserve_limit = aircraft_state.initial_fuel_mass * reserve_percent
        self.dt = TIME_STEP

        self.telemetry = {
            "time": [],
            "distance": [],
            "mission_progress": [],
            "fuel_mass": [],
            "fuel_volume": [],
            "weight": [],
            "total_mass": [],
            "thrust": [],
            "fuel_flow": []
        }

    def run_mission(self, target_distance_m: float) -> dict:
        """Runs flight simulation until target distance or fuel reserve limit is hit."""
        time = 0.0
        distance = 0.0

        while distance < target_distance_m and self.aircraft.fuel_mass > self.reserve_limit:
            current_weight = self.aircraft.weight()
            current_total_mass = self.aircraft.total_mass()
            thrust = self.aircraft.required_thrust()
            fuel_flow = thrust * self.aircraft.fuel.tsfc
            fuel_burned = fuel_flow * self.dt
            fuel_vol = self.aircraft.fuel.calculate_volume(self.aircraft.fuel_mass)
            progress = (distance / target_distance_m) * 100.0

            self.telemetry["time"].append(time)
            self.telemetry["distance"].append(distance / 1000.0)
            self.telemetry["mission_progress"].append(progress)
            self.telemetry["fuel_mass"].append(self.aircraft.fuel_mass)
            self.telemetry["fuel_volume"].append(fuel_vol)
            self.telemetry["weight"].append(current_weight)
            self.telemetry["total_mass"].append(current_total_mass)
            self.telemetry["thrust"].append(thrust)
            self.telemetry["fuel_flow"].append(fuel_flow)

            self.aircraft.burn_fuel(fuel_burned)
            distance += CRUISE_SPEED * self.dt
            time += self.dt

        return self.telemetry
