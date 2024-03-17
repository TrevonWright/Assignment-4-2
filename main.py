# Input from user
employee_name = input("Enter employee's name: ")
num_shifts = int(input("Enter number of shifts: "))
num_transactions = int(input("Enter number of transactions: "))
transaction_value = float(input("Enter transaction value: "))


# calculate productivity score
productivity_score = transaction_value / (num_transactions * num_shifts)


# Calculate bonus
if productivity_score <= 30:
    bonus = 50.00
elif 31 <= productivity_score <= 69:
    bonus = 75.00
elif 70 <= productivity_score <= 199:
    bonus = 100.00
else:
    bonus = 200.00

#Output
print("Employee Name:", employee_name)
print("Employee Bonus: ${:.2f}".format(bonus))
