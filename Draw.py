import pygame
import Basic

class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, widht = 0, height = 0):
        super().__init__()
        self.texts = text
        self.sizes = size

        self.Alphabet = {}

        self.Alphabet["A"] = [1, 27, 7, 9]   #A
        self.Alphabet["B"] = [9, 27, 7, 9]   #B
        self.Alphabet["C"] = [17, 27, 7, 9]  #C
        self.Alphabet["D"] = [25, 27, 7, 9]  #D
        self.Alphabet["E"] = [33, 27, 7, 9]  #E
        self.Alphabet["F"] = [41, 27, 7, 9]  #F
        self.Alphabet["G"] = [49, 27, 7, 9]  #G
        self.Alphabet["H"] = [57, 27, 7, 9]  #H
        self.Alphabet["I"] = [65, 27, 4, 9]  #I
        self.Alphabet["J"] = [70, 27, 7, 9]  #J
        self.Alphabet["K"] = [78, 27, 7, 9]  #K
        self.Alphabet["L"] = [86, 27, 7, 9]  #L
        self.Alphabet["M"] = [94, 27, 9, 9]  #M
        self.Alphabet["N"] = [1, 36, 8, 9]   #N
        self.Alphabet["O"] = [10, 36, 7, 9]  #O
        self.Alphabet["P"] = [18, 36, 7, 9]  #P
        self.Alphabet["Q"] = [26, 36, 8, 9]  #Q
        self.Alphabet["R"] = [35, 36, 7, 9]  #R
        self.Alphabet["S"] = [43, 36, 7, 9]  #S
        self.Alphabet["T"] = [51, 36, 8, 9]  #T
        self.Alphabet["U"] = [60, 36, 7, 9]  #U
        self.Alphabet["V"] = [68, 36, 7, 9]  #V
        self.Alphabet["W"] = [76, 36, 9, 9]  #W
        self.Alphabet["X"] = [86, 36, 7, 9]  #X
        self.Alphabet["Y"] = [94, 36, 8, 9]  #Y
        self.Alphabet["Z"] = [103, 36, 7, 9] #Z
        self.Alphabet[" "] = [50, 18, 9, 9]  #Space

        self.Alphabet["0"] = [1, 9, 7, 9]    #0
        self.Alphabet["1"] = [9, 9, 4, 9]    #1
        self.Alphabet["2"] = [14, 9, 7, 9]   #2
        self.Alphabet["3"] = [22, 9, 7, 9]   #3
        self.Alphabet["4"] = [30, 9, 7, 9]   #4
        self.Alphabet["5"] = [38, 9, 7, 9]   #5
        self.Alphabet["6"] = [46, 9, 7, 9]   #6
        self.Alphabet["7"] = [54, 9, 7, 9]   #7
        self.Alphabet["8"] = [62, 9, 7, 9]   #8
        self.Alphabet["9"] = [70, 9, 7, 9]   #9

        self.Alphabet[":"] = [1, 18, 4, 8]

        self.lenght = len(text)
        self.width = 0
        
        self.getImage = pygame.Surface((self.lenght * 9, 9))
        if widht == 0 and height == 0:
            self.image = pygame.Surface((self.lenght * size, size))
        else:
            self.image = pygame.Surface((widht, height))
        self.char_texture = pygame.image.load("Textures\\boxy_bold_font.png")

        self.rect = self.image.get_rect()

        self.char_now = 0

        self.check_now = None
        self.check_before = None

        self.x_now = 0
        self.x_before = 0

        self.getImage.fill(Basic.GREEN)

        


        self.image.blit(pygame.transform.scale(self.getImage, (self.lenght * self.sizes, self.sizes)), (0, 0))
        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

        for char in self.texts:
            self.check_now = self.Alphabet[char]

            if self.char_now == 0:
                self.x_now = 0

            else:
                self.x_now = self.x_before + (self.check_before[2] + 1)

            self.getImage.blit(self.char_texture, (self.x_now, 0), self.check_now)
                
            self.check_before = self.check_now
            self.x_before = self.x_now
            self.char_now += 1

        self.image.blit(pygame.transform.scale(self.getImage, (self.lenght * self.sizes, self.sizes)), (0, 0))

    def text_counter(self, new_text):
        self.texts = new_text
        self.image.fill(Basic.GREEN)
        self.image.set_colorkey(Basic.GREEN)

        self.getImage.fill(Basic.GREEN)
        self.getImage.set_colorkey(Basic.GREEN)

        self.char_now = 0

        self.check_now = None
        self.check_before = None

        self.x_now = 0
        self.x_before = 0

        for char in self.texts:
            self.check_now = self.Alphabet[char]

            if self.char_now == 0:
                self.x_now = 0

            else:
                self.x_now = self.x_before + (self.check_before[2] + 1)

            self.getImage.blit(self.char_texture, (self.x_now, 0), self.check_now)
                
            self.check_before = self.check_now
            self.x_before = self.x_now
            self.char_now += 1

        self.image.blit(pygame.transform.scale(self.getImage, (self.lenght * self.sizes, self.sizes)), (0, 0))