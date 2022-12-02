import pygame, sys, time
from conf import *
from sprites import BG, Ground, Plane, Obstacle



class Game:
    def __init__(self):

        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Flabby Bird')
        self.clock = pygame.time.Clock()
        self.active = True

        self.all_sprites = pygame.sprite.Group()
        self.collission_sprites = pygame.sprite.Group()

        bg_height = pygame.image.load("jOGO/bird/assets/background_resized.png").get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height
        
        BG(self.all_sprites,self.scale_factor)
        Ground([self.all_sprites,self.collission_sprites],self.scale_factor)
        self.plane = Plane(self.all_sprites,self.scale_factor / 5.8)

        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer,1400)
        
        self.font = pygame.font.Font("jOGO/bird/assets/BD_Cartoon_Shout.ttf",30)
        self.score = 0
        self.start_offset = 0

        self.menu_surf = pygame.image.load("jOGO/bird/assets/menu.png").convert_alpha()
        self.menu_rect = self.menu_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self.music = pygame.mixer.Sound("jOGO/bird/assets/music.mp3")
        self.music.set_volume(0.3)
        self.music.play(loops = -1)

    def collisions(self):
        if pygame.sprite.spritecollide(self.plane,self.collission_sprites,False,pygame.sprite.collide_mask) or self.plane.rect.top <= 0:
            for sprite in self.collission_sprites.sprites():
                if sprite.sprite_type == 'obstacle':
                    sprite.kill()
            self.active = False
            self.plane.kill()

    def display_score(self):
        if self.active:
            self.score = (pygame.time.get_ticks() - self.start_offset) // 1000
            y = WINDOW_HEIGHT / 10
        else:
            y = WINDOW_HEIGHT / 3 + self.menu_rect.height    

        score_surf = self.font.render(str(self.score),True,'black')
        score_rect = score_surf.get_rect(midtop = (WINDOW_WIDTH / 2,y))
        self.display_surface.blit(score_surf,score_rect)

    def run(self):
           last_time = time.time()
           while True:

               dt = time.time() - last_time
               last_time = time.time()


               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
                   if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.active:
                            self.plane.jump()
                        else:
                            self.plane = Plane(self.all_sprites,self.scale_factor / 5.8)
                            self.active = True
                            self.start_offset = pygame.time.get_ticks()    

                   if event.type == self.obstacle_timer and self.active:
                        Obstacle([self.all_sprites,self.collission_sprites],self.scale_factor * 1.3)

               self.display_surface.fill('black')
               self.all_sprites.update(dt)
               self.all_sprites.draw(self.display_surface)
               self.display_score()

               if self.active: 
                    self.collisions()
               else:
                    self.display_surface.blit(self.menu_surf,self.menu_rect)     
               
               pygame.display.update()
               self.clock.tick(FRAMERATE)

if __name__ == '__main__':

    game = Game()
    game.run()
