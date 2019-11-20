#JamesDraney Project 11
#TheEndIsNear
#james.draney1@marist.edu
#letsgetitfolks

import math 

class sphere:

    def __init__(self, radius):

        self.radius=radius
        self.surfaceArea=4*math.pi*self.radius**2
        self.volume=(4/3)*math.pi*self.radius**3

    def getRadius(self):

        return self.radius

    def getsurfaceArea(self):

        return self.surfaceArea

    def getvolume(self):

        return self.volume

def main():
        radius=float(input("Enter radius of sphere: " ))
        NewSphere=sphere(radius)
        print("Surface area: ", NewSphere.getsurfaceArea())
        print("Volume: ", NewSphere.getvolume())

    
main()
