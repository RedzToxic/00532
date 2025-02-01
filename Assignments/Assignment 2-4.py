# Given input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here

# Calcualting the state tax by taking the salary and mult by 6.5%
stateTax = salary * .065
# Calculating the federal tax by taking the salary and mult by 28%
federalTax = salary * .28
# Calciulating the dependent deductions by taking the salary mult by 2.5% and by how many dependents is given from input
dependentDeduction = salary * .025 * numDependents
# Calculating the total withholding by taking all previous taxes and deductions and adding them toghether
totalWithholding = stateTax + federalTax + dependentDeduction
# Calculating how much employee takes home by subtracting the salary from the totalWithholding's
takeHomePay = salary - totalWithholding

# My outputs statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))

# Given output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
