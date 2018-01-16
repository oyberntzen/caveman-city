import pygame
import Basic

class Platform(pygame.sprite.Sprite):
 
    def __init__(self, width, height, moving):
        super().__init__()

        self.texture = pygame.image.load("Textures\\sheet1.png")

        self.x = 0
        self.y = 0
 
        self.image = pygame.Surface([width, height])
        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

        self.block = (160, 0, 32, 32)

        while not self.y >= height:

            while not self.x >= width:
                if not moving:
                    if self.y == 0:
                        if self.x == 0:
                            self.block = (128, 0, 32, 32)

                        else:
                            if self.x >= width - 32:
                                self.block = (192, 0, 32, 32)

                            else:
                                self.block = (160, 0, 32, 32)

                    else:
                        self.block = (160, 32, 32, 32)
                else:
                    self.block = (96, 128, 32, 32)

                self.image.blit(self.texture, (self.x, self.y), self.block)
                self.x += 32

            self.y += 32
            self.x = 0
        
        self.rect = self.image.get_rect()
 
 
class MovingPlatform(Platform):
    change_x = 0
    change_y = 0
 
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
 
    player = None
 
    level = None

    block = (96, 128, 32, 32)
 
    def update(self):
        self.rect.x += self.change_x

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        self.rect.y += self.change_y

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, length):
        super().__init__()

        self.length = length

        spritesheet = pygame.image.load("Textures\\lava_spr_strip45.png")

        self.lava = pygame.surface.Surface((16, 16))

        self.images = []
        for i in range(45):
            self.lava.blit(spritesheet, (0, 0), (i * 16, 0, 16, 16))
            self.images.append(self.lava.copy())

        self.image = pygame.surface.Surface((length, 16))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = Basic.SCREEN_HEIGHT - 16

        self.counter = 0

        for i in range(int(self.length / 16)):
            self.image.blit(self.images[0], (i * 16, 0))
    
    def update(self):
        self.counter = self.counter + 0.3
        if self.counter >= 45:
            self.counter = 0
        for i in range(int(self.length / 16)):
            self.image.blit(self.images[int(self.counter)], (i * 16, 0))
        