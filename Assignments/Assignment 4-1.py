"""
This program calculates prices for custom house signs.
""" 

# Declare and initialize variables here.

# Charge for this sign.
charge = 0.00

# Number of characters.
numChars = 8

# Color of characters.
color = "gold"

# Type of wood.
woodType = "oak"

# Base charge for a sign
charge = 35.00

# Takes input of how many chars, what wood type and what color they would like to use
numChars = float(input("How many characters would you like?: "))
woodType = input("What type of wood?: ")
color = input("What type of text color?: ")

# Write assignment and if statements here as appropriate.

# Checks if number if characters exced 5, if so each one is charged
if (numChars > 5):
    charge = charge + (numChars - 5) * 4.00
else:
    charge = charge

# Check if the wood that is inputed is oak
if (woodType == "oak"):
    charge = charge + 20.00
else:
    charge = charge

# Check if the color that is inputed is gold
if (color == "gold"):
    charge = charge + 15.00 
else: 
    charge = charge

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))