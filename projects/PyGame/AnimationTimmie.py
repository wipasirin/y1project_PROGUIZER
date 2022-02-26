import pygame
import sys

WIDTH = 750
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class animateTimmie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imgChar =[]
        self.imgChar.append(pygame.image.load("projects/PyGame/pictures/ch1.png"))
        self.imgChar.append(pygame.image.load("projects/PyGame/pictures/ch2.png"))
        self.current_imgChar = 0
        self.compute_animation = False
        self.image = self.imgChar[self.current_imgChar]
        # self.char0_1 = pygame.transform.scale(char0 (int(char0.get_width() * scale, char0.get_height() * scale)))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
    
    def compute(self):
        self.compute_animation = True

    def update(self, speed): # speed ต้องบวกได้จำนวนเต็ม 0++
        if self.compute_animation == True:
            self.current_imgChar += speed
            if int(self.current_imgChar) >= len(self.imgChar):
                self.current_imgChar = 0
                self.compute_animation = False
        
        self.image = self.imgChar[int(self.current_imgChar)]

running = True
animation_timmie = pygame.sprite.Group()
timmie = animateTimmie(200, 200)
animation_timmie.add(timmie)
        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            timmie.compute()
        
    screen.fill((0,0,0))
    animation_timmie.draw(screen) # draw charactor
    animation_timmie.update(0.2)
    pygame.display.update()
    clock.tick(15)
    