from enum import Enum
from bangtal import *
import time

class User(Object):
    def __init__(self, image, scene):
        super().__init__(image)
        self.image = image
        self.scene = scene

        self.x = 100;   self.y = 45
        self.x_size = 265;  self.y_size = 260;
        self.scale = 1

        self.up_velocity = 0
        self.down_velocity = 0
        self.ahead_velocity = 5
        self.back_velocity = -5

        self.life = 3
        self.life_img=[]
        for i in range(self.life) :
            img = Object('Images/life.png')
            self.life_img.append(img)
            img.setScale(0.1)
            img.locate(self.scene, 1100+i*50, 650)
            img.show()
        
        self.combo = 0
        self.MaxCombo = 0

        self.state = UserState.RUN
        self.run_state = 0  # 0 ~ 5

        self.is_ahead_stop = True
        self.is_back_stop = True

        self.user_jump_Timer = UserJumpTimer(0.01, self)
        #self.user_down_Timer = UserDownTimer(0.01, self)
        self.user_ahead_Timer = UserAheadTimer(0.01, self)
        self.user_back_Timer = UserBackTimer(0.01, self)
        self.user_run_Timer = UserRunTimer(0.1, self)
        self.user_run_Timer.start()
    

    def locate(self, scene, x, y):
        super().locate(scene, x, y)
        super().setScale(self.scale)

    def add_combo(self):
        self.combo += 1
        self.MaxCombo = max(self.MaxCombo, self.combo)

        first_num = int(self.combo / 10)
        second_num = self.combo % 10

        second = Object('Images/number/' + str(second_num) + '.png')
        second.x = 920; second.y = 500; second.scene = self.scene; second.scale = 0.8
        second.locate(self.scene, 920, 450)
        second.setScale(0.8)
        second.show()

        combo = Object('Images/combo.png')
        combo.x = 1000; combo.y = 530; combo.scene = self.scene; combo.scale = 0.4
        combo.locate(self.scene, 1000, 480)
        combo.setScale(0.4)
        combo.show()

        if first_num != 0:
            first = Object('Images/number/' + str(first_num) + '.png')
            first.x = 850; first.y = 500; first.scene = self.scene; first.scale = 0.8
            first.locate(self.scene, 840, 450)
            first.setScale(0.8)
            first.show()
            t = ComboTimer(0.01, first, second, combo)
            t.start()
        else:
            t = ComboTimer(0.01, second, combo)
            t.start()
        

    def crush(self) :
        self.combo = 0

        burst = Object('Images/burst.png')
        burst.locate(self.scene, 380, 140)
        #burst.locate(self.scene, self.x, self.y)
        #burst.setScale(0.5)
        burst.show()

        bursttimer = BurstTimer(0.3, burst, self)
        bursttimer.start()


        if self.life == 1 :
            print(self.MaxCombo)
            endGame()
        else :
            self.life -=1
            self.life_img[-1].hide()
            del self.life_img[-1]
            print('crush!!')


    def run(self):
        if self.state == UserState.RUN:
            self.run_state += 1
            if self.run_state == 6:
                self.run_state = 0

            self.setImage('Images/character/user/run/user_' + str(self.run_state) + '.png')        
    
    def jump(self):
        self.up_velocity = 30
        self.state = UserState.JUMP
        self.setImage('Images/character/user/jump.png')
        self.user_run_Timer.stop()
        self.user_jump_Timer.start()

    def down(self):
        #self.down_velocity = 0
        #self.state = UserState.DOWN
        #self.user_jump_Timer.stop()
        #self.user_down_Timer.start()
        if self.state == UserState.JUMP:
            self.up_velocity = -15
        else:                               #TODO 납작 업드리기
                print('드러눕기 구현해라')

    def ahead(self):
        self.user_ahead_Timer.start()
    
    def back(self):
        self.user_back_Timer.start()    

    def stop(self):
        self.user_ahead_Timer.stop()
        self.user_back_Timer.stop()


class UserState(Enum):
    RUN = 0,
    JUMP = 1,
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
                self.user.y = 45; self.user.up_velocity = 0.0
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

            #self.user.ahead()

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

            #self.user.back()
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
