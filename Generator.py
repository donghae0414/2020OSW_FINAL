from Models.RedMan import *

class Generator:

    num_of_enemy = 0

    def __init__(self, scene, user):
        self.scene = scene
        self.user = user

    # example ���� ����
    def create_redman(self):
        redman = RedMan(self.scene, 1280, 45, 0, 0, 15, self.user, 'Images/character/enemy/redman.png')
        redman.locate(self.scene, redman.x, redman.y)
        redman.setScale(0.6)
        redman.show()