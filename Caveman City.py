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

    pygame.display.set_caption("CAVEMAN CITY!")


    manager = Menus.Menu()

    now = True
    press = False

    done = False

    clock = pygame.time.Clock()

    Time = 60

    while not done:
        for event in pygame.event.get():
            manager.event(event)
            if event.type == pygame.QUIT:
                done = True
        manager.show(screen)

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
