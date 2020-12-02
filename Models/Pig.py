from Models.Enemy import Enemy, EnemyTimer
from bangtal import *

class Pig(Enemy):
    def __init__(self, scene, x, y, x_size, y_size, velocity, user, image='/Images/character/enemy/pig.png', scale=1):
        super().__init__(scene, x, y, x_size, y_size, velocity, user, image, scale)
        #self.attacked = False

        self.timer = EnemyTimer(0.01, self, self.user)
        self.timer.start()
        
#    def run(self):
#        self.x -= self.velocity
#        self.locate(self.scene, self.x, self.y)
#        self.setScale(0.6)
#        self.show()
 

#class PigTimer(Timer):
#    def __init__(self, seconds, pig, user):
#        super().__init__(seconds)
#        self.pig = pig
#        self.user = user

#    def onTimeout(self):
#        self.pig.run()
#        self.check_crush()
#        self.set(0.01)
#        self.start()
    
#    def check_crush(self) :
#        x = self.pig.x
#        X = self.user.x

#        if X-20<x<X+20 and 45<=self.user.y<60 and not self.pig.attacked:
#            self.user.crush()
#            self.pig.attacked=True
                
        
        