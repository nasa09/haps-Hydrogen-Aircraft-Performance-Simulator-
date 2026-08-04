"""
fuel.py - Fuel Class Definition with Literature-Based TSFC Values
"""

class Fuel:
    """
    Defines the thermophysical properties and baseline performance metrics of aviation fuel.
    """
    def __init__(self, name: str, density: float, lhv: float, tsfc: float):
        self.name = name
        self.density = density
        self.lhv = lhv
        self.tsfc = tsfc

    def calculate_volume(self, mass: float) -> float:
        """Calculates storage volume in cubic meters (m^3) for a given fuel mass."""
        return mass / self.density


JET_A = Fuel(
    name="Jet-A",
    density=800.0,
    lhv=42.8e6,
    tsfc=1.55e-5
)

LIQUID_HYDROGEN = Fuel(
    name="Liquid Hydrogen (LH2)",
    density=71.0,
    lhv=120.0e6,
    tsfc=5.80e-6
)
