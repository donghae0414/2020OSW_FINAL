from Models.Enemy import Enemy
from bangtal import *

class RedMan(Enemy):
    def __init__(self, scene, x, y, x_size, y_size, velocity, user, image='/Images/character/enemy/redman.png'):
        super().__init__(scene, x, y, x_size, y_size, velocity, image)
        self.user = user
        self.attacked = False

        self.timer = RedManTimer(0.01, self, self.user)
        self.timer.start()
        
    def run(self):
        self.x -= self.velocity
        self.locate(self.scene, self.x, self.y)
        self.setScale(0.6)
        self.show()
 

class RedManTimer(Timer):
    def __init__(self, seconds, redman, user):
        super().__init__(seconds)
        self.redman = redman
        self.user = user
    def onTimeout(self):
        self.redman.run()
        #print(self.user.x, self.user.y)
        self.check_crush()
        self.set(0.01)
        self.start()
    
    def check_crush(self) :
        x, y= self.redman.x, self.redman.y
        #print(x)
        #print(self.user.x)
        #print(self.user.y)
        if 80<x<120 and 45<=self.user.y<60 and not self.redman.attacked:
            if self.user.heart == 1 :
                endGame()
            else :
                self.redman.attacked=True
                print('crush!!')
                self.user.heart-=1
                
        
        