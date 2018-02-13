import pygame
import random
import time
import Basic
import Draw

class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = 40
        height = 40
        self.visible = True
        self.level = []
        self.picknow = False

        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        
        self.Coin = []
        self.teller = 0
        self.Coinsheet = Basic.SpriteSheet("Textures\\coins.png")

        self.sound = pygame.mixer.Sound("Textures\\Pickup_Coin.wav")

        self.Coin.append(self.Coinsheet.get_image(0, 0, 40, 40))
        self.Coin.append(self.Coinsheet.get_image(0, 43, 40, 40))
        self.Coin.append(self.Coinsheet.get_image(0, 88, 40, 40))
        self.Coin.append(self.Coinsheet.get_image(0, 133, 40, 40))

        self.Coin.append(pygame.transform.flip(self.Coin[2], True, False))
        self.Coin.append(pygame.transform.flip(self.Coin[1], True, False))

    def update(self):
        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

        if self.visible:
            self.image.blit(self.Coin[int(self.teller)], (0, 0))
            self.teller += 0.2

        if int(self.teller) == 6:
            self.teller = 0

        if self.picknow:
            self.picknow = False
            return True
        return False

    def pickup(self):
        if self.visible:
            pygame.mixer.Sound.play(self.sound)
            self.visible = False
            self.picknow = True

class Tree(pygame.sprite.Sprite):
    def __init__(self):
                
        super().__init__()
        self.texture2 = pygame.image.load("Textures\\tree.png")
        self.texture2 = pygame.transform.scale(self.texture2, (160, 226))

        self.image = pygame.Surface([160, 200])
        self.image.blit(self.texture2, (0,0), (0, 0, 160, 200))
        self.image.set_colorkey(Basic.BLACK)

        self.rect = self.image.get_rect()

class Bottun(pygame.sprite.Sprite):
    def __init__(self, x, y, color, color2, widht, height):
        super().__init__()

        self.color = color
        self.color2 = color2
        self.widht = widht
        self.height = height
        self.x = x
        self.y = y

        self.clicks = False
        self.over = False

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (self.x + self.widht > mouse[0] and mouse[0] > self.x) and (self.height + self.y > mouse[1] and mouse[1] > self.y):
            self.over = True
            if click[0] == 1:
                self.clicks = True
            else:
                self.clicks = False
        else:
            self.over = False

    def show(self, surface):
        if self.over:
            pygame.draw.rect(surface, self.color2, (self.x, self.y, self.widht, self.height))
        else:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.widht, self.height))

    def change(self, x, y, color, color2, widht, height):
        self.color = color
        self.color2 = color2
        self.widht = widht
        self.height = height
        self.x = x
        self.y = y

        self.clicks = False
        self.over = False

class Flag(pygame.sprite.Sprite):
    def __init__(self, x):

        super().__init__()

        self.flag = pygame.image.load("Textures\\flag.png")
        self.image = pygame.Surface((36, 77))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = Basic.SCREEN_HEIGHT - 77

        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

        self.image.blit(self.flag, (0, 0), (1, 3, 36, 77))        