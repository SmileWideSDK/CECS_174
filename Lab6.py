def get_magnitude(number):
    magnitude = float(-1)
    #Defines variable before setting up the loop that only allows positive numbers
    while magnitude < 0:
        magnitude = float(input("Please enter the magnitude for earthquake" + str(number)+ ':  '))
        return magnitude
    #Returns value back to main

def compare_magnitudes(m1, m2):
    strength_difference = round(float(10**(1.5*(m1-m2))),1)
#Calculates strength
    return strength_difference
#Returns it back to main


def get_run_again():
    leave = int(input("Try again? Type 1 for yes: "))
    bye = False
    if leave != 1:
        bye = True
    return bye
#Simple acquire value and return

def main():
#Create infinite loop
    while(1 == 1):
        value1 = float(get_magnitude(1))
        value2 = float(get_magnitude(2))

        if value1 > value2:
            magnitude1 = value1
            magnitude2 = value2

        elif value2 > value1:
            magnitude1 = value2
            magnitude2 = value1
#Acquired first input value and reorganized them into the largest value being first
            
        difference = float(compare_magnitudes(magnitude1, magnitude2))
        if magnitude1 > magnitude2:
            print("An earthquake of magnitude", magnitude1, "is", difference, "times more powerful than an earthquake of magnitude", magnitude2)
#receives calculations of strength differences and prints out the result
        good_bye = get_run_again()
#Acquires if the user still wishes to continue
        if good_bye == True:
            print("goodbye")
            exit
            quit
            break
#If the user wishes to quit, then the returned value has to be anything not 1.
        #I also just used every possible quit command I know or would seem to reasonably work.

##############################################################################################

#Actual call of the start of the program        
main()
    
#Japan : 9.1
#San Francsisco: 6.9
#Haiti : 7

#2: An earthquake of magnitude 9.1 is 1412.5 times more powerful than an earthquake of magnitude 7.0

#Haiti was nearly 800 deaths, Japan 15,896 deaths. I am appreciative of building and safety codes that would prevent death in most circumstances.
