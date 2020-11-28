from Models.Background import *
from Timers.BackgroundTimer import *

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

    def onKeyBoard(self, key, pressed):
        if key == 84:
            pass
            #self.character.velocity = 30
    

