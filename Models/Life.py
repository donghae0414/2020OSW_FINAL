from Models.Enemy import Enemy
from bangtal import *

class Life(Enemy):
    def __init__(self, scene, x, y, x_size, y_size, velocity, user, image='/Images/life.png', scale=1):
        super().__init__(scene, x, y, x_size, y_size, velocity, user, image, scale)
        #self.attacked = False
        self.is_eatten = False

        self.timer = LifeTimer(0.01, self, self.user)
        self.timer.start()

class LifeTimer(Timer):
    def __init__(self, seconds, enemy, user):
        super().__init__(seconds)
        self.enemy = enemy
        self.user = user
        self.combo_checked = False

    def onTimeout(self):
        if not self.enemy.is_eatten:
            self.enemy.run()
        self.check_crush()

        if self.enemy.x > (-1)*self.enemy.x_size and not self.enemy.is_eatten:
            self.set(0.01)
            self.start()

    def check_crush(self):
        enemy_x_size, enemy_y_size = self.enemy.x_size, self.enemy.y_size

        small_enemy_x, small_enemy_y = self.enemy.x, self.enemy.y
        big_enemy_x = small_enemy_x + enemy_x_size*self.enemy.scale
        big_enemy_y = small_enemy_y + enemy_y_size*self.enemy.scale
        
        user_x_size, user_y_size = self.user.x_size, self.user.y_size

        small_user_x, small_user_y = self.user.x, self.user.y
        big_user_x = small_user_x + user_x_size*self.user.scale
        big_user_y = small_user_y + user_y_size*self.user.scale

        threshold = 40
        small_user_x += threshold;  big_user_x -= threshold
        small_user_y += threshold;  big_user_y -= 30

        small_enemy_x += threshold;  big_enemy_x -= threshold
        small_enemy_y += threshold;  big_enemy_y -= threshold

        if not self.enemy.attacked:
            if small_user_x < small_enemy_x < big_user_x:
                if small_user_y <= small_enemy_y <= big_user_y:
                    self.user.eat_life()
                    self.enemy.hide()
                    self.enemy.is_eatten = True

                elif small_user_y <= big_enemy_y <= big_user_y:
                    self.user.eat_life()
                    self.enemy.hide()
                    self.enemy.is_eatten = True
                   
            elif small_user_x < big_enemy_x < big_user_x:
                if small_user_y <= small_enemy_y <= big_user_y:
                    self.user.eat_life()
                    self.enemy.hide()
                    self.enemy.is_eatten = True
                    
                elif small_user_y <= big_enemy_y <= big_user_y:
                    self.user.eat_life()
                    self.enemy.hide()
                    self.enemy.is_eatten = True
                    