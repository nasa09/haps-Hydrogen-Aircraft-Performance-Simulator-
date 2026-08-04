"""
main.py - Primary Execution Pipeline for HAPS
"""
from fuel import JET_A, LIQUID_HYDROGEN
from aircraft import AircraftState
from haps import HAPS
from analysis import print_summary
from plots import generate_all_plots


def run():
    TARGET_DISTANCE_METERS = 4000 * 1000.0

    empty_mass = 42000.0
    payload = 13000.0
    initial_jeta_fuel = 14000.0
    baseline_ld = 17.5

    initial_lh2_fuel = initial_jeta_fuel * (JET_A.lhv / LIQUID_HYDROGEN.lhv)

    TANK_MASS_FACTOR = 0.25
    lh2_tank_mass = initial_lh2_fuel * TANK_MASS_FACTOR

    jeta_initial_vol = JET_A.calculate_volume(initial_jeta_fuel)
    lh2_initial_vol = LIQUID_HYDROGEN.calculate_volume(initial_lh2_fuel)

    ac_jeta = AircraftState(
        name="Jet-A Baseline",
        empty_mass=empty_mass,
        payload=payload,
        fuel_mass=initial_jeta_fuel,
        lift_to_drag=baseline_ld,
        drag_multiplier=1.00,
        tank_mass=0.0,
        fuel=JET_A
    )

    ac_lh2 = AircraftState(
        name="Liquid Hydrogen",
        empty_mass=empty_mass,
        payload=payload,
        fuel_mass=initial_lh2_fuel,
        lift_to_drag=baseline_ld,
        drag_multiplier=1.05,
        tank_mass=lh2_tank_mass,
        fuel=LIQUID_HYDROGEN
    )

    sim_jeta = HAPS(ac_jeta)
    telemetry_jeta = sim_jeta.run_mission(TARGET_DISTANCE_METERS)

    sim_lh2 = HAPS(ac_lh2)
    telemetry_lh2 = sim_lh2.run_mission(TARGET_DISTANCE_METERS)

    print_summary("Jet-A Baseline", telemetry_jeta, initial_jeta_fuel, jeta_initial_vol)
    print_summary("Liquid Hydrogen", telemetry_lh2, initial_lh2_fuel, lh2_initial_vol)

    generate_all_plots(telemetry_jeta, telemetry_lh2)


if __name__ == "__main__":
    run()
