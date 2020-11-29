from Models.RedMan import *
from bangtal import Object
import time
import threading

class Generator(Object):

    num_of_enemy = 0

    def __init__(self, scene, user):
        self.scene = scene
        self.user = user
        self.timer = GeneratorTimer(0.01, self)
        self.timer.start()
    # example ���� ����
    def create_redman(self):
        redman = RedMan(self.scene, 1280, 45, 0, 0, 15, self.user, 'Images/character/enemy/redman.png')
        redman.locate(self.scene, redman.x, redman.y)
        redman.setScale(0.6)
        redman.show()


 

class GeneratorTimer(Timer):
    def __init__(self, seconds, generator):
        super().__init__(seconds)
        self.generator = generator
        self.seconds = seconds
        self.st = time.time()
        self.lock = threading.Lock()
    def onTimeout(self):
        now = time.time() - self.st

        print(now)
        if now > 2 :
            self.lock.acquire()
            self.st = time.time()
            self.generator.create_redman()
            self.lock.release()
            
        #print(self.user.x, self.user.y)
        
        #self.set(0.01)
        self.start()