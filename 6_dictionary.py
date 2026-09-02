========================================
CODE
========================================

# 1. Friends' names and their lengths
friends = ['Aditya', 'Priya', 'Rahul', 'Sneha', 'Karan']
friends_tuples = [(name, len(name)) for name in friends]
print("Friends list of tuples:")
print(friends_tuples)

print()

# 2. Trip expenses
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

# Total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more overall by", your_total - partner_total)
elif partner_total > your_total:
    print("Your partner spent more overall by", partner_total - your_total)
else:
    print("Both spent the same amount overall")

print()

# Category with biggest difference
max_diff = 0
max_category = None
for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        max_category = category

print("Category with the most significant difference:", max_category)
print("Difference amount:", max_diff)


========================================
OUTPUT
========================================

Friends list of tuples:
[('Aditya', 6), ('Priya', 5), ('Rahul', 5), ('Sneha', 5), ('Karan', 5)]

Your total expenses: 3000
Partner's total expenses: 3050
Your partner spent more overall by 50

Category with the most significant difference: Hotel
Difference amount: 200
