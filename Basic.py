import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN_rare = (111, 109, 81)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.fill(GREEN)
        image.set_colorkey(GREEN)

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey((255, 174, 201))

        return image