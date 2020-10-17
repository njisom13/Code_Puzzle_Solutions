import math

def coordinates(degrees, radius):
    return(round(radius*math.cos(degrees*(math.pi/180)),10), round(radius*math.sin(degrees*(math.pi/180)),10))
