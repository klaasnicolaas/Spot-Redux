#!/usr/bin/env python
import math
import matplotlib.pyplot as plt 

"""
---------------------------
First test on inverse kinametics for the spot redux robot specific leg.
Dimensions are worked in milimeters. Angles calculated parallel to the ground plane and then converted to work on a 45 degree angle.

TODO: Workout leg offset to get accurate end affector calculations.
TODO: Give function input and output values so that it can be imported and used in different files.
---------------------------
"""

def calculateLegJointsInDeg(x, y, z):
    lowerLeg = 100
    upperLeg = 100
    lowerLegOffset = 24.24

    #Put leg offset logic here
    #something like: y = y + lowerLegOffset

    #Different calculation incase of no Z offset.
    s = (math.sqrt((y*y)/(z*z))
    shoulderLegAngle = (math.atan(y/z))

    #Refer to Readme.md for explanation.
    lowerLegAngle = math.acos((x*x + s*s - lowerLeg*lowerLeg - upperLeg*upperLeg)/(2*lowerLeg*upperLeg))
    upperLegAngle = math.atan(s/x)-math.atan((upperLeg*math.sin(lowerLegAngle))/(lowerLeg+upperLeg*math.cos(lowerLegAngle)))
    
    #Radians to degrees + fysical offsets.
    upperLegAngle = 225 + ((upperLegAngle*180)/math.pi)
    lowerLegAngle = 180 - ((lowerLegAngle*180)/math.pi)
    shoulderLegAngle = 180 + ((shoulderLegAngle*180)/math.pi)

    #Put leg offset logic here.

    #Calculates angle difference due to upper leg state.
    diffUpperLeg = upperLegAngle - 90
    lowerLegAngle = lowerLegAngle - diffUpperLeg 

    #Invert upperLegAngle due to inverted motor rotation.
    upperLegAngle = 180 - upperLegAngle

    #If angles are negative turn into positive values.
    #Needed because sinus and cosinus functions have possibilities in positive and negative values.
    #Real world always need positive values.
    if(upperLegAngle <= 0):
        upperLegAngle = 180 + upperLegAngle
    if(lowerLegAngle <= 0):
        lowerLegAngle = 180 + lowerLegAngle
    
    print("--------")
    print("onderbeenpos: " + str(lowerLegAngle))
    print("bovenbeenpos: " + str(upperLegAngle))
    print("schouderpos: " + str(shoulderLegAngle))
    forwardKinametics(lowerLegAngle, upperLegAngle, shoulderLegAngle)

def forwardKinametics(lowerLegAngle, upperLegAngle, shoulderLegAngle):
    x = math.tan(upperLegAngle)*(math.cos(lowerLegAngle+45)*20)
    print("------------")
    print(x)

def main():
    for x in range(-40,40):
        calculateLegJointsInDeg(x, -100, 1)

    #plt.plot(x, y) 
    plt.xlabel('x - axis')
    plt.ylabel('y - axis') 
    plt.title('My first graph!') 
    plt.show() 


if __name__ == "__main__":
    main()
