placings = ["United States","Sweden","Switzerland","Canada","Great Britain","Norway","South Korea","Japan","Italy","Denmark"]

def old_main():
    #I set up a main function because of habit
    while 1 == 1:
        #Infinite loop until requested to end
        country_name = str(input("Please enter a country name."))
        for i in range(0,10):
            #Just the range of countries
            if country_name == placings[i]:
                #Compares index to country names
                if i == 0:
                    print(country_name, "placed", i+1,"(Gold Medal)")
                elif i == 1:
                    print(country_name, "placed", i+1,"(Silver Medal)")
                elif i == 2:
                    print(country_name, "placed", i+1,"(Bronze Medal)")
                    #All the above compares for specifically first, second, and third placed medals
                elif i > 2:
                    print(country_name, "placed", i+1,)
                    #I also add 1 to i so that it shows the proper placement
                break
            #I add a break here so it would avoid the elif
            elif i == 9:
                print(country_name,"did not compete")
                #prints if it searches through the entire list and none of the names the user entered comes up
            i += 1
            #loops
        leave = str(input("Would you like to go again, yes or no?"))
        if leave == "no" or leave == "No" or leave == "NO":
            break
        #Simple ask questions in the form of strings compared to integers.

        
def get_country():
    country_name = str(input("Please enter a country name."))
    return country_name

def get_placing(standings, country):
    for i in range(0,10):
        if standings[i].startswith(country):
            return i+1
        elif i == 9:
            return 0
        i += 1
def main():
    while 1 == 1:
        country_name = get_country()
        placing = get_placing(placings, country_name)
        if placing == 1:
            print("The", placings[0],"placed", placing, "(gold medal)")
        elif placing == 2:
            print(placings[1],"placed", placing, "(silver medal)")
        elif placing == 3:
            print(placings[2],"placed", placing, "(bronze medal)")
        elif placing >3:
            print(placings[placing-1],"placed", placing)
        elif placing == 0:
            print(country_name, "did not participate")
        leave = str(input("Would you like to go again? type quit to exit."))
        if leave == "quit" or leave == "Quit" or leave == "QUIT":
            break    
main()


#Stones = heavy polished granite rocks meant to be slid across ice
#House = the target that the stone needs to end on
#Button = the center of the house that is the best spot
#Sweeper = the athletes with like the broom that guides the stones onto the house
#skip = is the strategy maker and also shoots the last shot

#Norway has won the most medals at 329

#The biathalon of skiing and shooting.
