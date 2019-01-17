
#ver1

import pygame, sys, random
from pygame.locals import *

DEBUG = False
MALEFEMALE = False #True for Male, False for Female

WINDOWWIDTH =800
WINDOWHEIGHT = 450
BACKGROUNDCOLOUR = (97, 133, 248)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
GAMECLOCK = pygame.time.Clock()
FPS = 120 #could be varied to change difficulty

CURRENTSCORE = 0
FPSCOUNTER = 0

PLAYERCOORDSX = 0 #these are placeholders for an actual spawn - actual spawn will work for custom aspect ratios
PLAYERCOORDSY = 0
PLATFORMCOORDSX =0
PLATFORMCOORDSY =(WINDOWHEIGHT - (WINDOWHEIGHT*0.111))
PLAYERMOVEMENTSPEED = 5
PLATFORMMOVEMENTSPEED = 0.001
SCROLLSPEED = 5
JUMPHEIGHT = PLAYERMOVEMENTSPEED*2 #IMPLEMT IT


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
        
    def getRect(self):
        return self.rect

    def getSurface(self):
        return self.image
    
    def posUpdate(self):
        self.rect.x += self.changeX

    def scrollLtoR(self):
        self.changeX -= PLATFORMMOVEMENTSPEED


class PlatformUpDown(Platform):

    def __init__(self, platformCoOrdsX, platformCoOrdsY, tbound=10, bbound=10):#pass in speed here  ##, moveUp=True):
        super().__init__(platformCoOrdsX, platformCoOrdsY)

        self.fixedY = self.getRect().y    #replace with ubound and bbound
        self.tbound = tbound
        self.bbound = bbound

        self.moveUp = True
        
        self.changeY = 0
        
        if self.moveUp:
            self.changeY -= 0.1
            if DEBUG:
                print("self.changeY -= 1")
        else:
            self.changeY = 0.1
            if DEBUG:
                print("self.changeY = 1")
        
    def _UpDown(self):
        #if self.rect.y has gotten to a certain point: turn around
        if self.rect.y <= self.fixedY + self.tbound:
            self.changeY += 10
            #<=
            #maintain direction just keep it going
            #

    def posUpdate(self):
        self.rect.x += self.changeX
        self.rect.y = self.changeY



        
class Player(pygame.sprite.Sprite):

    

    def __init__(self, playerCoOrdsX=PLAYERCOORDSX, playerCoOrdsY=PLAYERCOORDSY):
        super().__init__()

        if MALEFEMALE == True:
            self.image = pygame.image.load('Mplayer_14x19.png')
        else:
            self.image = pygame.image.load('Fplayer_70x95.png')

        self.rect = self.image.get_rect()

        self.rect.x = playerCoOrdsX
        self.rect.y = playerCoOrdsY

        self.changeX = 0
        self.changeY = 0

        self.gravity = True

        #gravity for self.change values contant goes here
        self.GRAVITYSTRENGTH = 0.35
        if DEBUG:
            print("grav is true")
            
    def calculateGravity(self):
        ##APPLIES GRAVITY TO PLAYER OBJECT WHEN NOT COLLIDING WITH A PLATFORM
        if self.gravity == True:
            if self.changeY == 0:
                self.changeY = self.GRAVITYSTRENGTH
                if DEBUG:
                    print("gravity true")
            else:
                self.changeY += self.GRAVITYSTRENGTH
                if DEBUG:
                    print("gravity false")
        else:
            self.gravity=True
            
    def collision(self, sprite):
        #DETECTS A COLLISION BETWEEN PLATFORM AND PLAYER
        return self.rect.colliderect(sprite.rect)
    
    def collisionGravity(self):
        #IF THERE HAS BEEN A COLLISION, THIS WILL STOP THE PLAYER FROM MOVING
        self.gravity = False
        if self.changeY >0:
            self.changeY = 0
        else:
            self.gravity = True
        
    def getRect(self):
        return self.rect

    def getSurface(self):
        return self.image

    def moveLeft(self):
        if DEBUG:
            print("player moveLeft called")
        self.changeX -= PLAYERMOVEMENTSPEED
    
    def moveRight(self):
        if DEBUG:
            print("player moveRight called")
        self.changeX += PLAYERMOVEMENTSPEED
        
    def moveStopX(self):
        if DEBUG:
            print("player moveStopX called")
        self.changeX = 0

    def moveStopY(self):
        if DEBUG:
            print("player moveStopY called")
        self.changeY =0

    def moveUp(self):
        self.gravity = False
        if DEBUG:
             print("player moveUp called")
        self.changeY -= JUMPHEIGHT
        
    def posUpdate(self):
        ##UPDATES THE LOCATION OF THE PLAYER IN MEMORY
        self.calculateGravity()
        self.rect.y += self.changeY
        self.rect.x += self.changeX
        if DEBUG:
            print("posUpdate called")
    

##MENU TO BE USED IN TESTING
##CURRENTLY TEXT BASED, WILL BE GRAPHICS BASED
def Menu():
    protoMenu = input("INPUT CHOICE: ")

    if protoMenu == "Start":
        print("main")
        main()

    elif protoMenu == "Leaderboard":
        None
    elif protoMenu == "Player Select":
        PlayerSelect()
    elif protoMenu == "Exit":
        pygame.quit()

    else:
        print ("else")
    Menu()

##PLAYER SELECT - CHANGES THE CONSTANT MALEFEMALE
##CURRENTLY TEXT BASED, WILL BE GRAPHICS BASED
def PlayerSelect():
    MaleYN = input("MALE/FEMALE: ").title()
    if MaleYN == "Male":
        MALEFEMALE = True
    else:
        MALEFEMALE = False

    Menu()






    
def main():
    platforms = []
    global FPSCOUNTER
    while True:

        #SET UP THE START OF THE GAME
            #PLATFORMS, SCORE, TIMER

            #ADD PLATFORMS TO THE PLATFORM LIST
            
            #p = Platform(random.randint(0,WINDOWWIDTH),(random.randint((myPlayer.rect.y-10),WINDOWHEIGHT)))
            while len(platforms) < 3:
                platforms.append(Platform(WINDOWWIDTH, random.randint((myPlayer.rect.y-JUMPHEIGHT),WINDOWHEIGHT)))
                #print(platforms)
                #remove platform from list, the del platform
                #list should refil to three and new platform appears

                #counter every loop
                #counter =100? then if less than 3 spawn 1
                #reset counter

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

            
            #spawning the first starting platform
            windowsurface.fill(BACKGROUNDCOLOUR)
            windowsurface.blit(myPlayer.getSurface(), myPlayer.getRect())
            windowsurface.blit(myPlatform.getSurface(), myPlatform.getRect())
            
            

            #spawn in the list of platforms
            for p in platforms:
                windowsurface.blit(p.getSurface(),p.getRect())
                p.scrollLtoR()
                if myPlayer.collision(p):
                    myPlayer.collisionGravity()
                p.posUpdate()
                if p.rect.x == (0 - 250):
                    platforms.remove(p)
                    del p
                

            #myPlatform._scrollLtoR()
            myPlatform.posUpdate()


            myPlayer.posUpdate()
            
            
            GAMECLOCK.tick(FPS)
            FPSCOUNTER = FPSCOUNTER + 1
            
            timer = FPSCOUNTER/FPS
            score = str(int(timer*4))
            scoreText = myFont.render(("Score: "+score), True, (WHITE))
            scoreText_rect = scoreText.get_rect(center=((WINDOWWIDTH/6)*5,20))
            windowsurface.blit(scoreText, scoreText_rect)
            
            pygame.display.update()
            
    
    
## MAIN PROGRAM

pygame.init()
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
windowsurface.fill(BACKGROUNDCOLOUR)
myFont = pygame.font.SysFont("Calibri", 35)
pygame.display.set_caption("Benjamin Davidson - Jumper")
pygame.mouse.set_visible(True)#this will be set to False in the final version
pygame.display.update()

myPlayer = Player()
myPlatform = Platform(PLATFORMCOORDSX, PLATFORMCOORDSY)


Menu()













    
