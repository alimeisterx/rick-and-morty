import pygame
import random
import image
from settings import *
from morty import Morty
rickImgs = ['assets/images/rick/sad_rick.png', 'assets/images/rick/asleep_rick.png', 'assets/images/rick/pickle_rick.png']
class Rick(Morty):
    def __init__(self):
        random_size_value = random.uniform(RICK_SIZE_RANDOMIZE[0], RICK_SIZE_RANDOMIZE[1])
        size = (int(RICKS_SIZES[0] * random_size_value), int(RICKS_SIZES[1] * random_size_value))
        moving_direction, start_pos = self.define_spawn_pos(size)
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.2, size[1]//1.2)
        rickImg = random.choice(rickImgs)
        self.images = [image.load(rickImg, size=size, flip=moving_direction=="right") for nb in range(1, 10)] # load the images
        self.current_frame = 0
        self.animation_timer = 0
    def kill(self, rick): # remove rick from the list
        rick.remove(self)
        return -RICK_PENALITY
