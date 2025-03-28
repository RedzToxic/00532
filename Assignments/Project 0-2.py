# Make a CarFinder

# Does initial text, made it here because repeating elements
def houseKeeping():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu: ")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

# The list that was provided
AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan"]

# Calls function
houseKeeping();

# Defines what user input is
user_input = int(input())

# Checks the user input and does actions based on it
if user_input == 1:
    for car in (AllowedVehiclesList):
        print(car)
else:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
