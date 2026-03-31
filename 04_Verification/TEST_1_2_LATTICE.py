import numpy as np

def run_lattice_skeleton():
    # THE RECTIFIED RAILS (Applying the 0.5 Sync)
    B3_FLOW = 2.220446049250313e-16 * 0.5
    B4_LOCK = 1.0842566190763042e-16
    
    # Calculate the Structural Mean (The "Mid-Rail")
    skeleton_mean = (B3_FLOW + B4_LOCK) / 2
    
    # Calculate the Tension Gap
    gap = B3_FLOW - B4_LOCK
    
    print("\n" + "="*45)
    print("MARCELL ARTIFACT 4: TEST 1_2 LATTICE")
    print("="*45)
    print(f"B3 FLOW (ROOT):    {B3_FLOW:.20e}")
    print(f"B4 LOCK (LEAF):    {B4_LOCK:.20e}")
    print(f"STRUCTURAL MEAN:   {skeleton_mean:.20e}")
    print(f"SKELETON GAP:      {gap:.20e}")
    print("-"*45)
    
    if gap > 0:
        print("VERDICT: LATTICE SKELETON SECURED.")
        print("CONCLUSION: The parallel rails are anchored in the buffer.")
    else:
        print("VERDICT: SKELETON COLLAPSE.")
    print("="*45 + "\n")

if __name__ == "__main__":
    run_lattice_skeleton()
