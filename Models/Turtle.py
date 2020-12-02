from Models.Enemy import Enemy
from bangtal import *

class Turtle(Enemy):
    def __init__(self, scene, x, y, x_size, y_size, velocity, user, image='/Images/character/enemy/turtle.png'):
        super().__init__(scene, x, y, x_size, y_size, velocity, image)
        self.user = user
        self.attacked = False

        self.timer = TurtleTimer(0.01, self, self.user)
        self.timer.start()
        
    def run(self):
        self.x -= self.velocity
        self.locate(self.scene, self.x, self.y)
        self.setScale(0.6)
        self.show()
 

class TurtleTimer(Timer):
    def __init__(self, seconds, turtle, user):
        super().__init__(seconds)
        self.turtle = turtle
        self.user = user

    def onTimeout(self):
        self.turtle.run()
        #print(self.user.x, self.user.y)
        self.check_crush()
        self.set(0.01)
        self.start()
    
    def check_crush(self) :
        x = self.turtle.x
        X = self.user.x

        if X-20<x<X+20 and 45<=self.user.y<60 and not self.turtle.attacked:
            self.user.crush()
            self.turtle.attacked=True
                
        
        