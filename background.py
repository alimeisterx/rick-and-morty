import image
from settings import *
class Background:
    def __init__(self, imgPath):
        self.image = image.load(imgPath, size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                convert="default")


    def draw(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")
