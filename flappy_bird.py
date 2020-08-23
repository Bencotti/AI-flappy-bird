import pygame
import neat
import time
import os
import random

WIN_WIDTH = 900
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("..","imgs","bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("..","imgs","bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("..","imgs","bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("..","imgs","pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("..","imgs","base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("..","imgs","bg.png")))

#Bird class 
class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self. height = self.y
        self.img_count = 0
        self.img = self.IMG[0]
    
    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        # making the arc for jump, d for displacement
        d = self.val * self.tick_count + 1.5 * self.tick_count ** 2
        
        # terminal velocity, max drop speed
        if d >= 16:
            d = 16

        # variable hight jump   
        if d < 0:
            d -= 2

        # gradual increase in movement
        self.y = self.y + d

        #tilting (moving upwards)
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
    
    def draw(self, win):
        self.img_count += 1

        # flappping wings
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # check dropping bird, no flap