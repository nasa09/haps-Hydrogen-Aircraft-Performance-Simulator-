"""
plots.py - Single-Figure PNG Export to outputs/ Directory
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTPUT_DIR = "outputs"


def _ensure_output_folder():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def plot_total_mass(t_jeta: dict, t_lh2: dict):
    plt.figure(figsize=(8, 5))
    plt.plot(t_jeta["distance"], t_jeta["total_mass"], 'b-', label="Jet-A Aircraft", linewidth=2)
    plt.plot(t_lh2["distance"], t_lh2["total_mass"], 'r--', label="LH2 Aircraft", linewidth=2)
    plt.title("Figure 1: Total Aircraft Mass vs. Distance")
    plt.xlabel("Distance Traveled (km)")
    plt.ylabel("Total Mass (kg)")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "figure1.png"), dpi=300)
    plt.close()


def plot_fuel_mass(t_jeta: dict, t_lh2: dict):
    plt.figure(figsize=(8, 5))
    plt.plot(t_jeta["distance"], t_jeta["fuel_mass"], 'b-', label="Jet-A Fuel", linewidth=2)
    plt.plot(t_lh2["distance"], t_lh2["fuel_mass"], 'r--', label="LH2 Fuel", linewidth=2)
    plt.title("Figure 2: Fuel Mass Remaining vs. Distance")
    plt.xlabel("Distance Traveled (km)")
    plt.ylabel("Fuel Mass Remaining (kg)")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "figure2.png"), dpi=300)
    plt.close()


def plot_fuel_volume(t_jeta: dict, t_lh2: dict):
    plt.figure(figsize=(8, 5))
    plt.plot(t_jeta["distance"], t_jeta["fuel_volume"], 'b-', label="Jet-A Fuel Volume", linewidth=2)
    plt.plot(t_lh2["distance"], t_lh2["fuel_volume"], 'r--', label="LH2 Fuel Volume", linewidth=2)
    plt.title("Figure 3: Required Storage Tank Volume vs. Distance")
    plt.xlabel("Distance Traveled (km)")
    plt.ylabel("Liquid Volume (m^3)")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "figure3.png"), dpi=300)
    plt.close()


def plot_thrust(t_jeta: dict, t_lh2: dict):
    plt.figure(figsize=(8, 5))
    plt.plot(t_jeta["distance"], [t / 1000.0 for t in t_jeta["thrust"]], 'b-', label="Jet-A Thrust", linewidth=2)
    plt.plot(t_lh2["distance"], [t / 1000.0 for t in t_lh2["thrust"]], 'r--', label="LH2 Thrust", linewidth=2)
    plt.title("Figure 4: Required Cruise Thrust vs. Distance")
    plt.xlabel("Distance Traveled (km)")
    plt.ylabel("Required Thrust (kN)")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "figure4.png"), dpi=300)
    plt.close()


def plot_fuel_flow(t_jeta: dict, t_lh2: dict):
    plt.figure(figsize=(8, 5))
    plt.plot(t_jeta["distance"], t_jeta["fuel_flow"], 'b-', label="Jet-A Mass Flow", linewidth=2)
    plt.plot(t_lh2["distance"], t_lh2["fuel_flow"], 'r--', label="LH2 Mass Flow", linewidth=2)
    plt.title("Figure 5: Instantaneous Fuel Flow Rate vs. Distance")
    plt.xlabel("Distance Traveled (km)")
    plt.ylabel("Fuel Flow Rate (kg/s)")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "figure5.png"), dpi=300)
    plt.close()


def generate_all_plots(t_jeta: dict, t_lh2: dict):
    _ensure_output_folder()
    plot_total_mass(t_jeta, t_lh2)
    plot_fuel_mass(t_jeta, t_lh2)
    plot_fuel_volume(t_jeta, t_lh2)
    plot_thrust(t_jeta, t_lh2)
    plot_fuel_flow(t_jeta, t_lh2)
    print("Exported output plots to outputs/ directory (figure1.png - figure5.png)")
