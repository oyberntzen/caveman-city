import pygame
import random
import Objects
import Player
import Monster
import Basic
import Platforms
import time
import Draw

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
                x = before[0] + before[2] + 1
            else:
                x = before[0] + random.randint(int(before[2] / 2), before[2])
        else:
            if place:
                x = before[0] - widht - 1
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
    def __init__(self):
        self.platforms = pygame.sprite.Group() 
        self.monsters = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.texts = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        self.lavas = pygame.sprite.Group()

        self.player = Player.Player()
        self.player.level = self

        self.player.rect.x = 340
        self.player.rect.y = Basic.SCREEN_HEIGHT - self.player.rect.height

        self.text = Draw.Text("TIME: 0.000", 50)
        self.text.rect.x = 0
        self.text.rect.y = 0
        self.texts.add(self.text)

        self.splash = pygame.mixer.Sound("Textures\\lava.flac")

        self.state = "play"

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
                    monster = Monster.Monster([j[0] * 32 + offset, Basic.SCREEN_HEIGHT - j[1] * 32, j[2] * 32, j[3] * 32])
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

        lava = Platforms.Lava(offset - 32, 20 * 8 * 32 - 64)
        self.lavas.add(lava)

        self.world_shift = 0
        self.level_limit = -1000

        self.extra_time = 0
        self.start_time = time.time()

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
        screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        

    def update(self):
        self.texts.update()
        self.lavas.update()
        self.monsters.update()
        self.player.update()
        for coin in self.coins:
            if coin.update():
                self.extra_time += 5

        for monster in self.monsters:
            if monster.check_attack():
                self.extra_time -= 4
            elif monster.check_die():
                self.extra_time += 10

        if self.player.rect.right >= (Basic.SCREEN_WIDTH - 200):
            diff = self.player.rect.right - (Basic.SCREEN_WIDTH - 200)
            self.player.rect.right = (Basic.SCREEN_WIDTH - 200)
            self.shift_world(-diff)

        elif self.player.rect.left <= 200:
            diff = 200 - self.player.rect.left
            self.player.rect.left = 200
            self.shift_world(diff)

        if self.player.fire:
            self.player.fire = False
            pygame.mixer.Sound.play(self.splash)
            self.extra_time -= 5
        
        if not self.player.done:
            Time = int(60 - (time.time() - self.start_time - self.extra_time))
            self.text.text_counter("TIME: " + str(Time))
            if Time < 0:
                self.state = "lose"

        elif self.player.change_x == 0:
            self.state = "win"

    def event(self, event):
        if not self.player.done:
            self.player.event(event)