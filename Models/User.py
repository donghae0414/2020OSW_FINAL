from enum import Enum
from bangtal import *
import time
import GameManager


class User(Object):
    def __init__(self, image, scene, scale, game_manager):
        super().__init__(image)
        self.ReGameMenu = Scene("MENU", "Images/background/background.png")
        self.image = image
        self.scene = scene
        self.game_manager = game_manager

        self.x = 100
        self.y = 45
        self.x_size = 265
        self.y_size = 260
        self.origin_scale = scale
        self.scale = scale
        self.startTime = time.time()

        self.up_velocity = 0
        self.down_velocity = 0
        self.ahead_velocity = 5
        self.back_velocity = -5

        self.up_background_velocity = None
        self.down_background_velocity = None

        self.jump_count = 0

        self.life = 3
        self.life_img = []
        for i in range(self.life):
            img = Object("Images/life.png")
            self.life_img.append(img)
            img.setScale(0.1)
            img.locate(self.scene, 1200 - i * 50, 650)
            img.show()

        self.combo = 0
        self.MaxCombo = 0

        self.state = UserState.RUN
        self.run_state = 0  # 0 ~ 5

        self.is_ahead_stop = True
        self.is_back_stop = True

        self.user_jump_Timer = UserJumpTimer(0.01, self)
        # self.user_down_Timer = UserDownTimer(0.01, self)
        self.user_ahead_Timer = UserAheadTimer(0.01, self)
        self.user_back_Timer = UserBackTimer(0.01, self)
        self.user_run_Timer = UserRunTimer(0.1, self)
        self.user_run_Timer.start()

    def locate(self, scene, x, y):
        super().locate(scene, x, y)
        super().setScale(self.scale)

    def eat_life(self):
        self.life += 1
        img = Object("Images/life.png")
        img.setScale(0.1)
        img.locate(self.scene, 1200 - len(self.life_img) * 50, 650)
        self.life_img.append(img)
        img.show()

    def add_combo(self):
        self.combo += 1
        self.game_manager.up_velocity()
        # self.up_background_velocity()

        self.MaxCombo = max(self.MaxCombo, self.combo)

        first_num = int(self.combo / 10)
        second_num = self.combo % 10

        second = Object("Images/number/" + str(second_num) + ".png")
        second.x = 920
        second.y = 500
        second.scene = self.scene
        second.scale = 0.8
        second.locate(self.scene, 920, 450)
        second.setScale(0.8)
        second.show()

        combo = Object("Images/combo.png")
        combo.x = 1000
        combo.y = 530
        combo.scene = self.scene
        combo.scale = 0.4
        combo.locate(self.scene, 1000, 480)
        combo.setScale(0.4)
        combo.show()

        if first_num != 0:
            first = Object("Images/number/" + str(first_num) + ".png")
            first.x = 850
            first.y = 500
            first.scene = self.scene
            first.scale = 0.8
            first.locate(self.scene, 840, 450)
            first.setScale(0.8)
            first.show()
            t = ComboTimer(0.01, first, second, combo)
            t.start()
        else:
            t = ComboTimer(0.01, second, combo)
            t.start()

    def crush(self):
        self.combo = 0
        self.game_manager.init_velocity()
        # self.down_background_velocity()

        burst = Object("Images/burst.png")
        burst.locate(self.scene, 380, 140)
        burst.show()

        bursttimer = BurstTimer(0.3, burst, self)
        bursttimer.start()

        if self.life == 1:
            self.menu()
        else:
            self.life -= 1
            self.life_img[-1].hide()
            del self.life_img[-1]
            print("crush!!")

    def run(self):
        if self.state == UserState.RUN:
            self.run_state += 1
            if self.run_state == 6:
                self.run_state = 0

            self.setImage("Images/character/user/run/user_" + str(self.run_state) + ".png")

    def jump(self):
        if self.y == 45:
            self.jump_count = 1

            self.up_velocity = 25
            self.state = UserState.JUMP
            self.setImage("Images/character/user/jump.png")
            self.user_run_Timer.stop()
            self.user_jump_Timer.start()
        else:
            if self.jump_count == 1:
                self.jump_count += 1

                self.up_velocity = 25
                self.state = UserState.JUMP
                self.setImage("Images/character/user/jump.png")
                self.user_run_Timer.stop()
                self.user_jump_Timer.start()
            else:
                pass

    def down(self):
        if self.state == UserState.JUMP:
            self.up_velocity = -15
        else:  # TODO 납작 업드리기
            self.setScale(0.5)
            self.scale = 0.5

    def growup(self):
        self.setScale(self.origin_scale)
        self.scale = self.origin_scale

    def ahead(self):
        self.user_ahead_Timer.start()

    def back(self):
        self.user_back_Timer.start()

    def stop(self):
        self.user_ahead_Timer.stop()
        self.user_back_Timer.stop()

    def menu(self):
        print(self.MaxCombo)
        print(round(time.time() - self.startTime, 2))
        self.game_manager.generator.timer.stop()
        self.print_Combo_duration()
        ReGameScene = Scene("GAME", "Images/button/start.png")

        restartButton = Object("Images/button/restart.png")
        restartButton.locate(self.ReGameMenu, 561, 140)
        restartButton.setScale(0.3)
        restartButton.show()

        exitButton = Object("Images/button/exit.png")
        exitButton.locate(self.ReGameMenu, 561, 80)
        exitButton.setScale(0.3)
        exitButton.show()

        def restartButton_onMouseAction(x, y, action):
            ReGameScene.enter()
            self.__init__(self.image, self.scene, 0.9, self.game_manager)
            self.user_run_Timer.stop()
            newmanager = GameManager.GameManager(ReGameScene)

        restartButton.onMouseAction = restartButton_onMouseAction

        def exitButton_onMOuseAction(x, y, action):
            endGame()

        exitButton.onMouseAction = exitButton_onMOuseAction

        startGame(self.ReGameMenu)

    def print_Combo_duration(self):
        showMessage('MaxCombo : {}           Duration : {}'.format(self.MaxCombo, round(time.time() - self.startTime, 2)))
        # first_num = int(self.MaxCombo / 10)
        # second_num = self.MaxCombo % 10

        # MaxCombo = Object("Images/result/MaxCombo.png")
        # MaxCombo.locate(self.ReGameMenu, 417, 415)
        # MaxCombo.show()

        # Duration = Object("Images/result/Duration.png")
        # Duration.locate(self.ReGameMenu, 390, 315)
        # Duration.show()

        # first = Object("Images/result/" + str(first_num) + ".png")
        # first.locate(self.ReGameMenu, 675, 415)
        # first.show()

        # second = Object("Images/result/" + str(second_num) + ".png")
        # second.locate(self.ReGameMenu, 775, 415)
        # second.show()

        # duration = int(round(time.time() - self.startTime, 2) * 100)

        # if duration < 1000:
        #     a = duration // 100
        #     c = (duration % 100) // 10
        #     d = duration % 10
        # else:
        #     a = duration // 1000
        #     b = (duration % 1000) // 100
        #     bb = Object("Images/result/" + str(b) + ".png")
        #     c = ((duration % 1000) % 100) // 10
        #     d = duration % 10

        # point = Object("Images/result/point.png")
        # aa = Object("Images/result/" + str(a) + ".png")
        # cc = Object("Images/result/" + str(c) + ".png")
        # dd = Object("Images/result/" + str(d) + ".png")

        # if duration < 1000:
        #     aa.locate(self.ReGameMenu, 675, 315)
        #     point.locate(self.ReGameMenu, 748, 315)
        #     cc.locate(self.ReGameMenu, 775, 315)
        #     dd.locate(self.ReGameMenu, 875, 315)

        #     aa.show()
        #     point.show()
        #     cc.show()
        #     dd.show()

        # else:
        #     aa.locate(self.ReGameMenu, 675, 315)
        #     bb.locate(self.ReGameMenu, 760, 315)
        #     point.locate(self.ReGameMenu, 845, 315)
        #     cc.locate(self.ReGameMenu, 875, 315)
        #     dd.locate(self.ReGameMenu, 975, 315)

        #     aa.show()
        #     bb.show()
        #     point.show()
        #     cc.show()
        #     dd.show()


class UserState(Enum):
    RUN = (0,)
    JUMP = (1,)
    DOWN = 2


class UserJumpTimer(Timer):
    def __init__(self, seconds, user):
        super().__init__(seconds)
        self.user = user

    def onTimeout(self):
        if self.user.state == UserState.JUMP:
            self.user.y += self.user.up_velocity
            self.user.up_velocity -= 1

            if self.user.y <= 45:
                self.user.y = 45
                self.user.up_velocity = 0.0
                self.user.state = UserState.RUN
                self.user.user_run_Timer.set(0.1)
                self.user.user_run_Timer.start()

            self.user.locate(self.user.scene, self.user.x, self.user.y)

            self.set(0.01)
            self.start()


class UserAheadTimer(Timer):
    def __init__(self, seconds, user):
        super().__init__(seconds)
        self.user = user

    def onTimeout(self):
        if self.user.x <= 1000:
            self.user.x += self.user.ahead_velocity
            self.user.locate(self.user.scene, self.user.x, self.user.y)

            # self.user.ahead()

            if not self.user.is_ahead_stop:
                self.set(0.01)
                self.start()


class UserBackTimer(Timer):
    def __init__(self, seconds, user):
        super().__init__(seconds)
        self.user = user

    def onTimeout(self):
        if self.user.x >= 20:
            self.user.x += self.user.back_velocity
            self.user.locate(self.user.scene, self.user.x, self.user.y)

            # self.user.back()
            if not self.user.is_back_stop:
                self.set(0.01)
                self.start()


class UserRunTimer(Timer):
    def __init__(self, seconds, user):
        super().__init__(seconds)
        self.user = user

    def onTimeout(self):
        self.user.run()

        self.set(0.1)
        self.start()


class BurstTimer(Timer):
    def __init__(self, seconds, burst, user):
        super().__init__(seconds)
        self.burst = burst
        self.user = user
        self.second = seconds
        self.count = 0

    def onTimeout(self):
        self.burst.hide()


class ComboTimer(Timer):
    def __init__(self, seconds, *objects):
        super().__init__(seconds)
        self.limit = 0.25
        self.second = seconds
        self.now_duration = 0
        self.objects = objects

    def onTimeout(self):
        self.now_duration += self.second

        for object in self.objects:
            object.y += 4
            object.locate(object.scene, object.x, object.y)
            object.setScale(object.scale)
            object.show()

        if self.limit > self.now_duration:
            self.set(self.second)
            self.start()
        else:
            for object in self.objects:
                object.hide()
