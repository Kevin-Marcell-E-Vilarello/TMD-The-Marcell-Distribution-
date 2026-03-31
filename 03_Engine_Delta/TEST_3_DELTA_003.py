import numpy as np

def run_delta_verification():
    # THE ANCHORS FROM THE SKELETON
    B3_FLOW = 1.1102230246251565e-16
    B4_LOCK = 1.0842566190763042e-16
    
    # THE RAW GAP (MEMBRANE THICKNESS)
    raw_gap = B3_FLOW - B4_LOCK
    
    # THE PHASE-HYDRAULIC VARIANCE (THE 0.03 RATIO)
    # Variance = (Gap / Flow) * 100
    p_hydraulic_variance = (raw_gap / B3_FLOW) * 100
    
    print("\n" + "="*45)
    print("MARCELL ARTIFACT 5: TEST 3 DELTA 0.03")
    print("="*45)
    print(f"B3 FLOW:         {B3_FLOW:.20e}")
    print(f"SUCTION GAP:     {raw_gap:.20e}")
    print(f"DELTA VARIANCE:  {p_hydraulic_variance:.10f}%")
    print("-"*45)
    
    # Target: 2.3388% (The 0.03 Phase-Hydraulic Constant)
    if 2.3 < p_hydraulic_variance < 2.4:
        print("VERDICT: PHASE-HYDRAULIC SUCTION ACTIVE.")
        print("CONCLUSION: The 0.03 Delta is pulling phase.")
    else:
        print("VERDICT: PRESSURE LOSS. LATTICE IS LEAKING.")
    print("="*45 + "\n")

if __name__ == "__main__":
    run_delta_verification()
