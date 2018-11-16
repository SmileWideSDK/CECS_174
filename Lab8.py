interstate_number = 0
is_it_prime = False
direction = ("I don't know yet")
is_arterial = False
parent_highway = 0
#Setting global variables

def get_interstate_number():
    highway_num = input("Please enter a US Interstate Highway route number: ")
    if highway_num.startswith('I-',0,2) or highway_num.startswith('i-',0,2):
        num = highway_num[2:]
        return num
    elif highway_num.isdigit():
        return highway_num
    elif len(highway_num) == 4:
        num = highway_num[1:]
        print(num)
        return num
    elif highway_num.startswith('Interstate',0,11) or highway_num.startswith('interstate',0,11):
        num = highway_num[11:]
        print(num)
        return num

#Inquires user for input
def is_primary(number):
    is_prime = True
    if number > 1 and number <100:
        return is_prime
    if number > 100:
        return False
#Checks quota for highway number
def compass_orientation(number):
    if number % 2 == 0:
        return ("east-west")
    elif number % 2 != 0:
        return ("north-south")
#Calculates distance
def is_arterial(number):
    arterial = False
    if number % 5 == 0:
        arterial = True
        return arterial
    elif number % 5 !=0:
        arterial = False
        return arterial
#determines if it is arterial
def auxiliary_type(number):
    first_num = (str(number))[:1]
    if int(first_num) % 2 == 0:
        return "circumferential"
    if int(first_num) % 2 != 0:
        return "spur"
#calculates if the highway is circumferential or spur
def parent_highway(number):
    parent_highway = 0
    if number > 100:
        parent_highway = abs(number) % 100
        return parent_highway
#calculates the parent highway for highways eligible
def main():
    while 1 == 1:
    #Setting for the try again feature
                    
        interstate_number = 0
        is_it_prime = False
        direction = ("")
        arterial = False                    
        type_auxiliary = ("") 
        parent_highway_num = 0
        try_again = 1
        
        #Resetting variable values so that it can loop
                    
        interstate_number = int(get_interstate_number())
        is_it_prime = is_primary(interstate_number)
        type_auxiliary = auxiliary_type(interstate_number)
        direction = compass_orientation(interstate_number)
        type_artierial = is_arterial(interstate_number)
        arterial = is_arterial(interstate_number)
        if arterial == False:
            arterial = ""
        if arterial == True:
            arterial = ("long-distance arterial ")
        if is_it_prime == False:
            parent_highway_num = parent_highway(interstate_number)
            print("Interstate", interstate_number, "is a", type_auxiliary, "highway of Interstate", parent_highway_num)
            #For 3 digit highways
        if is_it_prime == True:
            print("Interstate", interstate_number, "is a", arterial, "highway oriented", direction)
            #for 2 digit or less highways
            
        try_again = int(input("Would you like to try again? 1 for yes, 0 for no."))
        if try_again == 0:
            break
        #asks if the user wishes to repeat the program
main()

#1) Dwight D. Eisenhower
#2) I-405
#3) formed in Bellingham, Washington. It is unlikely because the 405 is in Southern California compared to Washington not being near so-cal
#4) Because Dwight D. Eisenhower chose to do so.
