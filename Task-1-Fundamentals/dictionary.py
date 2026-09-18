# 1
# Create a list of at least 5 friends' names
friends = ["Vinit", "Shreya", "Vinu", "Shree", "Vinushree"]

# Create a list of tuples: (name, length)
name_lengths = [(name, len(name)) for name in friends]

print("Friends Name Length Tuples:")
print(name_lengths)

# 2 
# Define expenses for both partners across 5 categories
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
total_your_expenses = sum(your_expenses.values())
total_partner_expenses = sum(partner_expenses.values())
combined_total = total_your_expenses + total_partner_expenses

print(f"Your Total Expense: ${total_your_expenses}")
print(f"Partner's Total Expense: ${total_partner_expenses}")
print(f"Combined Trip Expense: ${combined_total}")

# Determine overall highest spender
if total_your_expenses > total_partner_expenses:
    print(f"You spent more overall by ${total_your_expenses - total_partner_expenses}.")
elif total_partner_expenses > total_your_expenses:
    print(f"Your partner spent more overall by ${total_partner_expenses - total_your_expenses}.")
else:
    print("Both spent the exact same amount overall.")

# Identify category with the largest spending difference
differences = {cat: abs(your_expenses[cat] - partner_expenses[cat]) for cat in your_expenses}
max_diff_category = max(differences, key=differences.get)
print(f"Largest Expense Difference: {max_diff_category} (Difference: ${differences[max_diff_category]})")