#ver0.1

import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH =800
WINDOWHEIGHT = 450
PLAYERCOORDSX = 0 #these are placeholders for an actual spawn - actual spawn will work for custom aspect ratios
PLAYERCOORDSY = 0
BACKGROUNDCOLOUR = (255, 255, 255)#placeholder colour is white
GAMECLOCK = pygame.time.Clock()
FPS = 60 #could be varied to change difficulty

print (WINDOWHEIGHT*0.111)

### Detects Collisions between player and platforms
##def PlayerPlatformCollide(playerShape, platformShape):
##    for p in platformShape:
##        if playerShape.colliderect(collisions['rect']):
##            return True
##        return False
##
##player = pygame.sprite.Group()

#initialsing pygame, setting window size and window caption, setting the mouse to invisible
pygame.init()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('ben project')
pygame.mouse.set_visible(True) # this will be set to false later on

##class Player(pygame.sprite.Sprite):
##    def __init__(self):
##        sprite.Sprite.__init__()
##        self.image = "player.png"
##        self.rect = self.image.rect()
##        self.rect.x = 0
##        self.rect.y = 0
##
##    def draw(self, windowSurface):
##        windowSurface.blit(self.sprite,(self.x, self.y))
##Player.draw(Player.self.x, Player.self.y)

#imorting the player sprite and game world
playerSprite = pygame.image.load("player.png")
playerShape = playerSprite.get_rect(topleft=(PLAYERCOORDSX, PLAYERCOORDSY))

windowSurface.fill(BACKGROUNDCOLOUR)
pygame.display.update()

#setting up platforms
##rectMode(BOTTOMLEFT)
platformSprite = pygame.image.load("platform.png")
platformShape = platformSprite.get_rect()
##windowSurface.blit(platformSprite,(0, (WINDOWHEIGHT - (WINDOWHEIGHT*0.111))))
##pygame.display.update

moveUp = False
moveLeft = False
moveDown = False
moveRight = False

# game loop starts - scores, controls, spawning in player and platforms take place here
while True:

# Game controls: esc exits, w/up is up, a/left is left, s/down is down, d/right is right
    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_UP or event.key == K_w:
                moveUp = True
                moveDown = False
                
            elif event.key == K_LEFT or event.key == K_a:
                moveLeft = True
                moveRight = False

            elif event.key == K_DOWN or event.key == K_s:
                moveDown = True
                moveUp = False

            elif event.key == K_RIGHT or event.key == K_d:
                moveRight = True
                moveLeft = False
            # Quit the game - not working
##            elif event.type == K_ESCAPE:
##                pygame.quit()
##                sys.exit()

        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key ==  K_UP or event.key == K_w:
                moveUp = False
            
    # Move the player around
    if moveRight == True:
        PLAYERCOORDSX += 5
    if moveDown == True:
        PLAYERCOORDSY += 5
    if moveLeft == True:
        PLAYERCOORDSX -= 5
    if moveUp == True:
        PLAYERCOORDSY -= 5
        
    # re-fill the background colour
    windowSurface.fill(BACKGROUNDCOLOUR)
    
    
    windowSurface.blit(playerSprite, (PLAYERCOORDSX, PLAYERCOORDSY))
    windowSurface.blit(platformSprite,(0, (WINDOWHEIGHT - (WINDOWHEIGHT*0.111))))

##    if PlayerPlatformCollide(playerShape, platformShape):
##        print("test")

##    if playerShape.colliderect(platformShape):
##        #print ("Hello")
##        moveUp = False
##        moveLeft = False
##        moveDown = False
##        moveRight = False

##    if playerShape.top < 0:
##        if moveUp == True:
##            moveUp == False and moveDown == True
##
    pygame.display.update()
    

    GAMECLOCK.tick(FPS)



























    
