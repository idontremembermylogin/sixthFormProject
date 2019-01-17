#ver1

import pygame, sys
from pygame.locals import *

DEBUG = False

WINDOWWIDTH =800
WINDOWHEIGHT = 500
BACKGROUNDCOLOUR = (255, 255, 255)#placeholder colour is white
GAMECLOCK = pygame.time.Clock()
FPS = 60 #could be varied to change difficulty

PLAYERCOORDSX = 0 #these are placeholders for an actual spawn - actual spawn will work for custom aspect ratios
PLAYERCOORDSY = 0
PLATFORMCOORDSX =0
PLATFORMCOORDSY =(WINDOWHEIGHT - (WINDOWHEIGHT*0.111))

PLATFORM2COORDSX = 700
PLATFORM2COORDSY = 350

#print(WINDOWHEIGHT*0.111)

class Player(pygame.sprite.Sprite):

    def __init__(self, playerCoOrdsX=PLAYERCOORDSX, playerCoOrdsY=PLAYERCOORDSY):
        super().__init__()

        self.image = pygame.image.load('player.png')

        self.rect = self.image.get_rect()

        self.rect.x = playerCoOrdsX
        self.rect.y = playerCoOrdsY

        self.changeX = 0
        self.changeY = 0

        self.gravity = True
        if DEBUG:
            print("grav is true")
    def getRect(self):
        return self.rect

    def getSurface(self):
        return self.image

    def moveUp(self):
        self.gravity = False
        if DEBUG:
             print("player moveUp called")
        self.changeY -= 10

    def moveRight(self):
        if DEBUG:
            print("player moveRight called")
        self.changeX += 5

    def moveLeft(self):
        if DEBUG:
            print("player moveLeft called")
        self.changeX -= 5

    def moveStopX(self):
        #print("player moveStopX called")
        self.changeX = 0

    def moveStopY(self):
        #print("player moveStopY called")
        self.changeY =0
        
    def posUpdate(self):
        self.calculateGravity()
        self.rect.y += self.changeY
        self.rect.x += self.changeX
        if DEBUG:
            print("posUpdate called")
            
    def calculateGravity(self):
        #add gravity contols to movement
        if self.gravity == True:
            if self.changeY == 0:
                self.changeY = 0.35
                if DEBUG:
                    print("gravity true")
            else:
                self.changeY += 0.35
                if DEBUG:
                    print("gravity false")
        else:
            self.gravity=True
            
    def collision(self, sprite):
        #slow down Y speed to 0 when collision happens
        return self.rect.colliderect(sprite.rect)
    
    def collisionGravity(self):
        self.gravity = False
        if self.changeY >0:#if chnage is >0 then stop moving down
            self.changeY = 0
        else:
            self.gravity = True#else do nothing?

class Platform(pygame.sprite.Sprite):

    def __init__(self, platformCoOrdsX, platformCoOrdsY):
        super().__init__()

        self.image = pygame.image.load('platform.png')
        self.rect = self.image.get_rect()
        #self.surface = self.Surface.get_surface()
        
        self.rect.x = platformCoOrdsX
        self.rect.y = platformCoOrdsY
    def getRect(self):
        return self.rect

    def getSurface(self):
        return self.image 

## MAIN PROGRAM

pygame.init()
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
windowsurface.fill(BACKGROUNDCOLOUR)
pygame.display.set_caption('ben project')
pygame.mouse.set_visible(True)#this will be set to False in the final version
pygame.display.update()

myPlayer = Player()
myPlatform = Platform(PLATFORMCOORDSX, PLATFORMCOORDSY)
myPlatform2 = Platform(PLATFORM2COORDSX, PLATFORM2COORDSY)

while True: #change this!

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_w:
                myPlayer.moveUp()
            elif event.key == K_LEFT or event.key == K_a:
                myPlayer.moveLeft()
            elif event.key == K_RIGHT or event.key == K_d:
                myPlayer.moveRight()

        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_d:
                myPlayer.moveStopX()
            if event.key == K_LEFT or event.key == K_a:
                myPlayer.moveStopX()
            if event.key == K_UP or event.key == K_w:
                myPlayer.moveStopY()

        if event.type == QUIT:
            exit()
            
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    if myPlayer.collision(myPlatform):
        myPlayer.collisionGravity()

    if myPlayer.collision(myPlatform2):
        myPlayer.collisionGravity()
    
    myPlayer.posUpdate()
    
    windowsurface.fill(BACKGROUNDCOLOUR)
    windowsurface.blit(myPlayer.getSurface(), myPlayer.getRect())
    windowsurface.blit(myPlatform.getSurface(), myPlatform.getRect())
    windowsurface.blit(myPlatform2.getSurface(), myPlatform2.getRect())

    pygame.display.update()
    GAMECLOCK.tick(FPS)



















    
