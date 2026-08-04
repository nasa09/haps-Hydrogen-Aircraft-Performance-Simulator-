# HAPS — Hydrogen Aircraft Performance Simulator

HAPS is a Python simulation that compares liquid hydrogen (LH2) and conventional Jet-A fuel on the same mid-range commercial aircraft during steady, level cruise flight. Using standard aircraft performance equations, it steps through the flight one second at a time, updating aircraft weight, required thrust, fuel burned, and distance traveled, while keeping every other flight condition identical between the two fuels, so any difference in the results comes from the fuel properties themselves.

**Full research write-up:** [https://drive.google.com/file/d/1iAIO0hnbRmY7Vz6_UeL0N7BuGFp-ycnu/view?usp=sharing]

## Why this exists

Liquid hydrogen carries almost three times the energy per kilogram of Jet-A, but it's roughly eleven times less dense, and it has to be stored as a cryogenic liquid at about 20 K (-253°C). This project models that trade-off directly: how much fuel *mass* does an aircraft save by using hydrogen, and how much fuel *volume* does it cost?

## How it works

At every one-second time step, HAPS:
1. Calculates the aircraft's current total weight
2. Calculates the thrust required to maintain cruise (from the lift-to-drag ratio)
3. Calculates fuel burned that second (from Thrust Specific Fuel Consumption)
4. Updates the aircraft's remaining fuel mass
5. Advances the aircraft's distance traveled
6. Logs everything for plotting

This repeats until the aircraft either completes the target mission distance or its fuel drops to a 5% reserve.

## Project structure

```
HAPS/
├── main.py          # Entry point — sets up both aircraft and runs the simulation
├── constants.py      # Physical constants (gravity, cruise speed, time step)
├── fuel.py            # Fuel class + Jet-A / liquid hydrogen property presets
├── aircraft.py       # AircraftState class — tracks weight, thrust, fuel burn
├── haps.py           # The simulation loop itself
├── analysis.py        # Console summary output
├── plots.py            # Generates the 5 comparison figures
├── outputs/            # Generated PNG figures land here
└── requirements.txt
```

## Running it

```bash
git clone https://github.com/<your-username>/HAPS.git
cd HAPS
pip install -r requirements.txt
python main.py
```

No configuration needed. It runs both fuels on a 4,000 km mission and prints a summary for each, then saves five comparison figures to `outputs/`.

## Sample output

```
==================================================
 HAPS MISSION SUMMARY: JET-A BASELINE
==================================================
Initial Required Tank Volume:      17.50 m^3
Mission Distance Completed :     3999.93 km
Total Fuel Burned :               9676.95 kg
Fuel Remaining at Terminus :      4323.05 kg
Final Remaining Fuel Volume :        5.40 m^3
Average Thrust Force :              35.90 kN
Average Mass Flow Rate :            0.5564 kg/s
==================================================

==================================================
 HAPS MISSION SUMMARY: LIQUID HYDROGEN
==================================================
Initial Required Tank Volume:      70.33 m^3
Mission Distance Completed :     3999.93 km
Total Fuel Burned :               3530.14 kg
Fuel Remaining at Terminus :      1463.19 kg
Final Remaining Fuel Volume :       20.61 m^3
Average Thrust Force :              35.00 kN
Average Mass Flow Rate :            0.2030 kg/s
==================================================
```

## Key takeaway

Even though the hydrogen aircraft takes off about 7,750 kg lighter (thanks to hydrogen's much higher specific energy), it needs roughly four times more tank volume than the Jet-A aircraft, this project attempts to measure that.

## Model assumptions & limitations

- Only the cruise phase of flight is modeled (no takeoff, climb, descent, or landing)
- Cruise altitude, airspeed, and lift-to-drag ratio are held constant
- Standard atmosphere, no wind
- Cryogenic tank mass is estimated as a fixed percentage of fuel mass, not from a full structural design
- Hydrogen boil-off and detailed combustion chemistry are not modeled

See the full paper (linked above) for input sources, the underlying equations, and a full discussion.
