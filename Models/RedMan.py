from Models.Enemy import Enemy, EnemyTimer
from bangtal import *


class RedMan(Enemy):
    def __init__(
        self, scene, x, y, x_size, y_size, velocity, user, image="/Images/character/enemy/redman.png", scale=1
    ):
        super().__init__(scene, x, y, x_size, y_size, velocity, user, image, scale)

        self.timer = EnemyTimer(0.01, self, self.user)
        self.timer.start()
