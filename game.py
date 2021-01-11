#started game.py and enemies.py
#created clicks to figure out the coordinates of the path
#-to hard code it for ememy movement

import pygame
import os

class Game:
    def __init__(self):
        self.width = 900 #for screen
        self.height = 500
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        #self.attack_towers = []
        #self.support_towers = []
        self.lives = 10
        self.money = 2000
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        
        #transforms background image to fill the width the height of the screen
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

        self.clicks = [] #remove

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60) #runs game at 60 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)
                    #prints coords of clicks


            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        for p in self.clicks:
            pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]),5,0)
        pygame.display.update()


g = Game()
g.run()