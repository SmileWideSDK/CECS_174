import math 
gravity = float(9.8)
distance = float(input("How far away will your target be? "))
if (distance <0 ):
    distance = float(input("How far away will your target be? Please keep it positive. "))

gunpowder = float(input("How much gunpowder will you use? "))
if (gunpowder < 0 ):
    gunpoweder = float(input("How much gunpowder will you use? Please keep it even. "))

angle = float(input("What angle shall the cannon be aimed at? "))
if angle <= 0  or  angle > 90:
   angle = float(input("What angle shall the cannon be aimed at? Please keep it greater than 0 and less than 90. "))


radians = (angle * (math.pi/180))
speed = float(gunpowder * 10)
velocity_x = (math.sin(radians)) * speed
velocity_y = (math.cos(radians)) * speed
air_time = ((2*velocity_y)/gravity)
total_distance = air_time * velocity_x
if (total_distance < distance +1) and (total_distance > distance -1):
    print("You hit the target!")

if (total_distance > distance +1):
    print("You shot over the target by", total_distance - distance, "meters :(")
if (total_distance < distance -1):
    print("You shot under the target by", distance - total_distance, "meters :(")
    
#1: 45 degrees max distnace
#2: 90 degrees max height
#3: 90 - y
