from enum import Enum
from bangtal import *

class User(Object):
    def __init__(self, image, scene):
        super().__init__(image)
        self.image = image
        self.scene = scene
        self.x = 100
        self.y = 45
        self.up_velocity = 0
        self.down_velocity = 0

        self.life = 3
        self.life_img=[]
        for i in range(self.life) :
            img = Object('Images/life.png')
            self.life_img.append(img)
            img.setScale(0.1)
            img.locate(self.scene, 1100+i*50, 650)
            img.show()
        

        self.state = UserState.RUN
        self.run_state = 0  # 0 ~ 5

        self.user_jump_Timer = UserJumpTimer(0.01, self)
        self.user_down_Timer = UserDownTimer(0.01, self)
        self.user_ahead_Timer = UserAheadTimer(0.01, self)
        self.user_back_Timer = UserBackTimer(0.01, self)
        self.user_run_Timer = UserRunTimer(0.1, self)
        self.user_run_Timer.start()

    def crush(self) :
        if self.life == 1 :
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
        self.down_velocity = 0
        self.state = UserState.DOWN
        self.user_jump_Timer.stop()
        self.user_down_Timer.start()

    def ahead(self):
        self.x += 5
        self.user_ahead_Timer.start()
    
    def back(self):
        self.x -= 5
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

class UserDownTimer(Timer):
    def __init__(self, seconds, user):
        super().__init__(seconds)
        self.user = user

    def onTimeout(self):
        if self.user.state == UserState.DOWN:
            if self.user.up_velocity > 0:
                self.user.y -= self.user.down_velocity
                self.user.down_velocity += 1
            else:
                self.user.y += self.user.up_velocity
                self.user.up_velocity -= 1

            if self.user.y <= 45:
                self.user.y = 45; self.user.down_velocity = 0.0
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
        if self.user.x <= 700:
            self.user.ahead()
            self.user.locate(self.user.scene, self.user.x, self.user.y)
            self.set(0.01)
            self.start()

class UserBackTimer(Timer):
    def __init__(self, seconds, user):
        super().__init__(seconds)
        self.user = user

    def onTimeout(self):
        if self.user.x >= 100:
            self.user.back()
            self.user.locate(self.user.scene, self.user.x, self.user.y)
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