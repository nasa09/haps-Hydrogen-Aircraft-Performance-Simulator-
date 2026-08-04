"""
aircraft.py - AircraftState Class
"""
from fuel import Fuel
from constants import GRAVITY


class AircraftState:
    """
    Tracks and updates the dynamic physical state of the aircraft during flight.
    """
    def __init__(
        self,
        name: str,
        empty_mass: float,
        payload: float,
        fuel_mass: float,
        lift_to_drag: float,
        drag_multiplier: float,
        tank_mass: float,
        fuel: Fuel
    ):
        self.name = name
        self.empty_mass = empty_mass
        self.payload = payload
        self.fuel_mass = fuel_mass
        self.initial_fuel_mass = fuel_mass
        self.lift_to_drag = lift_to_drag
        self.drag_multiplier = drag_multiplier
        self.tank_mass = tank_mass
        self.fuel = fuel

    def total_mass(self) -> float:
        """Calculates dynamic total aircraft mass (kg)."""
        return self.empty_mass + self.payload + self.fuel_mass + self.tank_mass

    def weight(self) -> float:
        """Calculates dynamic total weight force (N)."""
        return self.total_mass() * GRAVITY

    def required_thrust(self) -> float:
        """
        Calculates required cruise thrust:
        Thrust = (Weight / (L/D)) * drag_multiplier
        """
        base_drag = self.weight() / self.lift_to_drag
        return base_drag * self.drag_multiplier

    def burn_fuel(self, mass_burned: float):
        """Reduces current fuel mass while enforcing zero lower bound."""
        self.fuel_mass = max(0.0, self.fuel_mass - mass_burned)
