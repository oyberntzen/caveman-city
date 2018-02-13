import Basic
import Draw
import Level
import pygame
import Menus

def main():

    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
 
    size = [Basic.SCREEN_WIDTH, Basic.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    background = pygame.image.load("Textures\\background.png")
 
    pygame.display.set_caption("CAVEMAN CITY!")

    level = Level.Level()
    manager = Menus.Menu()

    now = True
    press = False

    done = False

    clock = pygame.time.Clock()

    Time = 60

    while not done:
        for event in pygame.event.get():

            level.event(event)

            if event.type == pygame.QUIT:
                done = True

        
          
        screen.blit(background, (0, 0))
        manager.show(screen)

        if manager.menu == "play":
            level.update()
            level.draw(screen) 
            if level.state == "win":
                manager.switch("win")
            elif level.state == "lose":
                manager.switch("lose")
                
            
        clock.tick(60)

        pygame.display.flip()

    pygame.quit()
 
if __name__ == "__main__":
    main()