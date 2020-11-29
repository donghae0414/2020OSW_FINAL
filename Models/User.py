from enum import Enum
from bangtal import Object, Timer

class User(Object):
    def __init__(self, image, scene):
        super().__init__(image)
        self.image = image
        self.scene = scene
        self.x = 100
        self.y = 45
        self.up_velocity = 0

        self.heart = 3

        self.state = UserState.RUN
        self.run_state = 0  # 0 ~ 5

        self.user_jump_Timer = UserJumpTimer(0.01, self)

        self.user_run_Timer = UserRunTimer(0.1, self)
        self.user_run_Timer.start()

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



class UserState(Enum):
    RUN = 0,
    JUMP = 1


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

class UserRunTimer(Timer):
    def __init__(self, seconds, user):
        super().__init__(seconds)
        self.user = user

    def onTimeout(self):
        self.user.run()
        
        self.set(0.1)
        self.start()