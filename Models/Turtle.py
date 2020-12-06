from Models.Enemy import Enemy, EnemyTimer
from bangtal import *
import random


class Turtle(Enemy):
    def __init__(
        self, scene, x, y, x_size, y_size, velocity, user, image="/Images/character/enemy/turtle.png", scale=1
    ):
        super().__init__(scene, x, y, x_size, y_size, velocity, user, image, scale)

        self.timer = EnemyTimer(0.01, self, self.user)
        self.timer.start()
        self.origin_velocity = velocity

        self.velo_check = False
        self.zero_count = 0

    def run(self):
        if self.x < 640 and not self.velo_check:
            self.velo_check = True
            if random.random() < 0.5:
                self.velocity = 0

        if self.velocity == 0:
            self.zero_count += 1

        if self.zero_count > 100:
            self.velocity = self.origin_velocity

        self.x -= self.velocity
        self.locate(self.scene, self.x, self.y)
        self.setScale(self.scale)
        self.show()
