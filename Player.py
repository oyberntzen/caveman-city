import pygame
import Basic
import Platforms

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

        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.monsters, False)
        for enemy in enemy_hit_list:
            if enemy.live:
                if self.rect.y + 50 < enemy.rect.y:
                    self.change_y = -10
                    enemy.hit()
                    pygame.mixer.Sound.play(self.punch_sound)
                    if enemy.lifes == 0:
                        pygame.mixer.Sound.play(self.die_sound)
                        enemy.die()
                        self.extra += 10
                else:
                    pygame.mixer.Sound.play(self.hit_sound)
                    dir = self.rect.x < enemy.rect.x
                    enemy.attack(dir)
                    self.extra -= 3
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
                    monster.lifes = 3
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

    def event(self, event):

        if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_a and self.change_x < 0 :
                    self.stop()
                if event.key == pygame.K_d and self.change_x > 0:
                    self.stop()

        if event.type == pygame.KEYDOWN:
                
            if event.key == pygame.K_a:
                self.go_left()
            else:
                if event.key == pygame.K_d:
                    self.go_right()

            if event.key == pygame.K_w:
                self.jump()