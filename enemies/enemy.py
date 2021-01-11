import pygame
class Enemy:
    def __init__(slef, x, y):
        self.x =x
        self.y=y 
        self.imgs = imgs
        self.animation_count = 0
        self.health = 1
        #hard code the path for enemy using printed clicks
        self.path = [[(16, 161), (117, 165), (166, 184), (193, 198), (397, 197), (450, 177), (469, 130), (479, 68), (539, 40), (613, 68), (625, 125), (652, 175), (693, 197), (758, 217), (788, 272), (767, 330), (700, 360), (597, 353), (552, 369), (517, 394), (138, 397), (88, 377), (67, 333), (58, 277), (31, 247), (0, 241)]]
        self.img = None

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        #figure out what image is going to be drawn, an dhow quickly looping through images
        self.animations_count += 1
        self.img = self.imgs(self.animmation_count)
        win.blit(self.img, (self.x, self.y))
        

    def collides(self,X,Y):
        """
        Returns if positions has hit enemy
        :param x: int
        :param y: int
        :return: Bool
        """
        #collision check  
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self): 
        #calculates based on x,y position how to move to the next position on the map
        """Move enemy
        :retin: None
        """

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True


