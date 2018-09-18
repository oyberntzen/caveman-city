import Draw
import Objects
import Basic
import pygame
import Level

class Menu:
    def __init__(self):
        self.menu = "start"
        self.start = Start()
        self.lose = Lose()
        self.level = Level.Level()

    def show(self, surface):
        if self.menu == "start":
            if self.start.show(surface):
                self.menu = "play"
        elif self.menu == "play":
            self.level.update()
            self.level.draw(surface)
            if self.level.state == "win":
                self.menu = "win"
            elif self.level.state == "lose":
                self.menu = "lose"
        elif self.menu == "win":
            surface.fill(Basic.GREEN)
            self.text.change("YOU WON", 100)
            surface.blit(self.text.image, (60, 100))

            self.button.change(Basic.SCREEN_WIDTH / 2 - 200, 350, Basic.RED, Basic.LIGHT_RED, 380, 60)
            self.button.update()
            self.button.show(surface)

            self.text.change("TRY AGAIN", 45)
            surface.blit(self.text.image, (Basic.SCREEN_WIDTH / 2 - 195, 360))

            if self.button.clicks:
                self.menu = "setup"

        elif self.menu == "lose":
            if self.lose.show(surface):
                level.gen_track()
                level.state = True
                manager.switch("play")
                self.menu = "play"

    def event(self, event):
        self.level.event(event)

class Start:
    def __init__(self):
        self.background = pygame.image.load("Textures\\background.png")
        self.button = Objects.Bottun(Basic.SCREEN_WIDTH / 2 - 190, 450, Basic.GREEN, Basic.LIGHT_GREEN, 385, 100)
        self.texts = pygame.sprite.Group()
        self.texts.add(Draw.Text("WELCOME TO:", 70, x = 50, y = 50))
        self.texts.add(Draw.Text("CAVEMAN", 120, x = 10, y = 150))
        self.texts.add(Draw.Text("CITY", 120, x = 200, y = 270))
        self.texts.add(Draw.Text("START", 80, x = Basic.SCREEN_WIDTH / 2 - 180, y = 465))

    def show(self, surface):
        surface.blit(self.background, (0, 0))
        self.button.update()
        self.button.show(surface)
        self.texts.draw(surface)
        if self.button.clicks:
            return True
        return False

class Lose:
    def __init__(self):
        self.button = Objects.Bottun(Basic.SCREEN_WIDTH / 2 - 200, 350, Basic.GREEN, Basic.LIGHT_GREEN, 380, 60)
        self.texts = pygame.sprite.Group()
        self.texts.add(Draw.Text("YOU LOSE", 100, x = 30, y = 100))

    def show(self, surface):
        surface.fill(Basic.RED)
        self.texts.draw(surface)
        self.button.update()
        self.button.show(surface)
        if self.button.clicks:
            return True
        return False
