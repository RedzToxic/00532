# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here

#calcualting the state tax
stateTax = salary * .065
federalTax = salary * .28
dependentDeduction = salary * .025 * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# My outputs
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
# Given output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
