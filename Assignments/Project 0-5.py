# Continue making the CarFinder

# Incorporating the text file into this program
import os

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
        # Using the file i/o to open and print out the text file
        with open("/Users/daniil/Desktop/COP1000/00532/Assignments/Allowed_Vehicles_List.txt", "r") as db:
            response = db.read()
            print(response)
            

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

         #The new updated code that works with the i/o and allows user to add another car with given input
        with open("/Users/daniil/Desktop/COP1000/00532/Assignments/Allowed_Vehicles_List.txt", "a") as db:
            db.write("\n" + add_vehicle)

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

            # Also an updated version of deleting, this one saves as db than saves the db.readlines as a varaible
            with open("/Users/daniil/Desktop/COP1000/00532/Assignments/Allowed_Vehicles_List.txt", "r") as db:
                cars = db.readlines()

                # Defines what cars is, which a for loop that checks for the remove_vehicle
                cars = [car for car in cars if car != remove_vehicle]

                # Finally writes over it or in other words deletes it within the actual db saved name
                with open("/Users/daniil/Desktop/COP1000/00532/Assignments/Allowed_Vehicles_List.txt", "w") as db:
                    db.writelines(cars)

            print(f'You have REMOVED {remove_vehicle} as an authorized vehicle')

    # If last one is chosen than it closes
    else:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break