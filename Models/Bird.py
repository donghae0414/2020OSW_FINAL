from Models.Enemy import Enemy
from bangtal import *

class Bird(Enemy):
    def __init__(self, scene, x, y, x_size, y_size, velocity, user, image='/Images/character/enemy/bird.png'):
        super().__init__(scene, x, y, x_size, y_size, velocity, image)
        self.user = user
        self.attacked = False

        self.timer = BirdTimer(0.01, self, self.user)
        self.timer.start()
        
    def run(self):
        self.x -= self.velocity
        self.locate(self.scene, self.x, self.y)
        self.setScale(0.6)
        self.show()
 

class BirdTimer(Timer):
    def __init__(self, seconds, bird, user):
        super().__init__(seconds)
        self.bird = bird
        self.user = user

    def onTimeout(self):
        self.bird.run()
        self.check_crush()
        self.set(0.01)
        self.start()
    
    def check_crush(self) :
        x, y= self.bird.x, self.bird.y
        X = self.user.x

        if X-20<x<X+20 and y<=self.user.y<y+100 and not self.bird.attacked:
            self.user.crush()
            self.bird.attacked=True
                
        
        