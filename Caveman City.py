import Basic
import Draw
import Level
import time
import pygame

def main():

    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
 
    size = [Basic.SCREEN_WIDTH, Basic.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    background = pygame.image.load("Textures\\background.png")
 
    pygame.display.set_caption("CAVEMAN CITY!")

    level = Level.Level()

    text = Draw.Text("TIME: 0.000", 50)
    text.rect.x = 0
    text.rect.y = 0
    level.texts.add(text)

    start_time = time.time()

    state = "start"
    now = True
    press = False

    done = False

    clock = pygame.time.Clock()

    extra_time = 0
    fire_time = 0

    Time = 60

    while not done:
        for event in pygame.event.get():

            level.event(event)

            if event.type == pygame.QUIT:
                done = True
          
        screen.blit(background, (0, 0))

        level.update()

        now_time = time.time()

        if not level.player.done:
            Time = int(60 - (now_time - start_time - level.extra_time + extra_time))
            text.text_counter("TIME: " + str(Time))

        level.draw(screen)
                    
        clock.tick(60)

        pygame.display.flip()

    pygame.quit()
 
if __name__ == "__main__":
    main()