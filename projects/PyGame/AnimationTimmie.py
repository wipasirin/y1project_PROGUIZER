from unicodedata import name
import pygame
import sys
import TestButton

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
        self.checkAni = False
        # self.char0_1 = pygame.transform.scale(char0 (int(char0.get_width() * scale, char0.get_height() * scale)))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
    
    def compute(self):
        self.compute_animation = True

    def update(self, speed): # speed ต้องบวกได้จำนวนเต็ม 0++
        if self.compute_animation == True:
            self.current_imgChar += speed
            if int(self.current_imgChar) >= len(self.imgChar):
                self.current_imgChar = 1
                # self.compute_animation = False
                self.checkAni = True
                print("enough")
        
        self.image = self.imgChar[int(self.current_imgChar)]

class quizTimmie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("projects/PyGame/pictures/ch2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]   
    def draw(self):
        screen.blit(self.image,[self.rect.x, self.rect.y])

def init_anime():
    global animation_timmie, timmieAni
    animation_timmie = pygame.sprite.Group()
    timmieAni = animateTimmie(200, 200)
    animation_timmie.add(timmieAni)

def mainAni():
    running = True    
    init_anime()      
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                timmieAni.compute()
            
        screen.blit(TestButton.bg2, (0,0))
        animation_timmie.draw(screen) # draw charactor
        animation_timmie.update(0.2)
        print(timmieAni.checkAni)
        if(timmieAni.checkAni):
            TestButton.func_quiz1()
            timmie = quizTimmie(200, 200)
            timmie.draw()
            TestButton.main_quiz1
            # running = False
        pygame.display.update()
        clock.tick(15)
        
mainAni()
# TestButton.main_menu()