combination_from_user1 = int(input("What is the first number of your combo?"))

while combination_from_user1 > 39 or combination_from_user1 < 0:
    combination_from_user1 = int(input("What is the first number of your combo?"))

combination_from_user2 = int(input("What is the second number of your combo?"))

while combination_from_user2 > 39 or combination_from_user2 < 0:
    combination_from_user2 = int(input("What is the second number of your combo?"))

combination_from_user3 = int(input("What is the third number of your combo?"))

while combination_from_user3 > 39 or combination_from_user3 < 0:
    combination_from_user3 = int(input("What is the third number of your combo?"))
#The variables above are making sure that the user's inputs stay within the realistic boundaries of our theoretical lock.
failed_combo = 1

while failed_combo == 1:
#This is the while function causing it to loop endlessly.
    ticks_clockwise = int(input("How many clockwise ticks?"))
    ticks_counter_clockwise = int(input("How many counter clockwise ticks?"))
    ticks_final_clockwise = int(input("Finally, how many clockwise ticks?"))
    lock_value = 0
    failed_combo = 1
#Variable reset and control + user input
    if 40 - ticks_clockwise == combination_from_user1:
        print("first number unlocked")
        if (combination_from_user1 + ticks_counter_clockwise) - 40  == combination_from_user2:
            print("second number unlocked")
            if 40 - (ticks_final_clockwise - combination_from_user2) == combination_from_user3:
                    print("you win, you get to go home now.")
                    break
            elif combination_from_user2 - ticks_final_clockwise == combination_from_user3:
                    print("you win, you get to go home now.")
                    break

        elif (combination_from_user1 + ticks_counter_clockwise) == combination_from_user2:
            print("second number unlocked")
            if 40 - (ticks_final_clockwise - combination_from_user2) == combination_from_user3:
                    print("you win, you get to go home now.")
                    break
            elif combination_from_user2 - ticks_final_clockwise == combination_from_user3:
                    print("you win, you get to go home now.")
                    break
#The actual equation for calculating the combination was legitimately the hardest thing in this. Like, the locks
#I used in high school were super different than this, so I had to just be really imaginative and logic'd everything.
        
            

#1) 64000 different combinations
#2) 192000 seconds, or 3200 minutes, or 53.33 hours, or 2.22 days
#3) the competitor's lock would take longer to force open by trying random combinations, since there are 1000000 total combinations.




