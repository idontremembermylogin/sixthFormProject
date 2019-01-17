import pygame, sys, random
from pygame.locals import *
DEBUG = False
MALEFEMALE = False #True for Male, False for Female

WINDOWWIDTH =800
WINDOWHEIGHT = 450
BACKGROUNDCOLOUR = (255, 255, 255)#placeholder colour is white
GAMECLOCK = pygame.time.Clock()
FPS = 60 #could be varied to change difficulty

PLAYERCOORDSX = 0 #these are placeholders for an actual spawn - actual spawn will work for custom aspect ratios
PLAYERCOORDSY = 0
PLATFORMCOORDSX =0
PLATFORMCOORDSY =(WINDOWHEIGHT - (WINDOWHEIGHT*0.111))
PLAYERMOVEMENTSPEED = 5
PLATFORMMOVEMENTSPEED = 0.1
SCROLLSPEED = 0.1



PLATFORM2COORDSX = 700
PLATFORM2COORDSY = 350

class Platform(pygame.sprite.Sprite):

    def __init__(self, platformCoOrdsX, platformCoOrdsY):
        super().__init__()

        self.image = pygame.image.load('platform.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = platformCoOrdsX
        self.rect.y = platformCoOrdsY
        self.changeX = 0
        
    def _getRect(self):
        return self.rect

    def _getSurface(self):
        return self.image
    
    def _posUpdate(self):
        self.rect.x += self.changeX

    def _scrollLtoR(self):
        self.changeX -= PLATFORMMOVEMENTSPEED


platforms = []
p = Platform(random.randint(0,WINDOWHEIGHT),(random.randint(0,WINDOWWIDTH)))
while True:
    platforms.append(p)
    print(platforms)
