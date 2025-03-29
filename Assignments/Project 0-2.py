# Continue making the CarFinder

# Does initial text, made it here because repeating elements
def houseKeeping():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")
    print("Please Enter the following number below from the following menu: ")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")


# The list that was provided
AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan"]


# Calls function
houseKeeping();


# Defines what user input is
user_input = int(input())


# Checks the user input and does actions based on it
# If chosen 1, it prints list
if user_input == 1:
    for car in (AllowedVehiclesList):
        print(car)
# If chosen 2, it will respond if it's apart or not of list
elif user_input == 2:
    print("Please Enter the full Vechicle name: ")
    # Gets the user input for which car they want
    car_input = input()

    # The two if statements check if the input is authorized or not
    if car_input == "Ford F-150":
        print("Ford F-150 is an authorized vehicle")
    
    if car_input == "Tesla":
        print("Tesla is not an authorized vehicle, if you received this in error please check the spelling and try again.")
# If last one than it closes
else:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

