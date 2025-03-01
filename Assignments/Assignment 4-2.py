# Make a program that calculates employee's productivity bonus

# Emplyoee's name
employee_name = input("Please enter your first and last name: ")

# Transactions dollar value
trans_dollar_val = float(input("Please enter your transactional dollar value: "))

# Number of transactions
numTransactions = int(input("Please enter your amount of transations: "))

# Number of shifts
numShifts = int(input("Please enter the amount of shifts done: "))

# Calculates productiviy score
productivity_Score = (trans_dollar_val/ numTransactions) / numShifts

# Checks productivity score
if (productivity_Score <= 30):
    print(employee_name)
    print("Employee Bonus: $50.00")
elif (productivity_Score >= 31 and productivity_Score <= 69):
    print(employee_name)
    print("Employee Bonus: $75.00")
elif (productivity_Score >= 70 and productivity_Score <= 199):
    print(employee_name)
    print("Employee Bonus: $100.00")
else:
    print(employee_name)
    print("Employee Bonus: $200")
