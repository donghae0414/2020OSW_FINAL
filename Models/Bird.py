from Models.Enemy import Enemy, EnemyTimer
from bangtal import *
import random


class Bird(Enemy):
    def __init__(self, scene, x, y, x_size, y_size, velocity, user, image="/Images/character/enemy/bird.png", scale=1):
        super().__init__(scene, x, y, x_size, y_size, velocity, user, image, scale)

        self.timer = EnemyTimer(0.01, self, self.user)
        self.timer.start()
        self.is_uping = random.random() < 0.5

    def run(self):
        self.x -= self.velocity
        if self.is_uping:
            self.y -= 3
            if self.y <= 400:
                self.is_uping = False
        else:
            self.y += 3
            if self.y >= 550:
                self.is_uping = True

        self.locate(self.scene, self.x, self.y)
        self.setScale(self.scale)
        self.show()
