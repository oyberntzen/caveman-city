import pygame
import Basic
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self, platform):

        super().__init__()

        
        self.monster = Basic.SpriteSheet("Textures//monster.png")

        self.widht = 64
        self.height = 72

        self.image = pygame.Surface((self.widht, self.height))

        self.rect = self.image.get_rect()

        self.change_x = random.randint(5, 20) / 5

        self.lifes = 3

        self.go_texture = []
        self.die_texture = []
        self.attack_texture = []
        self.stand_texture = []

        self.go_texture.append(pygame.transform.scale(self.monster.get_image(19, 82, 32, 36), (self.widht, self.height)))
        self.go_texture.append(pygame.transform.scale(self.monster.get_image(85, 82, 32, 36), (self.widht, self.height)))
        self.go_texture.append(pygame.transform.scale(self.monster.get_image(148, 82, 32, 36), (self.widht, self.height)))
        self.go_texture.append(pygame.transform.scale(self.monster.get_image(212, 82, 32, 36), (self.widht, self.height)))
        self.go_texture.append(pygame.transform.scale(self.monster.get_image(276, 82, 32, 36), (self.widht, self.height)))

        self.die_texture.append(pygame.transform.scale(self.monster.get_image(19, 210, 32, 36), (self.widht, self.height)))
        self.die_texture.append(pygame.transform.scale(self.monster.get_image(81, 210, 32, 36), (self.widht, self.height)))
        self.die_texture.append(pygame.transform.scale(self.monster.get_image(143, 210, 32, 36), (self.widht, self.height)))
        self.die_texture.append(pygame.transform.scale(self.monster.get_image(206, 210, 32, 36), (self.widht, self.height)))
        self.die_texture.append(pygame.transform.scale(self.monster.get_image(271, 210, 32, 36), (self.widht, self.height)))
        self.die_texture.append(pygame.transform.scale(self.monster.get_image(343, 210, 32, 36), (self.widht, self.height)))
        self.die_texture.append(pygame.transform.scale(self.monster.get_image(412, 210, 32, 36), (self.widht, self.height)))

        self.attack_texture.append(pygame.transform.scale(self.monster.get_image(19, 146, 32, 36), (self.widht, self.height)))
        self.attack_texture.append(pygame.transform.scale(self.monster.get_image(83, 146, 32, 36), (self.widht, self.height)))
        self.attack_texture.append(pygame.transform.scale(self.monster.get_image(148, 146, 32, 36), (self.widht, self.height)))
        self.attack_texture.append(pygame.transform.scale(self.monster.get_image(212, 146, 32, 36), (self.widht, self.height)))
        self.attack_texture.append(pygame.transform.scale(self.monster.get_image(276, 146, 32, 36), (self.widht, self.height)))
        self.attack_texture.append(pygame.transform.scale(self.monster.get_image(339, 146, 32, 36), (self.widht, self.height)))
        
        self.stand_texture.append(pygame.transform.scale(self.monster.get_image(19, 18, 32, 36), (self.widht, self.height)))
        self.stand_texture.append(pygame.transform.scale(self.monster.get_image(83, 18, 32, 36), (self.widht, self.height)))
        self.stand_texture.append(pygame.transform.scale(self.monster.get_image(148, 18, 32, 36), (self.widht, self.height)))
        self.stand_texture.append(pygame.transform.scale(self.monster.get_image(212, 18, 32, 36), (self.widht, self.height)))

        self.dir = "right"

        self.platform = platform

        self.go_frames = random.randint(0, 4)

        self.shift_x = 0

        self.live = True

        self.attack_f = 0
        self.die_f = 0

        self.dir = False

        self.Attack = False
        self.Die = False

    def set_pos(self):
        self.rect.x = self.platform[0]
        self.rect.y = self.platform[1] - self.height

    def update(self):
        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

        if self.live:
            self.go_frames += 0.1
            if int(self.go_frames) >= 5:
                self.go_frames = 0

            if self.change_x > 0:
                if self.rect.x + self.widht >= self.platform[0] + self.platform[2] + self.shift_x:
                    self.change_x = -1

            if self.change_x < 0:
                if self.rect.x <= self.platform[0] + self.shift_x:
                    self.change_x = 1
        
            if self.platform[2] > 64:
                self.rect.x += self.change_x
            
            if int(self.attack_f) == 0:
                if int(self.die_f) == 0:
                    if self.platform[2] > 64:
                        self.image.blit(self.go_texture[int(self.go_frames)], (0, 0))
                    else:
                        if self.go_frames >= 4:
                            self.go_frames = 0
                        self.image.blit(self.stand_texture[int(self.go_frames)], (0, 0))

                else:
                    self.image.blit(self.die_texture[int(self.die_f)], (0, 0))
                    self.die_f += 0.1
                    if int(self.die_f) >= 3:
                        self.die_f = 0
            else:
                self.image.blit(pygame.transform.flip(self.attack_texture[int(self.attack_f)], self.dir, False), (0, 0))
                self.attack_f += 0.1
                if int(self.attack_f) >= 6:
                    self.attack_f = 0

        else:
            if int(self.die_f) > 0:
                self.image.blit(self.die_texture[int(self.die_f)], (0, 0))
                self.die_f += 0.1
                if self.die_f >= 7:
                    self.die_f = 0

    def hit(self):
        self.die_f = 1
        self.lifes -= 1

    def die(self):
        self.live = False
        self.die_f = 1
        self.Die = True

    def attack(self, dir):
        self.attack_f = 1
        self.dir = dir
        self.Attack = True

    def check_die(self):
        if self.Die:
            self.Die = False
            return True
        return False

    def check_attack(self):
        if self.Attack:
            self.Attack = False
            return True
        return False