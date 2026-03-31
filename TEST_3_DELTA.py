import numpy as np

def execute_delta_audit():
    # INPUT DATA FROM PREVIOUS TESTS
    B3 = 1.1102230246251565e-16
    B4 = 1.0842566190763042e-16
    GAP = B3 - B4
    
    # CALCULATE THE 0.03 VARIANCE (PHASE-HYDRAULIC PRESSURE)
    variance_percentage = (GAP / B3) * 100
    
    print("\n" + "="*45)
    print("MARCELL DISTRIBUTION: TEST 3 (0.03 DELTA)")
    print("="*45)
    print(f"RAW GAP:         {GAP:.20e}")
    print(f"LATTICE VARIANCE: {variance_percentage:.10f}%")
    print("-"*45)
    
    # 2.33% is the decimal equivalent of the 0.03 phase shift in this resolution
    if 2.3 < variance_percentage < 2.4:
        print("VERDICT: PHASE-HYDRAULIC PRESSURE DETECTED.")
        print("CONCLUSION: The 0.03 Suction is active. The engine is primed.")
    else:
        print("VERDICT: STATIC EQUILIBRIUM. NO PRESSURE DETECTED.")
    print("="*45 + "\n")

if __name__ == "__main__":
    execute_delta_audit()
