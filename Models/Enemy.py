from bangtal import Object, Timer


class Enemy(Object):
    def __init__(self, scene, x, y, x_size, y_size, velocity, user, image, scale=1):
        super().__init__(image)
        self.image = image
        self.scene = scene
        self.user = user
        self.scale = scale
        self.attacked = False

        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size

        self.velocity = velocity

    def locate(self, scene, x, y):
        super().locate(scene, x, y)
        super().setScale(self.scale)

    def run(self):
        self.x -= self.velocity
        self.locate(self.scene, self.x, self.y)
        self.setScale(self.scale)
        self.show()


class EnemyTimer(Timer):
    def __init__(self, seconds, enemy, user):
        super().__init__(seconds)
        self.enemy = enemy
        self.user = user
        self.combo_checked = False

    def onTimeout(self):
        self.enemy.run()
        self.check_crush()
        if not self.combo_checked:
            self.check_combo()

        if self.enemy.x > (-1) * self.enemy.x_size:
            self.set(0.01)
            self.start()

    def check_combo(self):
        small_enemy_x = self.enemy.x
        enemy_x_size = self.enemy.x_size
        big_enemy_x = small_enemy_x + enemy_x_size * self.enemy.scale

        small_user_x = self.user.x

        if big_enemy_x < small_user_x and not self.enemy.attacked:
            self.combo_checked = True
            self.user.add_combo()

    def check_crush(self):
        enemy_x_size, enemy_y_size = self.enemy.x_size, self.enemy.y_size

        small_enemy_x, small_enemy_y = self.enemy.x, self.enemy.y
        big_enemy_x = small_enemy_x + enemy_x_size * self.enemy.scale
        big_enemy_y = small_enemy_y + enemy_y_size * self.enemy.scale

        user_x_size, user_y_size = self.user.x_size, self.user.y_size

        small_user_x, small_user_y = self.user.x, self.user.y
        big_user_x = small_user_x + user_x_size * self.user.scale
        big_user_y = small_user_y + user_y_size * self.user.scale

        threshold = 40
        small_user_x += threshold
        big_user_x -= threshold
        small_user_y += threshold
        big_user_y -= 30

        small_enemy_x += threshold
        big_enemy_x -= threshold
        small_enemy_y += threshold
        big_enemy_y -= threshold

        if not self.enemy.attacked:
            if small_user_x < small_enemy_x < big_user_x:
                if small_user_y <= small_enemy_y <= big_user_y:
                    self.user.crush()
                    self.enemy.attacked = True
                    # print('user_x :', small_user_x, big_user_x, ', user_y :', small_user_y, big_user_y)
                    # print('enemy_x :', small_enemy_x, big_enemy_x, ', enemy_y :', small_enemy_y, big_enemy_y)
                elif small_user_y <= big_enemy_y <= big_user_y:
                    self.user.crush()
                    self.enemy.attacked = True

            elif small_user_x < big_enemy_x < big_user_x:
                if small_user_y <= small_enemy_y <= big_user_y:
                    self.user.crush()
                    self.enemy.attacked = True

                elif small_user_y <= big_enemy_y <= big_user_y:
                    self.user.crush()
                    self.enemy.attacked = True
