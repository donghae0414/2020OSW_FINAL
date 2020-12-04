from bangtal import Object

class Background(Object):
    def __init__(self, image, x = 0):
        super().__init__(image)
        self.x = x
    def locate(self, scene, x, y):
        super().locate(scene, x, y)
        super().show()