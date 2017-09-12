import Basic
import Platforms
import Objects
import Draw
import random
import time
import pygame


class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 64
        height = 64
        self.image = pygame.Surface([width, height])
        
        self.enemy_limit = 0

        #self.texture = pygame.image.load("Textures\\Panda.png")
        #self.texture = pygame.transform.scale(self.texture, (52, 62))

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
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None

        self.bar = Health()
        self.lives = 200

        self.back = 0

        self.money = False

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)
        
        # Move left/right
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
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
        for block in block_hit_list:
            self.back = 0
            self.enemy_limit = 0
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        """
        item_hit_list = pygame.sprite.spritecollide(self, self.level.pickup_list, False)
        for item in item_hit_list:
            item.pickup()"""

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

        # Move up/down
        self.rect.y += self.change_y

        if self.back > 0:
            self.back -= 1
            self.rect.x += self.back
        elif self.back < 0:
            self.back += 1
            self.rect.x += self.back
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
        for block in block_hit_list:
            self.back = 0
            
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.enemy_limit = 0
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
            if isinstance(block, Platforms.MovingPlatform):
                self.rect.x += block.change_x
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35
 
        # See if we are on the ground.
        if self.rect.y >= Basic.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = Basic.SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= Basic.SCREEN_HEIGHT:
            pygame.mixer.Sound.play(self.jump_sound)
            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        #self.change_x = self.change_x - 1.5
        self.direction = False
        self.go = True
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        #self.change_x = self.change_x + 1.5
        self.direction = True
        self.go = True
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        #self.change_x = 0
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

        if self.lives < 200:
            pygame.draw.rect(self.image, Basic.GREEN, (self.lives + 1, 1, 200 - self.lives, 17))



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
        self.timer = 0
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

        if int(time.time() - self.timer) == 20 and self.die:
            self.die = False
            
            self.timer = 0
            self.pos()

    def pos(self):
        self.platform = self.level[random.choice([0, 1, 2, 3])]

        self.rect.x = (self.platform[2] + 1) + self.world_shift
        self.rect.y = (self.platform[3] - self.height)

    def dies(self):
        self.die = True
        

        self.timer = time.time()
        self.picture = 0

        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

    def attack(self, state):
        self.attack_frames = 6
        self.state = state

def gen_platforms(x):
    platforms = []

    y = random.randint(2, 4)
    widht = random.randint(2, 4)
    height = random.randint(1, 2)

    platforms.append([x, y, widht, height])

    coin = False
    for i in range(4):
        before = platforms[i]
        widht = random.randint(2, 4)
        if i % 2 == 0:
            x = before[0] + random.randint(int(before[2] / 2), before[2])
        else:
            x = before[0] - random.randint(int(widht / 2), widht)
        y = before[1] + random.randint(3, 4)
        height = random.randint(1, 2)

        if not coin:
            if random.randint(1, 3) == 1:
                coin = True

        platforms.append([x, y, widht, height])

    return platforms

class Level_():
    def __init__(self, player):
        self.platforms = pygame.sprite.Group() 
        self.monsters = pygame.sprite.Group()
        self.player = player

        coordinates = []

        for i in range(20):
            coordinates.append(gen_platforms(i*6))

        for i in coordinates:
            for j in i:
                platform = Platforms.Platform(j[2] * 32, j[3] * 32, False)
                platform.rect.x = j[0] * 32
                platform.rect.y = Basic.SCREEN_HEIGHT - j[1] * 32

                self.platforms.add(platform)

        self.world_shift = 0
        self.level_limit = -1000

    def shift_world(self, shift_x):

        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platforms:
            platform.rect.x += shift_x
 
        for enemy in self.monsters:
            enemy.rect.x += shift_x

        #for object in self.object_list:
        #    object.rect.x += shift_x

        #for item in self.pickup_list:
        #    item.rect.x += shift_x

        #self.coins.world_shift = self.world_shift

        
        for enemy in self.monsters:
            enemy.world_shift = self.world_shift

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.platforms.draw(screen)


class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.object_list = pygame.sprite.Group()
        self.pickup_list = pygame.sprite.Group()
        self.standed_list = pygame.sprite.Group()
        self.meny_list = pygame.sprite.Group()
        self.meny_list2 = pygame.sprite.Group()
        self.player = player
         
        # Background image
        self.tree_list = None
        self.tree_nr = None
        self.tree_now = None
        self.tree_block = None
     
        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000

        self.coins = Objects.coin()
        self.coins.world_shift = self.world_shift

        self.standed_list.add(self.coins.text)
        self.pickup_list.add(self.coins)

        self.health = Health()
        self.standed_list.add(self.health)

        self.backgorund = pygame.image.load("Textures\\Background.png")

        self.monster = Monster1()
        self.enemy_list.add(self.monster)

        for enemy in self.enemy_list:
            enemy.world_shift = self.world_shift

    
            
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.object_list.update()
        self.pickup_list.update()
        self.standed_list.update()

        if self.player.money:
            self.player.money = False
            self.coins.coin_counter += 5
            self.coins.updateing()
            

 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.object_list.draw(screen)
        self.pickup_list.draw(screen)
        self.standed_list.draw(screen)

    def draw2(self, screen):
        # Draw the background
        screen.blit(self.backgorund, (0, 0))
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything:
        """

        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for object in self.object_list:
            object.rect.x += shift_x

        for item in self.pickup_list:
            item.rect.x += shift_x

        self.coins.world_shift = self.world_shift

        
        for enemy in self.enemy_list:
            enemy.world_shift = self.world_shift
 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player, screen):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
        

        level = [
            [224, 64, 500, 500],
            [224, 64, 800, 400],
            [224, 64, 1000, 500],
            [224, 64, 1120, 280]
                ]
        #LevelMaker(player, screen, level)
        self.level_limit = 2400

        self.tree_list = [0, 1, 2, 3, 4]
        self.tree_nr = random.choice(self.tree_list)
        self.tree_now = 0
        self.tree_block = []
 
        # Array with width, height, x, and y of platform
        
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platforms.Platform(platform[0], platform[1], False)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Make a tree
        while not self.tree_now == self.tree_nr:
            tree_object = Objects.Tree() 
            self.tree_block = level[self.tree_now]

            tree_object.rect.x = self.tree_block[2]
            tree_object.rect.y = self.tree_block[3] - 200
            self.object_list.add(tree_object)

            self.tree_now = self.tree_now + 1

        # Make some text
        text = Draw.Text("CAVEMAN CITY ", 50)

        text.rect.x = 0
        text.rect.y = 0
        self.object_list.add(text)
 
        # Add a custom moving platform
        block = Platforms.MovingPlatform(64, 32, True)
        block.rect.x = 1345
        block.rect.y = 280
        block.boundary_left = 1345
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        self.coins.level = level
        self.coins.spawn()

        for enemy in self.enemy_list:
            enemy.level = level
            enemy.pos()

        self.standed_list.add(player.bar)



        

# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, screen):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = 1500


        self.tree_list = [0, 1, 2, 3, 4]
        self.tree_nr = random.choice(self.tree_list)
        self.tree_now = 0
        self.tree_block = []
 
        # Array with type of platform, and x, y location of the platform.
        level = [[224, 64, 500, 550],
                 [224, 64, 800, 400],
                 [224, 64, 1000, 500],
                 [224, 64, 1120, 280],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platforms.Platform(platform[0], platform[1], False)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Make a tree
        while not self.tree_now == self.tree_nr:
            tree_object = Objects.Tree()
            self.tree_block = level[self.tree_now]

            tree_object.rect.x = self.tree_block[2]
            tree_object.rect.y = self.tree_block[3] - 200
            self.object_list.add(tree_object)

            self.tree_now = self.tree_now + 1
 
        # Add a custom moving platform
        block = Platforms.MovingPlatform(64, 64, True)
        block.rect.x = 1450
        block.rect.y = 200
        block.boundary_top = 100
        block.boundary_bottom = 350
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)



class give_icon(pygame.sprite.Sprite):
    def __init__(self, images, widht, height, x, y):
        super().__init__()

        self.image = pygame.Surface((widht, height))
        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

        self.image.blit(pygame.transform.scale(images, (widht, height)), (0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def blits(self, images, widht, height):
        self.image.blit(pygame.transform.scale(images, (widht, height)), (0, 0))

    def tran(self):
        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

def main():
    """ Main Program """
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
 
    size = [Basic.SCREEN_WIDTH, Basic.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("CAVEMAN CITY!")
 
    # Create the player
    player = Player()
    """
    # Create all the levels
    level_list = []
    level = [
            [224, 64, 500, 450, 550],
            [224, 64, 800, 350, 450],
            [224, 64, 1000, 450, 550],
            [224, 64, 1120, 230, 330],
                ]
    level_list.append(Level_01(player, screen))

    level_list.append(Level_02(player, screen))
    """
    level = Level_(player)
    # Set the current level
    #current_level_no = 0
    #current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = level
 
    player.rect.x = 340
    player.rect.y = Basic.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    state = "start"
    now = True
    press = False

    
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    #active_sprite_list.update()

    
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

                    #if event.key == pygame.K_ESCAPE:
                    #    now = True
                    #    state = "resume"
            

        # Update items in the level
        #current_level.update()

        # Update the player.
        active_sprite_list.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= (Basic.SCREEN_WIDTH - 200):
            diff = player.rect.right - (Basic.SCREEN_WIDTH - 200)
            player.rect.right = (Basic.SCREEN_WIDTH - 200)
            level.shift_world(-diff)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 200:
            diff = 200 - player.rect.left
            player.rect.left = 200
            level.shift_world(diff)
        
        """ 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x - current_level.world_shift
        if current_position > current_level.level_limit:
            if current_level_no < len(level_list)-1:
                player.rect.x = 200
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else:
                # Out of levels. This just exits the program.
                # You'll want to do something better.
                done = True

        if current_position < -300:
            if current_level_no > 0:
                player.rect.x = (Basic.SCREEN_WIDTH - 300)
                current_level_no -= 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else:
                done = True
        """

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        level.draw(screen)
        active_sprite_list.draw(screen)
        #current_level.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        """
        if state == "start" or state == "resume":
            screen.fill(Basic.BLUE)
            


            if now:

                if state == "start":
                    bot = Objects.bottun((Basic.SCREEN_WIDTH / 2) - 200, (Basic.SCREEN_HEIGHT / 2) - 50, (255, 255, 255), (1, 1, 1), 400, 100)
                elif state == "resume":
                    bot = Objects.bottun((Basic.SCREEN_WIDTH / 2) - 240, (Basic.SCREEN_HEIGHT / 2) - 50, (255, 255, 255), (1, 1, 1), 480, 100)
                bot2 = Objects.bottun(0, 0, (255, 255, 255), (1, 1, 1), 80, 100)

                if state == "start":
                    text = Draw.Text("START  ", 84, 500, 84)
                    text.rect.x = ((Basic.SCREEN_WIDTH / 2) + 2) - 193
                    text.rect.y = ((Basic.SCREEN_HEIGHT / 2) + 5) - 43
                    
                elif state == "resume":
                    text.text_counter("RESUME")
                    text.rect.x = ((Basic.SCREEN_WIDTH / 2) + 2) - 228
                    text.rect.y = ((Basic.SCREEN_HEIGHT / 2) + 5) - 43

                man = give_icon(player.left_texture[0], 93, 93, -5, 7)
                

                
                
                current_level.meny_list2.add(bot)
                current_level.meny_list.add(text)
                
                
                current_level.meny_list2.add(bot2)
                current_level.meny_list.add(man)
                

                

                now = False

            current_level.meny_list2.update()
            current_level.meny_list.update()
            current_level.meny_list2.draw(screen)
            current_level.meny_list.draw(screen)

            if bot.clicks:
                state = "game"

            if bot2.clicks:
                if not press:
                    player.switch()
                    press = True
            else:
                press = False

            if player.extra == 1:
                man.tran()
                man.blits(player.left_texture[0], 93, 93)
            elif player.extra == 2:
                man.blits(player.left_texture2[0], 93, 93)
            elif player.extra == 3:
                man.blits(player.left_texture3[0], 93, 93)
        """
                    
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()