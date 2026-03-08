def get_amount(prompt):
    while True:
        value = float(input(prompt))
        if value > 0:
            return value
        print("Invalid amount. Please enter a value greater than 0.")

while True:
    budget_input = input("Enter your total monthly budget (or 'exit' to quit): Rs.")
    if budget_input.lower() == "done":
        print("Goodbye!")
        break
    budget = float(budget_input)
    if budget <= 0:
        print("Invalid amount. Please enter a value greater than 0.")
        continue

    expense1 = get_amount("Enter expense 1 amount: Rs.")
    expense2 = get_amount("Enter expense 2 amount: Rs.")
    expense3 = get_amount("Enter expense 3 amount: Rs.")

    total_expenses = expense1 + expense2 + expense3
    remaining = budget - total_expenses

    print(f"\nTotal Budget:    Rs.{budget:.2f}")
    print(f"Total Expenses:  Rs.{total_expenses:.2f}")
    print(f"Remaining Balance: Rs.{remaining:.2f}")

    if remaining < 500:
        print("Warning: Low Funds")