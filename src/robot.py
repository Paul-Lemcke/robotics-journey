import math
class Robot:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
   
    def dist(self, x, y):
        dx= x - self.x
        dy = y - self.y 
        return math.sqrt(dx**2 + dy**2)
        