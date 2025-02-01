# Furniture.py - This program calculates profits and sales prices for a furniture company.

# All initial declarations of the name and how much a TV stand costs in either retail or whole sale pricing.
itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# Write your assignment statements here for profit, salePrice, and saleProfit

# Calculating the profit by subtracting the retailPrice from wholesalePrice
profit = retailPrice - wholesalePrice
# Calculating the sale price as being deducted for 25% from retailPrice
salePrice = .75 * retailPrice
# Calculating the profit by using the saleProfit variable then doing salePrice minus the wholesalePrice
saleProfit = salePrice - wholesalePrice

#Given program which prints/ outputs all corresponding values and variables
print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))
