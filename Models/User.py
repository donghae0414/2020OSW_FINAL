from bangtal import Object

class User(Object):
    def __init__(self, image, scene):
        super().__init__(image)
        self.image = image
        self.scene = scene
        self.x = 100
        self.y = 45
        self.up_velocity = 0

