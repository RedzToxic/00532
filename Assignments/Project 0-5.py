# Continue making the CarFinder

 # The list that was provided (moved list outside loop since it only needs to be delared once) 
AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan", "Rivian RT1", "Ram 1500"]

# Finally added a loop, since the user might be doing mutiple actions in one sitting, like adding new vehicles

while True:

    # Does initial text, made it here because repeating elements
    def houseKeeping():
        print("********************************")
        print("AutoCountry Vehicle Finder v0.5")
        print("********************************")
        print("Please Enter the following number below from the following menu: ")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")
        print("5. Exit")


    # Calls function
    houseKeeping();


    # Defines what user input is and how gets it
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


    # If chosen 3, it will respond by asking which vehicle the user wants to add
    elif user_input == 3:
        print("Please Enter the full Vehicle name you would like to add: ")

        # Takes in the response from the user and then is used for append value in append function
        add_vehicle = input()

        # This is where the appending happens, the append function is being fed the user input
        AllowedVehiclesList.append(add_vehicle)

        # The program confirms to the user, after it has appended the new car to the list 
        print(f'You have added {add_vehicle} as an authorized vehicle')

    # If chosen 4, it will respond by asking which car user wants to remove and if they're sure
    elif user_input == 4:
        print("Please Enter the full Vehicle name you would like to REMOVE: ")

        # gets the user response for which car
        remove_vehicle = input()

        # double checks with the user if they want to do this change
        print(f'Are you sure you want to remove {remove_vehicle} from the Authorized Vehicles List?')

        # takes in the final input
        final_input = input()

        # checks if the final input is yes, then it will remove the desired car
        if final_input == "yes":

            # the program removes the car and reminds the user of what action they've just done and what car they removed
            AllowedVehiclesList.remove(remove_vehicle)
            print(f'You have REMOVED {remove_vehicle} as an authorized vehicle')

    # If last one is chosen than it closes
    else:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break