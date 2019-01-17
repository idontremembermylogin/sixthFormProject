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


class main():
    def __init__(self):
        #initialise the game window (size, colour etc.)
        pygame.init()
        self.windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.windowsurface.fill(BACKGROUNDCOLOUR)
        pygame.display.set_caption('ben project')
        pygame.mouse.set_visible(True)#this will be set to False in the final version

        pygame.display.update()
        self.GAMECLOCK = pygame.time.Clock()

        self.gameGo = True

    def newGame(self):
        #default settings for a new game:
        self.platforms = pygame.sprite.Group()
        self.player = Player(self)

        platforms = []
        for p in platforms:
            platforms.append(Platform(random.randint(1,100),random.randint(1,100)))

        self.Start()

    def Start(self):
        #game loop

        self.go = True

        while self.go == True:
            self.GAMECLOCK.tick(FPS)
            self.update()
            self.draw()

    def draw(self):
        #draw all the sprites
        self.platforms.draw(self.windowsurface)
        self.windowsurface.blit(Player)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    if self.go:
                        self.go = False
                        
                if event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_w:
                        myPlayer._moveUp()
                    elif event.key == K_LEFT or event.key == K_a:
                        myPlayer._moveLeft()
                    elif event.key == K_RIGHT or event.key == K_d:
                        myPlayer._moveRight()

                if event.type == KEYUP:
                    if event.key == K_RIGHT or event.key == K_d:
                        myPlayer._moveStopX()
                    if event.key == K_LEFT or event.key == K_a:
                        myPlayer._moveStopX()
                    if event.key == K_UP or event.key == K_w:
                        myPlayer._moveStopY()


class Platform(pygame.sprite.Sprite):
    def __init__(self,


main = main()

while main.gameGo:
    main.newGame()
