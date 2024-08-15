# Calculate Net Income
print('Earned amount:')
print('Bubblegum: $202')
print('Toffee: $118')
print('Ice cream: $2250')
print('Milk chocolate: $1680')
print('Doughnut: $1075')
print('Pancake: $80')
income = 202 + 118 + 2250 + 1680 + 1075 + 80
print('income: ' + str(income))

staff_expenses = int(input('Staff expenses: '))
other_expenses = int(input('other expenses: '))
net_income = income - (staff_expenses + other_expenses)
print('net income:', str(net_income))
