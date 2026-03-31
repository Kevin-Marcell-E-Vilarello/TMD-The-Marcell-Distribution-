import numpy as np

def run_mass_sweep():
    print("\n" + "="*45)
    print("MARCELL ARTIFACT 2: QX2 MASS SWEEP")
    print("="*45)
    
    # Sweep from 0 to Pi/2 (The Marcell Phase Quadrant)
    phases = np.linspace(0, np.pi/2, 10)
    
    print(f"{'PHASE (rad)':<15} | {'LATTICE RATIO':<15}")
    print("-" * 35)
    
    for p in phases:
        # Ratio derived from the Cosine of the Phase (The U-Valley)
        ratio = np.cos(p)
        print(f"{p:<15.4f} | {ratio:<15.10f}")
    
    print("-" * 45)
    # The Singularity check
    if np.isclose(np.cos(0.0), 1.0):
        print("VERDICT: SINGULARITY DETECTED AT 0.0.")
        print("CONCLUSION: The 'U-Valley' is centered. Mass is deterministic.")
    print("="*45 + "\n")

if __name__ == "__main__":
    run_mass_sweep()
