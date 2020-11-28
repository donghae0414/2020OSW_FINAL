from Models.Enemy import Enemy
from bangtal import Timer

class RedMan(Enemy):
    def __init__(self, scene, x, y, x_size, y_size, velocity, image='/Images/character/enemy/redman.png'):
        super().__init__(scene, x, y, x_size, y_size, velocity, image)

        self.timer = RedManTimer(0.01, self)
        self.timer.start()

    def run(self):
        self.x -= self.velocity
        self.locate(self.scene, self.x, self.y)
        self.setScale(0.6)
        self.show()
 

class RedManTimer(Timer):
    def __init__(self, seconds, redman):
        super().__init__(seconds)
        self.redman = redman

    def onTimeout(self):
        self.redman.run()
        
        self.set(0.01)
        self.start()
        
        