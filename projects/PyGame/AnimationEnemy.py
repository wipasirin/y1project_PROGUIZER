import pygame
import sys

WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class animateEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imgEne =[]
        self.imgEne.append(pygame.image.load("projects\PyGame\pictures\character\monster1.png"))
        self.imgEne.append(pygame.image.load("projects\PyGame\pictures\character\monster2.png"))
        self.imgEne.append(pygame.image.load("projects\PyGame\pictures\character\monster3.png"))
        self.imgEne.append(pygame.image.load("projects\PyGame\pictures\character\monster4.png"))
        self.imgEne.append(pygame.image.load("projects\PyGame\pictures\character\monster5.png"))
        self.imgEne.append(pygame.image.load("projects\PyGame\pictures\character\monster6.png"))
        self.imgEne.append(pygame.image.load("projects\PyGame\pictures\character\monster7.png"))
        self.imgEne.append(pygame.image.load("projects\PyGame\pictures\character\monster8.png"))
        self.current_imgEne = 0
        self.death_animation = False
        self.image = self.imgEne[self.current_imgEne]
        # self.char0_1 = pygame.transform.scale(char0 (int(char0.get_width() * scale, char0.get_height() * scale)))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
    
    def death(self):
        self.death_animation = True

    def update(self, speed): # speed ต้องบวกได้จำนวนเต็ม 0++
        if self.death_animation == True:
            self.current_imgEne += speed
            if int(self.current_imgEne) >= len(self.imgEne):
                self.current_imgEne = 0
                self.death_animation = False
        
        self.image = self.imgEne[int(self.current_imgEne)]

running = True
animation_enemy = pygame.sprite.Group()
timmie = animateEnemy(200, 200)
animation_enemy.add(timmie)
        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            timmie.death()
        
    screen.fill((200,200,200))
    animation_enemy.draw(screen) # draw charactor
    animation_enemy.update(0.2)
    pygame.display.update()
    clock.tick(15)