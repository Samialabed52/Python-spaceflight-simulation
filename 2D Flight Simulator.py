"""
Created on Wed Jan 20 16:41:20 2021

@author: leahd
"""


"""Simulation of spaceship chasing another"""
import matplotlib.pyplot
import math

def simulation(simTime, alpha, beta, speed1, speed2, x1, y1, x2, y2):   
    """Simulates a spaceship pursuit"""
    
    posArr = []
    angArr = []
    duration = 0
    
    #initial angle and distance between each ship
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    angle = math.degrees(math.asin((y1 - y2)/dist))
    #add to array
    posArr.append(dist)
    angArr.append(angle)
    
    #if runaway ship already in range of chasing ship
    if dist <= beta and -alpha <= angle <= alpha:
        print('Dead before you could run')
        return (posArr, angArr, duration)
    
    for t in range(simTime):
    #check if ship can get blasted
        if dist <= beta and -alpha <= angle <= alpha:
            print('That guy is dead')
            return (posArr, angArr, duration)
        
        # if it is within + angle, but not distance, fleeing ship moves up
        if -alpha <= angle <= alpha and not dist <= beta:
            y1 += speed1
            #chasing ship follows
            y2 += speed2
            #if ship is within distance but not angle, will run forward
        elif dist <= beta and not -alpha <= angle <= alpha:
            x1 += speed1
            #chasing ship comes at the current angle to get a better shot
            x2 += speed2
            #if ship is neither in range or at the right angle, ship flies at 45 degrees, and chasing ship flies at angle
        elif not dist <= beta and not -alpha <= angle <= alpha:
            if x1 > x2:
                x1 += speed1 * math.cos(45)
                x2 += speed2 * math.cos(angle)
            else:
                x1 -= speed1 * math.cos(45)
                x2 += speed2 * math.cos(angle)
            if y1 > y2:
                y1 += speed1 * math.sin(45)
                y2 += speed2 * math.sin(angle)
            else:
                y1 -= speed1 * math.sin(45)
                y2 += speed2 * math.sin(angle)
    
        #calculate new position and angle
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        angle = math.degrees(math.asin((y1 - y2)/dist))
        #add new position and angle to list of data
        posArr.append(dist)
        angArr.append(angle)
        
        duration += 1
        
    if dist <= beta and -alpha <= angle <= alpha:
        print('That guy is dead')
        return (posArr, angArr, duration)
    else:
        print('Ship escaped')
        return (posArr, angArr, duration) 

#########################################################################################################################
######################################## MAIN FUNCTION ##################################################################
#########################################################################################################################
"""User interface and output"""

#duration of simulation
simTime = int(input('Enter chase time: '))

#death constraints
alpha = int(input('Insert the angle of death: '))
beta = int(input('Insert the distance of death: '))

#velocity input of the two ships
speed1 = int(input('Enter speed of the runaway ship: '))
speed2 = int(input('Enter speed of the chaser ship: '))

#starting points of each ship
x1 = int(input('Enter x-starting point of runaway ship: '))
y1 = int(input('Enter y-starting point of runaway ship: '))
x2 = int(input('Enter x-starting point of chaser ship: '))
y2 = int(input('Enter y-starting point of chaser ship: '))
    
posArr, angArr, duration = simulation(simTime, alpha, beta, speed1, speed2, x1, y1, x2, y2)

print(posArr)
print(angArr)

displot = matplotlib.pyplot.plot(range(duration + 1), posArr)

matplotlib.pyplot.show()

angplot = matplotlib.pyplot.plot(range(duration + 1), angArr)

matplotlib.pyplot.show()