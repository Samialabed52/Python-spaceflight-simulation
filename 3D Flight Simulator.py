"""
Created on Wed Jan 20 16:41:20 2021

@author: leahd
"""


"""Simulation of spaceship chasing another"""
import matplotlib.pyplot
import math
import random as rand

def simulation(simTime, theta, phi, beta, speed1, speed2, x1, y1, z1, x2, y2, z2):   
    """Simulates a spaceship pursuit"""
    
    posArr = []
    horAngArr = []
    vertAngArr = []
    duration = 0
    
    #initial angle and distance between each ship
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    vertAngle = math.degrees(math.atan((z1 - z2) / (y1 - y2)))
    horAngle = math.degrees(math.atan((y1 - y2) / (x1 - x2)))
    
    #add first value to array
    posArr.append(dist)
    horAngArr.append(horAngle)
    vertAngArr.append(vertAngle)
    
    #if runaway ship already in range of chasing ship
    if dist <= beta and -theta <= horAngle <= theta and -phi <= vertAngle <= phi:
        print('Dead before you could run')
        return (posArr, horAngArr, vertAngArr, duration)
    
    #run simulation
    for t in range(simTime):
        
        #check if ship can get blasted
        if dist <= beta and -theta <= horAngle <= theta and -phi <= vertAngle <= phi:
            print('That guy is dead')
            return (posArr, horAngArr, vertAngArr, duration)
        
        
        # if it is within vertical angle, but not horizontal angle or distance, fleeing ship moves straight up
        if -phi <= vertAngle <= phi and not -theta <= horAngle <= theta and not dist <= beta:
            if z1 > z2:
                z1 += speed1
                z2 += speed2 * math.sin(rand.randrange(46))
            else:
                z1 -= speed1
                z2 -= speed2 * math.sin(rand.randrange(46))
                
            if x1 > x2:
                x2 += speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                x2 -= speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
            
            if y1 > y2:
                y2 += speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                y2 -= speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))               
            
        # if it is within horizontal angle, but not vertical angle or distance, fleeing ship moves straight on y-axis
        elif not -phi <= vertAngle <= phi and -theta <= horAngle <= theta and not dist <= beta:
            if y1 > y2:
                y1 += speed1
                y2 += speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                y1 -= speed1
                y2 -= speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
                
            if z1 > z2:
                z2 += speed2 * math.sin(rand.randrange(46))
            else:
                z2 -= speed2 * math.sin(rand.randrange(46))
                
            if x1 > x2:
                x2 += speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                x2 -= speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
        
        # if it is within distance, but not horizontal or vertical angle, fleeing ship moves straight on x-axis
        elif not -phi <= vertAngle <= phi and not -theta <= horAngle <= theta and dist <= beta:
            if x1 > x2:
                x1 += speed1
                x2 += speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                x1 -= speed1
                x2 -= speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
                
            if y1 > y2:
                y2 += speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                y2 -= speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
                
            if z1 > z2:
                z2 += speed2 * math.sin(rand.randrange(46))
            else:
                z2 -= speed2 * math.sin(rand.randrange(46))  
            
        # if it is within distance and horizontal angle, but not vertical angle, fleeing ship moves along x and y
        elif not -phi <= vertAngle <= phi and -theta <= horAngle <= theta and dist <= beta:
            if z1 > z2:
                z2 += speed2 * math.sin(rand.randrange(46))
            else:
                z2 -= speed2 * math.sin(rand.randrange(46))
            
            if x1 > x2:
                x1 += speed1 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
                x2 += speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                x1 -= speed1 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
                x2 -= speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
                
            if y1 > y2:
                y1 += speed1 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
                y2 += speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                y1 -= speed1 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
                y2 -= speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
        
        # if it is within distance and vertical angle, but not horizontal angle, fleeing ship moves along x and z
        elif -phi <= vertAngle <= phi and not -theta <= horAngle <= theta and dist <= beta:
            if y1 > y2:
                y2 += speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                y2 -= speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
            
            if x1 > x2:
                x1 += speed1 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
                x2 += speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                x1 -= speed1 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
                x2 -= speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
                
            if z1 > z2:
                z1 += speed1 * math.sin(rand.randrange(46))
                z2 += speed2 * math.sin(rand.randrange(46))
            else:
                z1 -= speed1 * math.sin(rand.randrange(46))
                z2 -= speed2 * math.sin(rand.randrange(46))
        
        # if it is within horizontal and vertical angle, but not distance, fleeing ship moves along y and z
        elif -phi <= vertAngle <= phi and -theta <= horAngle <= theta and not dist <= beta:
            
            if x1 > x2:
                x2 += speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                x2 -= speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
            
            if y1 > y2:
                y1 += speed1 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
                y2 += speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                y1 -= speed1 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
                y2 -= speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
                
            if z1 > z2:
                z1 += speed1 * math.sin(rand.randrange(46))
                z2 += speed2 * math.sin(rand.randrange(46))
            else:
                z1 -= speed1 * math.sin(rand.randrange(46))
                z2 -= speed2 * math.sin(rand.randrange(46))
        
        #if ship is not in any range
        elif not -phi <= vertAngle <= phi and not -theta <= horAngle <= theta and not dist <= beta:
            if x1 > x2:
                x1 += speed1 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
                x2 += speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                x1 -= speed1 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
                x2 -= speed2 * math.cos(rand.randrange(46)) * math.cos(rand.randrange(46))
            
            if y1 > y2:
                y1 += speed1 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
                y2 += speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
            else:
                y1 -= speed1 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
                y2 -= speed2 * math.sin(rand.randrange(46)) * math.cos(rand.randrange(46))
                
            if z1 > z2:
                z1 += speed1 * math.sin(rand.randrange(46))
                z2 += speed2 * math.sin(rand.randrange(46))
            else:
                z1 -= speed1 * math.sin(rand.randrange(46))
                z2 -= speed2 * math.sin(rand.randrange(46))
    
        #calculate new position and angles
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        vertAngle = math.degrees(math.atan((z1 - z2) / (y1 - y2)))
        horAngle = math.degrees(math.atan((y1 - y2) / (x1 - x2)))
        
        #add new position and angles to list of data
        posArr.append(dist)
        vertAngArr.append(vertAngle)
        horAngArr.append(horAngle)
        
        #time array increases by 1
        duration += 1
        
    #if ship is blown after last iteration
    if dist <= beta and -theta <= horAngle <= theta and -phi <= vertAngle <= phi:
        print('That guy is dead')
        return (posArr, horAngArr, vertAngArr, duration)
    
    #if ship ecaped
    else:
        print('Ship escaped')
        return (posArr, horAngArr, vertAngArr, duration)

#########################################################################################################################
######################################## MAIN FUNCTION ##################################################################
#########################################################################################################################
"""User interface and output"""

#duration of simulation
simTime = int(input('Enter chase time: '))

#death constraints
theta = int(input('Insert the horizontal angle of death: '))
phi = int(input('Insert the vertical angle of death: '))
beta = int(input('Insert the distance of death: '))

#velocity input of the two ships
speed1 = int(input('Enter speed of the runaway ship: '))
speed2 = int(input('Enter speed of the chaser ship: '))

#starting points of each ship
x1 = int(input('Enter x-starting point of runaway ship: '))
y1 = int(input('Enter y-starting point of runaway ship: '))
z1 = int(input('Enter z-starting point of runaway ship: '))
x2 = int(input('Enter x-starting point of chaser ship: '))
y2 = int(input('Enter y-starting point of chaser ship: '))
z2 = int(input('Enter z-starting point of chaser ship: '))
    
#create arrays for graph using simulation function
posArr, horAngArr, vertAngArr, duration = simulation(simTime, theta, phi, beta, speed1, speed2, x1, y1, z1, x2, y2, z2)

# #print arrays
# print(posArr)
# print(horAngArr)
# print(vertAngArr)

#position plot
matplotlib.pyplot.plot(range(duration + 1), posArr)
matplotlib.pyplot.xlabel('Time')
matplotlib.pyplot.ylabel('Distance')
matplotlib.pyplot.grid()
matplotlib.pyplot.show()

#horizontal angle plot
matplotlib.pyplot.plot(range(duration + 1), horAngArr)
matplotlib.pyplot.xlabel('Time')
matplotlib.pyplot.ylabel('Horizontal Angle')
matplotlib.pyplot.grid()
matplotlib.pyplot.show()

#vertical angle plot
matplotlib.pyplot.plot(range(duration + 1), vertAngArr)
matplotlib.pyplot.xlabel('Time')
matplotlib.pyplot.ylabel('Vertical Angle')
matplotlib.pyplot.grid()
matplotlib.pyplot.show()