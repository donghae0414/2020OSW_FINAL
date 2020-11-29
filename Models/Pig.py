from Models.Enemy import Enemy
from bangtal import *

class Pig(Enemy):
    def __init__(self, scene, x, y, x_size, y_size, velocity, user, image='/Images/character/enemy/pig.png'):
        super().__init__(scene, x, y, x_size, y_size, velocity, image)
        self.user = user
        self.attacked = False

        self.timer = PigTimer(0.01, self, self.user)
        self.timer.start()
        
    def run(self):
        self.x -= self.velocity
        self.locate(self.scene, self.x, self.y)
        self.setScale(0.6)
        self.show()
 

class PigTimer(Timer):
    def __init__(self, seconds, pig, user):
        super().__init__(seconds)
        self.pig = pig
        self.user = user

    def onTimeout(self):
        self.pig.run()
        #print(self.user.x, self.user.y)
        self.check_crush()
        self.set(0.01)
        self.start()
    
    def check_crush(self) :
        x, y= self.pig.x, self.pig.y

        if 80<x<120 and 45<=self.user.y<60 and not self.pig.attacked:
            self.user.crush()
            self.pig.attacked=True
                
        
        