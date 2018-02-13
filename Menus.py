import Draw
import Objects
import Basic

class Menu:
    def __init__(self):
        self.menu = "start"
        self.button = Objects.Bottun(Basic.SCREEN_WIDTH / 2 - 190, 450, Basic.GREEN, Basic.LIGHT_GREEN, 385, 100)
        self.text = Draw.Text("WELCOME TO:", 70)

    def show(self, surface):
        if self.menu == "start":
            self.text.change("WELCOME TO:", 70)
            surface.blit(self.text.image, (50, 50))

            self.text.change("CAVEMAN", 120)
            surface.blit(self.text.image, (10, 150))

            self.text.change("CITY", 120)
            surface.blit(self.text.image, (200, 270))

            self.button.change(Basic.SCREEN_WIDTH / 2 - 190, 450, Basic.GREEN, Basic.LIGHT_GREEN, 385, 100)
            self.button.update()
            self.button.show(surface)

            self.text.change("START", 80)
            surface.blit(self.text.image, (Basic.SCREEN_WIDTH / 2 - 180, 465))
            
            if self.button.clicks:
                self.menu = "play"

        elif self.menu == "win":
            surface.fill(Basic.GREEN)
            self.text.change("YOU WON", 100)
            surface.blit(self.text.image, (60, 100))
            
            self.button.change(Basic.SCREEN_WIDTH / 2 - 200, 350, Basic.RED, Basic.LIGHT_RED, 380, 60)
            self.button.update()
            self.button.show(surface)

            self.text.change("TRY AGAIN", 45)
            surface.blit(self.text.image, (Basic.SCREEN_WIDTH / 2 - 187, 360))

        elif self.menu == "lose":
            surface.fill(Basic.RED)
            self.text.change("YOU LOSE", 100)
            surface.blit(self.text.image, (30, 100))

            self.button.change(Basic.SCREEN_WIDTH / 2 - 200, 350, Basic.GREEN, Basic.LIGHT_GREEN, 380, 60)
            self.button.update()
            self.button.show(surface)

            self.text.change("TRY AGAIN", 45)
            surface.blit(self.text.image, (Basic.SCREEN_WIDTH / 2 - 195, 360))

    def switch(self, new):
        self.menu = new