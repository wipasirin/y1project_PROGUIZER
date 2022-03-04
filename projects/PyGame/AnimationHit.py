import pygame
import sys

WIDTH = 750
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class animateHit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imgHit =[]
        self.imgHit.append(pygame.image.load("projects\PyGame\pictures\hit_1.png"))
        self.imgHit.append(pygame.image.load("projects\PyGame\pictures\hit_2.png"))
        self.imgHit.append(pygame.image.load("projects\PyGame\pictures\hit_3.png"))
        self.current_imgHit = 0
        self.attack = False
        self.image = self.imgHit[self.current_imgHit]
        # self.char0_1 = pygame.transform.scale(char0 (int(char0.get_width() * scale, char0.get_height() * scale)))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
    
    def attackmtd(self):
        self.attack = True

    def update(self, speed): # speed ต้องบวกได้จำนวนเต็ม 0++
        if self.attack == True:
            self.current_imgHit += speed
            if int(self.current_imgHit) >= len(self.imgHit):
                self.current_imgHit = 0
                self.attack = False
        
        self.image = self.imgHit[int(self.current_imgHit)]

running = True
hit_group = pygame.sprite.Group()
hit = animateHit(200, 200)
hit_group.add(hit)
        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            hit.attackmtd()
        
    screen.fill((0,0,0))
    hit_group.draw(screen) # draw charactor
    hit_group.update(0.2)
    pygame.display.update()
    clock.tick(15)