import Basic
import Platforms
import Objects
import Draw
import random
import time
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
 
        super().__init__()

        width = 64
        height = 64
        self.image = pygame.Surface([width, height])
        
        self.enemy_limit = 0

        self.jump_sound = pygame.mixer.Sound("Textures\\Jump.wav")
        self.punch_sound = pygame.mixer.Sound("Textures\\punch.wav")
        self.die_sound = pygame.mixer.Sound("Textures\\Die.wav")
        self.hit_sound = pygame.mixer.Sound("Textures\\hit.wav")

        self.spritesheet = Basic.SpriteSheet("Textures\\spritesheet_caveman.png")

        self.left_texture = []

        self.left_texture.append(self.spritesheet.get_image(0, 0, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(32, 0, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(64, 0, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(96, 0, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(0, 32, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(32, 32, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(64, 32, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(96, 32, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(0, 64, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(32, 64, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(64, 64, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(96, 64, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(0, 96, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(32, 96, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(64, 64, 32, 32))
        self.left_texture.append(self.spritesheet.get_image(96, 96, 32, 32))


        self.spritesheet2 = Basic.SpriteSheet("Textures\\spritesheet_caveman2.png")

        self.left_texture2 = []

        self.left_texture2.append(self.spritesheet2.get_image(0, 0, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(32, 0, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(64, 0, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(96, 0, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(0, 32, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(32, 32, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(64, 32, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(96, 32, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(0, 64, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(32, 64, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(64, 64, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(96, 64, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(0, 96, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(32, 96, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(64, 64, 32, 32))
        self.left_texture2.append(self.spritesheet2.get_image(96, 96, 32, 32))


        self.spritesheet3 = Basic.SpriteSheet("Textures\\spritesheet_caveman3.png")

        self.left_texture3 = []

        self.left_texture3.append(self.spritesheet3.get_image(0, 0, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(32, 0, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(64, 0, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(96, 0, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(0, 32, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(32, 32, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(64, 32, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(96, 32, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(0, 64, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(32, 64, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(64, 64, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(96, 64, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(0, 96, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(32, 96, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(64, 64, 32, 32))
        self.left_texture3.append(self.spritesheet3.get_image(96, 96, 32, 32))

        self.extra = 1

        self.frame = 0

        self.image.set_colorkey(Basic.GREEN)

        self.direction = True
        self.go = False
 
        self.rect = self.image.get_rect()
 
        self.change_x = 0
        self.change_y = 0
 
        self.level = None

        self.back = 0

        self.done = False

        self.fire = False

    def update(self):

        self.calc_grav()

        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

        self.change_x = self.change_x * 0.9

        if self.change_x < 0:
            self.frame = self.frame + (self.change_x / -40)
        else:
            self.frame = self.frame + (self.change_x / 40)

        if self.change_x < 0.5 and self.change_x > -0.5:
            self.frame = 6
            self.change_x = 0

        if int(self.frame) > 15:
            self.frame = 0
            
        
        if self.go and not self.direction:
            self.change_x = self.change_x - 0.75

        if self.go and self.direction:
            self.change_x = self.change_x + 0.75

        if self.change_x < -2:
            self.rect.x += self.change_x
        else:
            if self.change_x > 2:
                self.rect.x += self.change_x

        if self.direction:
            self.image.blit(pygame.transform.scale(pygame.transform.flip(self.left_texture[int(self.frame)], True, False), (64, 64)), (0,0))
            if self.extra == 2:
                self.image.blit(pygame.transform.scale(pygame.transform.flip(self.left_texture2[int(self.frame)], True, False), (64, 64)), (0,0))
            elif self.extra == 3:
                self.image.blit(pygame.transform.scale(pygame.transform.flip(self.left_texture3[int(self.frame)], True, False), (64, 64)), (0,0))
        else:
            self.image.blit(pygame.transform.scale(self.left_texture[int(self.frame)], (64, 64)), (0,0))
            if self.extra == 2:
                self.image.blit(pygame.transform.scale(self.left_texture2[int(self.frame)], (64, 64)), (0,0))
            elif self.extra == 3:
                self.image.blit(pygame.transform.scale(self.left_texture3[int(self.frame)], (64, 64)), (0,0))         

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
        for block in block_hit_list:
            self.back = 0

            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
        
        coin_hit_list = pygame.sprite.spritecollide(self, self.level.coins, False)
        for coin in coin_hit_list:
            coin.pickup()

        flag_hit_list = pygame.sprite.spritecollide(self, self.level.objects, False)
        for i in flag_hit_list:
            self.done = True

        lava_hit_list = pygame.sprite.spritecollide(self, self.level.lavas, False)
        for i in lava_hit_list:
            self.fire = True
            self.change_y = -10
        """
        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.monsters, False)
        for enemy in enemy_hit_list:
            if not enemy.die:
                if self.change_y > 1:
                    self.change_y = -10
                    self.enemy_limit += 1
                    if self.enemy_limit < 3:
                        pygame.mixer.Sound.play(self.punch_sound)
                    else:
                        pygame.mixer.Sound.play(self.die_sound)
                elif not self.lives == 0:
                    self.lives -= 20
                    pygame.mixer.Sound.play(self.hit_sound)
                    if self.rect.x > enemy.rect.x:
                        enemy.attack(True)
                    else:
                        enemy.attack(False)

                    if self.rect.x > enemy.rect.x:
                        self.back = 15
                        self.change_y = -5
                    elif self.rect.x < enemy.rect.x:
                        self.back = -15
                        self.change_y = -5

                if self.enemy_limit == 3:
                    enemy.dies()
                    self.money = True

        self.bar.lives = self.lives
        """

        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.monsters, False)
        for enemy in enemy_hit_list:
            if enemy.live:
                if self.change_y > 1:
                    self.change_y = -10
                    enemy.lives -= 1
                    if enemy.lives == 0:
                        enemy.die()
                else:
                    if self.rect.x > enemy.rect.x:
                        self.back = 15
                        self.change_y = -5
                    elif self.rect.x < enemy.rect.x:
                        self.back = -15
                        self.change_y = -5

        self.rect.y += self.change_y

        if self.back > 0:
            self.back -= 1
            self.rect.x += self.back
        elif self.back < 0:
            self.back += 1
            self.rect.x += self.back

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
        for block in block_hit_list:
            self.back = 0

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                for monster in self.level.monsters:
                    monster.lives = 3
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0
 
            if isinstance(block, Platforms.MovingPlatform):
                self.rect.x += block.change_x
 
    def calc_grav(self):

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

        if self.rect.y >= Basic.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = Basic.SCREEN_HEIGHT - self.rect.height
        elif self.rect.y <= 0:
            self.rect.top = 0
 
    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= Basic.SCREEN_HEIGHT:
            pygame.mixer.Sound.play(self.jump_sound)
            self.change_y = -10

    def go_left(self):

        self.direction = False
        self.go = True
 
    def go_right(self):

        self.direction = True
        self.go = True
 
    def stop(self):

        self.go = False

    def switch(self):

        self.extra += 1
        if self.extra == 4:
            self.extra = 1

class Health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.spritesheet = Basic.SpriteSheet("Textures\\Health.png")
        self.image = pygame.Surface((202, 19))
        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

        self.list = []

        self.lives = 0

        self.rect = self.image.get_rect()

        self.list.append(pygame.transform.scale(self.spritesheet.get_image(0, 0, 182, 17), (202, 19)))

        self.rect.x = Basic.SCREEN_WIDTH - 202
        self.rect.y = Basic.SCREEN_HEIGHT - 19

        self.image.blit(self.list[0], (0, 0))

    def update(self):
        self.image.blit(self.list[0], (0, 0))

"""
class Monster1(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        
        self.monster = Basic.SpriteSheet("Textures//monster.png")

        self.widht = 64
        self.height = 72

        self.image = pygame.Surface((self.widht, self.height))

        self.rect = self.image.get_rect()

        self.go_texture = []
        self.die_texture = []
        self.attack_texture = []

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
        

        self.direction = True

        self.frames = 0.0

        self.rect.x = 0
        self.rect.y = 0

        self.level = []
        self.world_shift = 0
        
        self.die = False
        self.picture = 0
    
        self.attack_frames = 0
        self.state = False

    def update(self):
        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)
        
        if not self.die:
        
            if self.direction:
                self.image.blit(self.go_texture[int(self.frames)], (0, 0))
            else:
                self.image.blit(pygame.transform.flip(self.go_texture[int(self.frames)], True, False), (0, 0))

            self.frames += 0.08

            if int(self.frames) == 4:
                self.frames = 0.0

            if int(self.attack_frames) == 0:
                if self.direction:
                    self.rect.x += 1
                else:
                    self.rect.x -= 1
            else:
                self.attack_frames -= 0.1

                self.image.fill(Basic.GREEN)
                self.image.set_colorkey(Basic.GREEN)
                if self.state:
                    self.image.blit(self.attack_texture[int(self.attack_frames)], (0, 0))
                else:
                    self.image.blit(pygame.transform.flip(self.attack_texture[int(self.attack_frames)], True, False), (0, 0))

            if self.direction and ((self.platform[0] + self.platform[2]) - self.widht) + self.world_shift == self.rect.x:
                self.direction = False
            elif not self.direction and self.platform[2] + self.world_shift == self.rect.x:
                self.direction = True

        if self.die and int(self.picture) < 7:
            self.image.blit(self.die_texture[int(self.picture)], (0, 0))
            self.picture += 0.2

    def dies(self):
        self.die = True
        
        self.picture = 0

        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

    def attack(self, state):
        self.attack_frames = 6
        self.state = state
"""

class Monster(pygame.sprite.Sprite):
    def __init__(self, platform):

        super().__init__()

        
        self.monster = Basic.SpriteSheet("Textures//monster.png")

        self.widht = 64
        self.height = 72

        self.image = pygame.Surface((self.widht, self.height))

        self.rect = self.image.get_rect()

        self.change_x = random.randint(5, 20) / 5

        self.lives = 3

        self.go_texture = []
        self.die_texture = []
        self.attack_texture = []

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
        
        self.dir = "right"

        self.platform = platform

        self.go_frames = random.randint(0, 4)

        self.shift_x = 0

        self.live = True

    def set_pos(self):
        self.rect.x = self.platform[0]
        self.rect.y = self.platform[1] - self.height

    def update(self):
        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

        if self.live:
            if self.platform[2] > 64:
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
        
            self.image.blit(self.go_texture[int(self.go_frames)], (0, 0))

    def die(self):
        self.live = False
        print(self.live)

def gen_platforms(x):
    platforms = []

    y = random.randint(2, 4)
    widht = random.randint(2, 4)
    height = random.randint(1, 2)

    platforms.append([x, y, widht, height, 10, random.randint(0, 10)])

    for i in range(4):
        before = platforms[i]
        widht = random.randint(2, 4)

        if before[5] == 0:
            place = True
        else:
            place = True

        if i % 2 == 0:
            if place:
                x = before[0] + before[2]
            else:
                x = before[0] + random.randint(int(before[2] / 2), before[2])
        else:
            if place:
                x = before[0] - widht
            else:
                x = before[0] - random.randint(int(widht / 2), widht)
            
        y = before[1] + 4
        if place:
            height = 1
        else:
            height = random.randint(1, 2)

        platforms.append([x, y, widht, height, random.randint(0, 5), random.randint(0, 10)])

    return platforms

class Level(): 
    def __init__(self, player):
        self.platforms = pygame.sprite.Group() 
        self.monsters = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.texts = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        self.lavas = pygame.sprite.Group()
        self.player = player

        coordinates = []

        offset = 512

        for i in range(20):
            coordinates.append(gen_platforms(i*8))

        for i in coordinates:
            for j in i:
                platform = Platforms.Platform(j[2] * 32, j[3] * 32, False)
                platform.rect.x = j[0] * 32 + offset
                platform.rect.y = Basic.SCREEN_HEIGHT - j[1] * 32

                self.platforms.add(platform)

                if j[5] == 0:
                    monster = Monster([j[0] * 32 + offset, Basic.SCREEN_HEIGHT - j[1] * 32, j[2] * 32, j[3] * 32])
                    monster.set_pos()
                    self.monsters.add(monster)

                if j[4] == 0:
                    coin = Objects.coin()
                    coin.rect.x = j[0] * 32 + offset
                    coin.rect.y = (Basic.SCREEN_HEIGHT - j[1] * 32) - 40
                    self.coins.add(coin)

        platform = Platforms.Platform(64, Basic.SCREEN_HEIGHT, False)
        platform.rect.x = 0
        platform.rect.y = 0

        

        self.platforms.add(platform)

        self.end_point = 20 * 32 * 8 + offset * 2

        self.flag = Objects.Flag(self.end_point)
        self.objects.add(self.flag)

        lava = Platforms.Lava(offset + 64, 20 * 8 * 32 - 64)
        self.lavas.add(lava)

        self.world_shift = 0
        self.level_limit = -1000

        self.counter = 0

    def shift_world(self, shift_x):
        self.world_shift += shift_x

        for platform in self.platforms:
            platform.rect.x += shift_x
 
        for enemy in self.monsters:
            enemy.rect.x += shift_x
            enemy.shift_x = self.world_shift

        for coin in self.coins:
            coin.rect.x += shift_x

        for object in self.objects:
            object.rect.x += shift_x

        for lava in self.lavas:
            lava.rect.x += shift_x

    def draw(self, screen):
        self.platforms.draw(screen)
        self.coins.draw(screen)
        self.texts.draw(screen)
        self.objects.draw(screen)
        self.lavas.draw(screen)
        self.monsters.draw(screen)
        

    def update(self):
        self.texts.update()
        self.lavas.update()
        self.monsters.update()
        for coin in self.coins:
            if coin.update():
                self.counter = self.counter + 1

def main():

    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
 
    size = [Basic.SCREEN_WIDTH, Basic.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    background = pygame.image.load("Textures\\background.png")
 
    pygame.display.set_caption("CAVEMAN CITY!")

    player = Player()

    level = Level(player)
 
    active_sprite_list = pygame.sprite.Group()
    player.level = level
 
    player.rect.x = 340
    player.rect.y = Basic.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    text = Draw.Text("TIME: 0.000", 50)
    text.rect.x = 0
    text.rect.y = 0
    level.texts.add(text)

    start_time = time.time()

    state = "start"
    now = True
    press = False

    done = False

    clock = pygame.time.Clock()

    ekstra_time = 0
    fire_time = 0
    splash = pygame.mixer.Sound("Textures\\lava.wav")

    Time = 60

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_a and player.change_x < 0 :
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_a:
                    player.go_left()
                else:
                    if event.key == pygame.K_d:
                        player.go_right()

                if event.key == pygame.K_w:
                    player.jump()          

        screen.blit(background, (0, 0))

        level.update()

        active_sprite_list.update()

        now_time = time.time()

        if player.fire:
            player.fire = False
            pygame.mixer.Sound.play(splash)
            ekstra_time += 5
            

        if not player.done:
            Time = int(60 - (now_time - start_time - level.counter * 5 + ekstra_time))
            text.text_counter("TIME: " + str(Time))

        if player.rect.right >= (Basic.SCREEN_WIDTH - 200):
            diff = player.rect.right - (Basic.SCREEN_WIDTH - 200)
            player.rect.right = (Basic.SCREEN_WIDTH - 200)
            level.shift_world(-diff)

        if player.rect.left <= 200:
            diff = 200 - player.rect.left
            player.rect.left = 200
            level.shift_world(diff)

        level.draw(screen)
        active_sprite_list.draw(screen)
                    
        clock.tick(60)

        pygame.display.flip()

    pygame.quit()
 
if __name__ == "__main__":
    main()