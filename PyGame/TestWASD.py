from turtle import Screen
import pygame

WIDTH = 500
HEIGHT = 250
SEABLUE = (92, 177, 179) #RGB
BLACK = (0,0,0)
FPS = 30


#BG = pygame.image.load("pictures\map.png")
pygame.init #initialize pygame
clock = pygame.time.Clock() #set time
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #set game screen
pygame.display.set_caption("PROGUIZER") #set head 
#exit_game = pygame.display.quit()

### create character ###
class mary(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pictures\mary2.png")
        self.rect = self.image.get_rect()
        # set position of character
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2
        # movement
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.image = pygame.image.load("pictures\mary2.png")
        keypress = pygame.key.get_pressed()
        if (keypress[pygame.K_d]): # if user press 'd' -- move right
            self.image = pygame.image.load("pictures\mary3.png")
            self.speedx = +5
        elif (keypress[pygame.K_a]): # if user press 'a' -- move left
            self.image = pygame.image.load("pictures\mary4.png")
            self.speedx = -5
        elif (keypress[pygame.K_w]): # if user press 'w' -- move up
            self.image = pygame.image.load("pictures\mary5.png")
            self.speedy = -5
        elif (keypress[pygame.K_s]): # if user press 's' -- move down
            self.image = pygame.image.load("pictures\mary2.png")
            self.speedy = 5
        # move by add position 
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # check screen scope (x, y) -- pygame don't have up down
        if (self.rect.right > WIDTH): 
            self.rect.right = WIDTH
        if (self.rect.left < 0):
            self.rect.left = 0

all_sprites = pygame.sprite.Group()
mary = mary()
all_sprites.add(mary)

running = True

while running : # loop screen/game
    clock.tick(FPS)

    for event in pygame.event.get(): # check circumstance in the game
        if (event.type == pygame.QUIT) : #when press botton an exit
            running = False
    
    all_sprites.update()
    screen.fill(SEABLUE) # bg
    all_sprites.draw(screen)
    pygame.display.flip() # update the full display surface to the screen <more important>

pygame.quit()