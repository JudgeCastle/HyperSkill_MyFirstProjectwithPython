# Defining my variables
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80
results = (bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake)

# Initiating my output
print("Earned amount:"
      + "\n Bubblegum: $" + str(bubblegum)
      + "\n Toffee: $" + str(toffee)
      + "\n Ice cream: $" + str(ice_cream)
      + "\n Milk chocolate: $" + str(milk_chocolate)
      + "\n Doughnut: $" + str(doughnut)
      + "\n Pancake: $" + str(pancake))

# Spacing the list from the results
print()

# Calling the results which means it does the math
print("Income: $" + str(results))

# Spacing the first results from the net income
print()

# Defining input variables
staff_expenses = int(input("Staff Expenses: "))
other_expenses = int(input("Other Expenses: "))

# Calculating the net income
net_income = results
net_income -= staff_expenses
net_income -= other_expenses

# Show Net Income
print("Net income: $", net_income)