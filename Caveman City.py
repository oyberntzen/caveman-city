import Basic
import Draw
import Level
import pygame

def main():

    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
 
    size = [Basic.SCREEN_WIDTH, Basic.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    background = pygame.image.load("Textures\\background.png")
 
    pygame.display.set_caption("CAVEMAN CITY!")

    level = Level.Level()

    state = "start"
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

        if level.state == "play":
            level.update()
            level.draw(screen)
        elif level.state == "win":
            screen.fill(Basic.GREEN)
            text = Draw.Text("YOU WON", 100)
            screen.blit(text.image, (60, 250))
        elif level.state == "lose":
            screen.fill(Basic.RED)
            text = Draw.Text("YOU LOSE", 100)
            screen.blit(text.image, (30, 250))
                    
        clock.tick(60)

        pygame.display.flip()

    pygame.quit()
 
if __name__ == "__main__":
    main()