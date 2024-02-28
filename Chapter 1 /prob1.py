import math

class Sphere:
    """Takes the radius of the sphere returns the diameter, circumference, surface area and volume."""
    def __init__(self, radius):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    
    def getDiameter(self):
        return self.radius*2
    
    def getCircumference(self):
        return self.radius * 2 * math.pi
    
    def getSurfaceArea(self):
        return 4 * math.pi * (self.radius**2)
    
    def getVolume(self):
        return (4/3)* math.pi * (self.radius**3)
     