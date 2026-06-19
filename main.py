# ==============================================================================
# PROJECT 2: STATE-PRESERVING EXPENSE TRACKER ENGINE
# Batch: 2026 | Powered by DecodeLabs
# ==============================================================================

def main():
    # PHASE 1: INITIALIZATION (MEMORY BANK)
    # The accumulator state must be initialized OUTSIDE the loop to avoid amnesia.
    total = 0 [cite: 144, 303]
    
    print("=" * 50)
    print(" DECODELABS BACKEND ENGINE: EXPENSE TRACKER ")
    print("=" * 50)
    print("Instructions: Enter integer expense amounts sequentially.")
    print("Type 'quit' to halt execution and view the final ledger total.\n")
    
    # PHASE 2: COMPUTATION & TRANSFORMATION (CONTINUOUS AUDIT LOOP)
    while True: [cite: 173, 175]
        # Raw material receiving via standard input
        raw_input = input("Enter expense amount (or 'quit'): ").strip() [cite: 91, 137]
        
        # THE KILL SWITCH: Sentinel Path Handling
        if raw_input.lower() == 'quit': [cite: 179, 186]
            print("\n[WARNING] Execution halted via sentinel.") [cite: 188]
            break [cite: 191]
            
        # DIGITAL POKA-YOKE: Type-Safety & Error Handling Barrier
        try: [cite: 129, 136]
            # Transformation mechanism: String to Integer conversion
            new_expense = int(raw_input) [cite: 121, 137]
            
            # ACCUMULATOR PATTERN: Updating the stateful ledger
            # State(new) = State(old) + Input
            total += new_expense [cite: 167, 168]
            
            print(f"-> Appended: ${new_expense} | Running Total: ${total}")
            
        except ValueError: [cite: 137, 305]
            # Defensive coding output stream for invalid structural inputs
            print("[ERROR] Invalid Data. System blocked unparsed string.") [cite: 137, 138]
            print("        Please feed a valid raw integer numeric value.") [cite: 97, 139]
            print("-" * 50)

    # PHASE 3: PRESENTATION & ACTION (OUTPUT DISPLAY)
    # Decoupled logic presenting the final actionable reality
    print("=" * 50)
    print(f"FINAL TOTAL: ${total:.2f}") [cite: 196]
    print("=" * 50)
    print("Ledger verification completed successfully. Status: Verified.") [cite: 13]

if __name__ == "__main__":
    main()