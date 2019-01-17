#ver0.1

import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH =800
WINDOWHEIGHT = 450
PLAYERCOORDSX = 0 #these are placeholders for an actual spawn - actual spawn will work for custom aspect ratios
PLAYERCOORDSY = 0
BACKGROUNDCOLOUR = (255, 255, 255)
GAMECLOCK = pygame.time.Clock()
FPS = 60 #could be varied to change difficulty

#initialsing pygame, setting window size and window caption, setting the mouse to invisible
pygame.init()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('ben project')
pygame.mouse.set_visible(True) # this will be set to false later on

#imorting the player sprite and game world
playerSprite = pygame.image.load("player.png")
playerShape = playerSprite.get_rect(topleft=(PLAYERCOORDSX, PLAYERCOORDSY))

windowSurface.fill(BACKGROUNDCOLOUR)
pygame.display.update()

#setting up platforms

platformSprite = pygame.image.load("platform.png")
platformShape = platformSprite.get_rect()

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

    pygame.display.update()
    
    GAMECLOCK.tick(FPS)



























    
