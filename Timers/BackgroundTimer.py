from bangtal import Timer

class BackgroundTimer(Timer):
    def __init__(self, seconds, scene, background1, background2):
        super().__init__(seconds)
        self.scene = scene
        self.background1 = background1
        self.background2 = background2
        self.velocity = 5

    def onTimeout(self):
        self.background1.x -= self.velocity
        if self.background1.x == -1280:
            self.background1.x = 1280
        self.background1.locate(self.scene, self.background1.x, 0)

        self.background2.x -= self.velocity
        if self.background2.x == -1280:
            self.background2.x = 1280
        self.background2.locate(self.scene, self.background2.x, 0)

        self.set(0.01)
        self.start()