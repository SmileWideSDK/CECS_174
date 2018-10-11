import random
secret = random.randrange(10) + 1
i = 0
# Variable control for constants
while 1 == 1:
    print(i + 1, "attempt(s)")
    answer = int(input("What shall be your guess?"))
#Input, loop, and keeping track of tries for user
    if answer == secret :
        print ("good job, you got it in", i, "attempt(s).")    
        break
#Upon finally guessing the value
    i += 1
if i > 5 and i < 10 :
    print("That's pretty unlucky.")
if i >= 10 :
    print("Don't buy a lottery ticket... ever.")
#Final statements.
