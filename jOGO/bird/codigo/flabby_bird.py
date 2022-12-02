import pygame, sys, time

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800
FRAMERATE = 120


class Game:
    def __init__(self):

        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Flabby Bird')
        self.cloak = pygame.time.Cloak()

       def run(self):
           last_time = time.time()
           while True:

               dt = time.time() - last_time
               last_time = time.time()


               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()

               pygame.display.update()
               self.clock.tick(FRAMERATE)

    if __name__ == '__main__':

        game = Game()
        game.run()
