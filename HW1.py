import sys
menu_navigation = 0
menu_choice = 0
quit1 = 0
#Basic variable set for the start of the program
while quit1 == 0:
    while menu_navigation == 0 and quit1 == 0: 
        menu_choice = 0
        print("Main menu:")
        print("1. Cost of fuel")
        print("2. Used Value")
        print("3. Stopping Distance")
        print("4. Quit")
        menu_choice = int(input("Make your selection: "))
#Above is merely variable control and menu interface
        if menu_choice == 1:
            menu_navigation = 1

        elif menu_choice == 2:
            menu_navigation = 2

        elif menu_choice == 3:
            menu_navigation = 3

        elif menu_choice == 4:
            quit1 = 1
#Options for user to input to navigate the program
        
    while menu_navigation == 1:
        
        print("Cost of Fuel:")
        car_1 = 0
        car_1_cost = 0
        car_2_cost = 0
        car_2 = 0
        return_menu = -1
#Notify user of change
        while car_1 <= 0:
            car_1 = float(input("Car 1's kilowatt-hours per mile rate (kW-h/mi) "))
        while car_1_cost <=0:
            car_1_cost = float(input("Price per KW-h "))
        while car_2 <= 0:
            car_2 = float(input("Car 2's mile per gallon rate (mi/gal) "))
        while car_2_cost <= 0:
            car_2_cost = float(input("Cost of a gallon of gasoline "))
        miles = float(input("How many miles do you drive each month? "))
#Variable control and user input
        cost_1 = float((miles/car_1)*car_1_cost)
        cost_1 = float(round(cost_1, 2))
        print(round(cost_1,2), "dollars per month car#1 ")
        cost_2 = float((miles/car_2)*car_2_cost)
        cost_2 = float(round(cost_2, 2))
        print(round(cost_2,2), "dollars per month car#2 ")
        cost_1_year = cost_1 * 12
        cost_2_year = cost_2 * 12
        if cost_1_year > cost_2_year:
            print("Car 2 will save", cost_1_year - cost_2_year, "in a year!")
        if cost_2_year > cost_1_year:
            print("Car 1 will save", cost_2_year - cost_1_year, "in a year!")
        if cost_1_year == cost_2_year:
            print("Car 1 and Car 2 will save the exact same amount.")
#calculations
        while return_menu >1 or return_menu <0:
            return_menu = int(input("Do you wish to return to the main menu? 1 = yes, 0 = no"))
        if return_menu == 1:
            menu_navigation = 0
#Send back to menu

            
    while menu_navigation == 2:
        print("Used Value")
        i = 0
        car_cost = -1
        years = -1
        return_menu = -1
#variable sets
        while car_cost <0:
            car_cost = float(input("How much did your car cost?"))
        while years <0:
            years = int(input("How many years to track the car's value?"))
        while i < years:
            i += 1
            depriciation_value = car_cost * 0.18
            car_cost = car_cost - depriciation_value
            print("year", + i, " the car costs", + round(car_cost, 2))
#Calculations
        while return_menu >1 or return_menu <0:
            return_menu = int(input("Do you wish to return to the main menu? 1 = yes, 0 = no"))
        if return_menu == 1:
            menu_navigation = 0
#Sends back to menu if the user wishes
            
    while menu_navigation == 3:
        print("Stopping Distances")
        return_menu = -1
        car_speed = -1.1
        car_tires = 0
        friction = float(0.1)
        gravity = 32.174
#Setting variables once more
        while car_speed < 0:
            car_speed = float(input("How fast is the car going?"))
        while car_tires < 1 or car_tires > 3:
            car_tires = int(input("How new are the car's tires? 1 = new, 2 = good, 3 = poor"))
        if car_tires == 1:
            friction = float(0.8)
        elif car_tires == 2:
            friction = float(0.6)
        elif car_tires == 3:
            friction = float(0.5)
        stopping = (car_speed * car_speed)/(2 *friction * gravity)
        print("The car will stop at a minimum of", stopping, "feet")
#Calculations
        while return_menu >1 or return_menu <0:
            return_menu = int(input("Do you wish to return to the main menu? 1 = yes, 0 = no"))
        if return_menu == 1:
            menu_navigation = 0
#Send back to main menu


sys.exit()
exit
#Exits once the loop for the entire program ends when the user chooses quit
