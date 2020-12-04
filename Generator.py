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
    velocity = 10

    def __init__(self, scene, user):
        self.scene = scene
        self.user = user
        self.timer = GeneratorTimer(0.01, self)
        self.timer.start()

    def create_redman(self, velocity):
        random_scale = random.randrange(5, 9) / 10
        redman = RedMan(self.scene, 1280, 200, 250, 250, velocity, self.user, 'Images/character/enemy/redman.png', scale=random_scale)
        redman.locate(self.scene, redman.x, redman.y)
        redman.show()

    def create_pig(self, velocity):
        random_scale = random.randrange(4, 7) / 10
        pig = Pig(self.scene, 1280, 45, 300, 262, velocity + 5, self.user, 'Images/character/enemy/pig.png', scale=random_scale)
        pig.locate(self.scene, pig.x, pig.y)
        pig.show()

    def create_turtle(self, velocity):
        random_scale = random.randrange(5, 8) / 10
        turtle = Turtle(self.scene, 1280, 45, 300, 252, velocity - 5, self.user, 'Images/character/enemy/turtle.png', scale=random_scale)
        turtle.locate(self.scene, turtle.x, turtle.y)
        turtle.show()

    def create_bird(self, velocity):
        random_scale = random.randrange(5, 8) / 10
        random_y = random.randrange(440, 500)
        bird = Bird(self.scene, 1280, random_y, 300, 237, velocity, self.user, 'Images/character/enemy/bird.png', scale=random_scale)
        bird.locate(self.scene, bird.x, bird.y)
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

        val = (self.generator.velocity - 10) / 10

        if now > 2 - val :
            self.lock.acquire()
            self.st = time.time()
            
            self.random_choose_character()
            
            self.lock.release()
                    
        #self.set(0.01)
        self.start()

    def random_choose_character(self):
        case = random.randint(0, self.character_num - 1)

        #velocity = 10 #TODO 변수화 되어야함, 시간에 따른 & 생성시간도 단축하면 좋음

        if case == 0:
            self.generator.create_redman(self.generator.velocity)
        elif case == 1:
            self.generator.create_pig(self.generator.velocity)
        elif case == 2:
            self.generator.create_turtle(self.generator.velocity)
        elif case == 3:
            self.generator.create_bird(self.generator.velocity)
        else:
            pass