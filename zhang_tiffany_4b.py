
import random

total_red_hit = 0
total_gray_hit = 0
total_green_hit = 0
total_blue_hit = 0
total_yellow_hit = 0
total_missed = 0
total_overlap_hit = 0

throws = int(input("How many dart throws? "))

while throws <= 0:
    throws = int(input("Please enter a positive number: "))

for i in range(0, throws):
    hit_shape = False 
    hit_gray = False #make hitgray false at beginning
    x_coord = random.randint(0,801) #generates between 0 and 800 (noninclusive so we do 801)
    y_coord = random.randint(0,501)

    #check if it has hit blue
    if x_coord <= 800 and x_coord >= 300 and y_coord <= 150 and y_coord >= 50:
        total_blue_hit += 1
        hit_shape = True
    
    #check if it has hit grey by seeing if the distance to center of grey is less than 100 (the radius)
    #center is at (300,250)
    if ((x_coord-300)**2 + (x_coord-250)**2)**0.5 <= 100:
        total_gray_hit += 1
        hit_shape = True
        hit_gray = True

    #check if it has hit yellow by seeing if the distance to center of grey is less than 100 (the radius)
    #center is at (600,300) radius is 150
    if ((x_coord-600)**2 + (y_coord-300)**2)**0.5 <= 150:
        total_yellow_hit += 1
        hit_shape = True

    #check if it has hit green by seeing if the distance to center of grey is less than 100 (the radius)
    #center is at (300,400)
    if ((x_coord-300)**2 + (y_coord-400)**2)**0.5 <= 100:
        total_green_hit += 1
        hit_shape = True
        if hit_gray == True:
            total_overlap_hit += 1
    
    #check if it has hit red
    if x_coord <= 200 and y_coord <= 250:
        #this if statement checks if it's within the hole, if it is, then it has missed
        if x_coord > 50 and x_coord < 150 and y_coord < 200 and y_coord > 100:
            hit_shape = False
        else:
            total_red_hit += 1
            hit_shape = True
            
    #if hitshape is false, then increment totalMissed (it has not hit anything)
    if hit_shape == False:
        total_missed += 1
    
print("\n")
print("Blue: ", format(total_blue_hit, ","), " (", format((total_blue_hit/throws), ".2%"), ")", sep='')
print("Yellow: ", format(total_yellow_hit, ","), " (", format(total_yellow_hit/throws, ".2%"), ")", sep='')
print("Red: ", format(total_red_hit, ","), " (", format(total_red_hit/throws, ".2%"), ")", sep='')
print("Gray: ", format(total_gray_hit, ","), " (", format(total_gray_hit/throws, ".2%"), ")", sep='')
print("Green: ", format(total_green_hit, ","), " (", format(total_green_hit/throws, ".2%"), ")", sep='')
print("Gray and green overlap: ", format(total_overlap_hit, ","), " (", format(total_overlap_hit/throws, ".2%"), ")", sep='')
print("Miss: ", format(total_missed, ","), " (", format(total_missed/throws, ".2%"), ")", sep='')

