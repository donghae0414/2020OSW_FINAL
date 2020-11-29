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

        self.user = User('Images/character/user/run/user_1.png', self.scene)
        self.user.locate(self.scene, self.user.x, self.user.y)
        self.user.show()
        
        self.generator = Generator(self.scene, self.user)
        self.generator.create_redman()
        

    def onKeyBoard(self, key, pressed):
        if key == 84 and pressed:
            if self.user.y == 45:
                self.user.jump()
    