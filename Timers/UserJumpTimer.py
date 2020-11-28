from bangtal import Timer

class UserJumpTimer(Timer):
    def __init__(self, seconds, user):
        super().__init__(seconds)
        self.user = user

    def onTimeout(self):
        self.user.y += self.user.up_velocity
        self.user.up_velocity -= 2

        if self.user.y <= 45:
            self.user.y = 45; self.user.up_velocity = 0

        self.user.locate(self.user.scene, self.user.x, self.user.y)
        
        self.set(0.01)
        self.start()