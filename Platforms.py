import pygame
import Basic

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height, moving):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
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
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
 
        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1