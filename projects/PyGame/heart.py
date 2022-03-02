import pygame
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg_img1 = pygame.image.load("projects/PyGame/pictures/background/quiz1.png")
bg1 = pygame.transform.scale(bg_img1,(WIDTH,HEIGHT))

class animate(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.heart = pygame.image.load('projects\PyGame\pictures\objects\heart.png')
        # self.char0 = pygame.image.load('projects\PyGame\pictures\ch1.png')
        # self.char0_1 = pygame.transform.scale(self.char0, (int(self.char0.get_width() * scale), int(self.char0.get_height() * scale)))
        self.heart0 = pygame.transform.scale(self.heart, (int(self.heart.get_width() * scale), int(self.heart.get_height() * scale)))
        # self.rectx = self.char0_1.get_rect()
        self.rectht = self.heart0.get_rect()
        # self.rectx.center = (x, y)
        self.rectht.center = (x, y)
        
def threeHeart():    
    running = True
    heart1 = animate(100, 50, 0.5)
    heart2 = animate(150, 50, 0.5)
    heart3 = animate(200, 50, 0.5)
    user = animate(150, 375, 1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg1, (0, 0))
        # screen.blit(user.char0_1, user.rectx)
        screen.blit(heart1.heart0, heart1.rectht)
        screen.blit(heart2.heart0, heart2.rectht)
        screen.blit(heart3.heart0, heart3.rectht) 
        pygame.display.update()

def twoHeart():    
    running = True
    heart1 = animate(100, 50, 0.5)
    heart2 = animate(150, 50, 0.5)
    user = animate(150, 375, 1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg1, (0, 0))
        # screen.blit(user.char0_1, user.rectx)
        screen.blit(heart1.heart0, heart1.rectht)
        screen.blit(heart2.heart0, heart2.rectht)
        pygame.display.update()

def oneHeart():    
    running = True
    heart1 = animate(100, 50, 0.5)
    user = animate(150, 375, 1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg1, (0, 0))
        # screen.blit(user.char0_1, user.rectx)
        screen.blit(heart1.heart0, heart1.rectht)
        pygame.display.update()

threeHeart()
# oneHeart()