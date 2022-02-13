#Cubie's Adventure
# Version 0.01

# import the pygame module
import pygame
import random

# import pygame.locals for easier
# access to key coordinates
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
#Define The Player object Class
class Cubie(pygame.sprite.Sprite):
    def __init__(self):
        super(Cubie, self).__init__()
        self.image = pygame.image.load("Cuby.svg")
        self.image.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [SCREEN_WIDTH/2,SCREEN_HEIGHT/2]
        self.speed = 5
        
    # Movement
    def update(self, pressed_keys, background):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,self.speed)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed,0)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed,0)
            

        #check for boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#Define the Background object Class
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        super(Background, self).__init__()
        self.image = pygame.image.load(image_file)
        self.image.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



#define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# initialize pygame
pygame.init()

# Define the dimensions of screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#make Cubie
cubie = Cubie()

#make the first background
quitbackground = Background("Background5_5.png", [0,0])

#setup clock
clock = pygame.time.Clock()

#variable to controll game loop
On = True

#game loop

while On:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                On = False
        #Did the Player Quit?
        elif event.type == QUIT:
            On = False

    #fill screen with black
    screen.fill((0,0,0))
    
    #Keys Pressed?
    pressed_keys = pygame.key.get_pressed()

    #Update Cubie
    cubie.update(pressed_keys, background)

    #draw the background
    screen.blit(background.image, background.rect)

    #draw cubie
    screen.blit(cubie.image, cubie.rect)

    #Update Display
    pygame.display.flip()

    #Speed of The Clock
    clock.tick(30)

pygame.quit()
