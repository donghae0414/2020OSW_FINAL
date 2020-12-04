from Models.Background import *
from Models.User import *

from Models.RedMan import *

from Timers.BackgroundTimer import *

from Generator import *
import time
class GameManager:
    def __init__(self, scene):
        self.scene = scene
        self.scene.onKeyboard = self.onKeyBoard

        self.background1 = Background('Images/background/background.png', 0)
        self.background1.locate(self.scene, self.background1.x, 0)
        self.background1.show()
        self.background2 = Background('Images/background/background.png', 1280)
        self.background2.locate(self.scene, self.background2.x, 0)
        self.background2.show()

        self.backgroundTimer = BackgroundTimer(0.01, self.scene, self.background1, self.background2)
        self.backgroundTimer.start()

        self.user = User('Images/character/user/run/user_1.png', self.scene, 0.9, self)
        self.user.locate(self.scene, self.user.x, self.user.y)
        self.user.show()
        
        self.generator = Generator(self.scene, self.user)

    def up_velocity(self):
        print('velocity up!')
        self.generator.velocity += 1

    def init_velocity(self):
        print('init velocity')
        self.generator.velocity = 10

    def onKeyBoard(self, key, pressed):
        if key == 84 and pressed:                   # Up Button
            if self.user.y == 45:
                self.user.jump()

        elif key == 85:                 # Down Button
            if pressed:
                self.user.down()
            else:
                self.user.growup()

        elif key == 83:                             # Ahead Button
            if pressed:
                if self.user.x <= 1000:
                    self.user.is_ahead_stop = False
                    self.user.ahead()
            else:                                   # Stop during going ahead
                self.user.is_ahead_stop = True

        elif key == 82:                             # Back Button
            if pressed:
                if self.user.x >= 20:
                    self.user.is_back_stop = False
                    self.user.back()        
            else:                                   # Stop during going back
                self.user.is_back_stop = True
                #self.user.stop()
