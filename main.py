# PROJECT 2: EXPENSE TRACKER

# Step 1: Initialize the total state
total = 0  

print("--- DecodeLabs Expense Tracker ---")
print("Enter your expense amounts below. Type 'quit' to calculate final total.\n")

# Step 2: Establish the continuous audit loop
while True:
    user_input = input("Enter expense amount: ").strip()
    
    # Step 3: Check for the sentinel kill switch value
    if user_input.lower() == 'quit':
        print("\nExecution halted via sentinel switch.")
        break  
        
    # Step 4: Implement the Digital error handling barrier
    try:  
        # Attempt to transform raw text string input into a real integer number
        new_expense = int(user_input)
        
        # Apply the accumulator pattern logic to add to the running total
        total = total + new_expense
        print(f"-> Added: ${new_expense} | Current running total: ${total}")
        
    except ValueError:
        # Catch unexpected string data to prevent a system crash
        print("[Invalid Data] Please provide a valid integer number.")

# Step 5: Final Output Stream presentation
print(f"FINAL TOTAL SPENT: {total:.2f}")