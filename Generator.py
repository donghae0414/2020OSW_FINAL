from Models.RedMan import *
from Models.Pig import *
from Models.Turtle import *
from Models.Bird import *

from bangtal import Object
import time
import threading
import random

class Generator(Object):

    num_of_enemy = 0

    def __init__(self, scene, user):
        self.scene = scene
        self.user = user
        self.timer = GeneratorTimer(0.01, self)
        self.timer.start()

    def create_redman(self):
        redman = RedMan(self.scene, 1280, 45, 0, 0, 15, self.user, 'Images/character/enemy/redman.png')
        redman.locate(self.scene, redman.x, redman.y)
        redman.setScale(0.6)
        redman.show()

    def create_pig(self):
        pig = Pig(self.scene, 1280, 45, 0, 0, 10, self.user, 'Images/character/enemy/pig.png')
        pig.locate(self.scene, pig.x, pig.y)
        pig.setScale(0.6)
        pig.show()

    def create_turtle(self):
        turtle = Turtle(self.scene, 1280, 45, 0, 0, 10, self.user, 'Images/character/enemy/turtle.png')
        turtle.locate(self.scene, turtle.x, turtle.y)
        turtle.setScale(0.6)
        turtle.show()

    def create_bird(self):
        bird = Bird(self.scene, 1280, 400, 0, 0, 10, self.user, 'Images/character/enemy/bird.png')
        bird.locate(self.scene, bird.x, bird.y)
        bird.setScale(0.6)
        bird.show()


class GeneratorTimer(Timer):
    def __init__(self, seconds, generator):
        super().__init__(seconds)
        self.generator = generator
        self.seconds = seconds
        self.st = time.time()
        self.lock = threading.Lock()

        self.character_num = 4

    def onTimeout(self):
        now = time.time() - self.st

        #print(now)
        if now > 2 :
            self.lock.acquire()
            self.st = time.time()
            
            self.random_choose_character()
            
            self.lock.release()
            
        #print(self.user.x, self.user.y)
        
        #self.set(0.01)
        self.start()

    def random_choose_character(self):
        case = random.randint(0, self.character_num - 1)
        if case == 0:
            self.generator.create_redman()
        elif case == 1:
            self.generator.create_pig()
        elif case == 2:
            self.generator.create_turtle()
        elif case == 3:
            self.generator.create_bird()
        else:
            pass