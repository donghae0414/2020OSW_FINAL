from Models.RedMan import *
from Models.Pig import *
from Models.Turtle import *
from Models.Bird import *
from Models.Life import *

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
        random_y = random.randrange(400, 480)
        bird = Bird(self.scene, 1280, random_y, 300, 237, velocity, self.user, 'Images/character/enemy/bird.png', scale=random_scale)
        bird.locate(self.scene, bird.x, bird.y)
        bird.show()

    def create_life(self, velocity):
        random_y = random.randrange(45, 500)
        life = Life(self.scene, 1280, random_y, 450, 450, velocity, self.user, 'Images/life.png', scale = 0.3)
        life.locate(self.scene, life.x, life.y)
        life.show()

class GeneratorTimer(Timer):
    def __init__(self, seconds, generator):
        super().__init__(seconds)
        self.generator = generator
        self.seconds = seconds
        self.st = time.time()
        self.lock = threading.Lock()

        self.character_num = 5

    def onTimeout(self):
        now = time.time() - self.st

        val = (self.generator.velocity - 10) / 10

        if now > max(2 - val, 0.2) :
            self.lock.acquire()
            self.st = time.time()
            
            self.random_choose_character()
            
            self.lock.release()
                    
        #self.set(0.01)
        self.start()

    def random_choose_character(self):
        case = random.randint(0, 13)

        if case == 0 or case == 5 or case == 9:
            self.generator.create_redman(self.generator.velocity)
        elif case == 1 or case == 6 or case == 10:
            self.generator.create_pig(self.generator.velocity)
        elif case == 2 or case == 7 or case == 11:
            self.generator.create_turtle(self.generator.velocity)
        elif case == 3 or case == 8 or case == 12:
            self.generator.create_bird(self.generator.velocity)
        elif case == 4:
            self.generator.create_life(self.generator.velocity)
        else:
            pass