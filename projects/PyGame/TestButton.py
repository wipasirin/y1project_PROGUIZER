#from turtle import update
import pygame
import sys

WIDTH = 1000
HEIGHT = 700

next = 0 # now where am I 
# ===== background =======
# -- menu
# -- gameplay1
# -- gameplay2
bg_img3 = pygame.image.load("projects\PyGame\pictures\Bg2.png")
bg3 = pygame.transform.scale(bg_img3, (WIDTH, HEIGHT))  # set a size of bg
# -- gameplay3
bg_img4 = pygame.image.load("projects\PyGame\pictures\Bg1.png")
bg4 = pygame.transform.scale(bg_img4, (WIDTH, HEIGHT))  # set a size of bg

# ============================  CHARACTER  =================================

timmy = pygame.image.load("projects/PyGame/pictures/character/timmy.png")
ani_timmy= pygame.transform.scale(timmy, (int(timmy.get_width() * 0.60), int(timmy.get_height() * 0.60)))

timmycom = pygame.image.load("projects/PyGame/pictures/character/timmycom.png")
ani_timmycom = pygame.transform.scale(timmycom, (int(timmycom.get_width() * 0.60), int(timmycom.get_height() * 0.60)))

monster1 = pygame.image.load("projects\PyGame\pictures\character\monster1.png")
q1_monster = pygame.transform.scale(monster1, (int(monster1.get_width() * 0.60), int(monster1.get_height() * 0.60)))

# ==============================  MENU  ====================================
# start/exit
bt_start = pygame.image.load("projects/PyGame/pictures/buttons/start.png")
bt_exit = pygame.image.load("projects/PyGame/pictures/buttons/exit.png")
# background
menu = pygame.image.load("projects/PyGame/pictures/background/menu.png")
bg_menu = pygame.transform.scale(menu, (WIDTH, HEIGHT))  # set a size of bg
game = pygame.image.load("projects/PyGame/pictures/background/game.png")
bg_game = pygame.transform.scale(game, (WIDTH, HEIGHT))  # set a size of bg
# bg logo
logo = pygame.image.load("projects\PyGame\pictures/background\logo.jpg")
bg_logo = pygame.transform.scale(logo, (WIDTH, HEIGHT))  # set a size of bg

# ============================== QUIZ 1 ====================================
quiz1 = pygame.image.load("projects/PyGame/pictures/background/quiz1.png")
bg_quiz1 = pygame.transform.scale(quiz1, (WIDTH, HEIGHT))
q1_choice1 = pygame.image.load("projects/PyGame/pictures/buttons/quiz1_choice1.png")
q1_choice2 = pygame.image.load("projects/PyGame/pictures/buttons/quiz1_choice2.png")
q1_choice3 = pygame.image.load("projects/PyGame/pictures/buttons/quiz1_choice3.png")
q1_choice4 = pygame.image.load("projects/PyGame/pictures/buttons/quiz1_choice4.png")

# ============================== QUIZ 2 ====================================
quiz2 = pygame.image.load("projects/PyGame/pictures/background/quiz2.png")
bg_quiz2 = pygame.transform.scale(quiz2, (WIDTH, HEIGHT))
q2_choice1 = pygame.image.load("projects/PyGame/pictures/buttons/quiz2_choice1.png")
q2_choice2 = pygame.image.load("projects/PyGame/pictures/buttons/quiz2_choice2.png")

# ============================== QUIZ 3 ====================================
quiz3 = pygame.image.load("projects/PyGame/pictures/background/quiz3.png")
bg_quiz3 = pygame.transform.scale(quiz3, (WIDTH, HEIGHT))
q3_choice1 = pygame.image.load("projects/PyGame/pictures/buttons/quiz3_choice1.png")
q3_choice2 = pygame.image.load("projects/PyGame/pictures/buttons/quiz3_choice2.png")
q3_choice3 = pygame.image.load("projects/PyGame/pictures/buttons/quiz3_choice3.png")
q3_choice4 = pygame.image.load("projects/PyGame/pictures/buttons/quiz3_choice4.png")

# ============================== QUIZ 4 ====================================
quiz4 = pygame.image.load("projects/PyGame/pictures/background/quiz4.png")
bg_quiz4 = pygame.transform.scale(quiz4, (WIDTH, HEIGHT))
q4_choice1 = pygame.image.load("projects/PyGame/pictures/buttons/quiz4_choice1.png")
q4_choice2 = pygame.image.load("projects/PyGame/pictures/buttons/quiz4_choice2.png")

# ============================== QUIZ 5 ====================================
quiz5 = pygame.image.load("projects/PyGame/pictures/background/quiz5.png")
bg_quiz5 = pygame.transform.scale(quiz5, (WIDTH, HEIGHT))
q5_choice1 = pygame.image.load("projects/PyGame/pictures/buttons/quiz5_choice1.png")
q5_choice2 = pygame.image.load("projects/PyGame/pictures/buttons/quiz5_choice2.png")
q5_choice3 = pygame.image.load("projects/PyGame/pictures/buttons/quiz5_choice3.png")
q5_choice4 = pygame.image.load("projects/PyGame/pictures/buttons/quiz5_choice4.png")

# ============================= [ START ] ==================================
pygame.init  # initialize pygame
pygame.display.set_caption("PROGUIZER")  # set head

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # set a size of display
buttonsMenuGroup = pygame.sprite.Group()
buttonsGameGroup = pygame.sprite.Group()

class ClassMenuButton(pygame.sprite.Sprite):  # create class button
    def __init__(self, x, y, image, width, hight, scale):
        # super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (int(width * scale), int(hight * scale)))  # rescale of button
        self.rect = self.image.get_rect()  # surface that suitable of object
        self.rect.topleft = (x, y)
        self.clicked = False
        buttonsMenuGroup.add(self)

    def update(self):  # kill object
        del self

    def draw(self):
        screen.blit(self.image, [self.rect.x, self.rect.y])

    def checkClick(self):
        print("I'm checking")
        pos = pygame.mouse.get_pos()
        if(hasattr(self, 'rect')):
            if(self.rect.collidepoint(pos)):  # test if a point is inside a rectangle(button)
                print("in rect", self)
                if (pygame.mouse.get_pressed()[0] and (self.clicked == False)): # clicked left mouse key (left[0], middle[1], right[2])
                    self.clicked = True
                elif(pygame.mouse.get_pressed()[0] and (self.clicked == True)):
                    self.clicked = False
        else:
            self.clicked = False
        return self.clicked

class ClassGameButton(pygame.sprite.Sprite):  
    def __init__(self, x, y, image, width, hight, scale): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (int(width * scale), int(hight * scale)))  # rescale of button
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y)
        self.clicked = False
        buttonsGameGroup.add(self)

    def drawGameBt(self):
        screen.blit(self.image, [self.rect.x, self.rect.y])

    def updateGameBt(self):
        del self

    def checkClickgm(self):
        print("I'm checking")
        pos = pygame.mouse.get_pos()
        if(hasattr(self, 'rect')):
            if(self.rect.collidepoint(pos)):  # test if a point is inside a rectangle(button)
                print("in rect", self)
                # clicked left mouse key (left[0], middle[1], right[2])
                if (pygame.mouse.get_pressed()[0] and (self.clicked == False)):
                    self.clicked = True
                elif(pygame.mouse.get_pressed()[0] and (self.clicked == True)):
                    self.clicked = False
        else:
            self.clicked = False
        return self.clicked

class ClassHeart(pygame.sprite.Sprite):
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

class ClassMonster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imgChar =[]
        self.imgChar.append(q1_monster)
        # self.imgChar.append(ani_timmycom)
        self.current_imgChar = 0
        self.compute_animation = False
        self.image = self.imgChar[self.current_imgChar]
        self.checkAni = False
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
    
    def damage(self):
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

class ClassAnimeTimmie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imgChar =[]
        self.imgChar.append(ani_timmy)
        self.imgChar.append(ani_timmycom)
        self.current_imgChar = 0
        self.compute_animation = False
        self.image = self.imgChar[self.current_imgChar]
        self.checkAni = False
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

class ClassQuizTimmie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = ani_timmycom
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]   
    def draw(self):
        screen.blit(self.image,[self.rect.x, self.rect.y])

def init_monster():
    global monster_group, monQ1
    monster_group = pygame.sprite.Group()
    monQ1 = ClassMonster(700, 250)
    monster_group.add(monQ1)
    
def init_timmie():
    global timmie_group, timmieAni
    timmie_group = pygame.sprite.Group()
    timmieAni = ClassAnimeTimmie(100, 250)
    timmie_group.add(timmieAni)
            
def threeHeart():    
    # running = True
    heart1 = ClassHeart(100, 75, 0.5)
    heart2 = ClassHeart(150, 75, 0.5)
    heart3 = ClassHeart(200, 75, 0.5)
    screen.blit(heart1.heart0, heart1.rectht)
    screen.blit(heart2.heart0, heart2.rectht)
    screen.blit(heart3.heart0, heart3.rectht) 

def twoHeart():    
    heart1 = ClassHeart(100, 75, 0.5)
    heart2 = ClassHeart(150, 75, 0.5)
    screen.blit(heart1.heart0, heart1.rectht)
    screen.blit(heart2.heart0, heart2.rectht)

def oneHeart():    
    heart1 = ClassHeart(100, 75, 0.5)
    screen.blit(heart1.heart0, heart1.rectht)

def func_menu():
    global button_start, button_exit
    screen.blit(bg_menu, (0, 0))  # used bg
    button_start = ClassMenuButton((WIDTH/2 - bt_start.get_width()/2), 250, bt_start, bt_start.get_width(), bt_start.get_height(), 0.95)
    button_exit = ClassMenuButton((WIDTH/2 - bt_exit.get_width()/2), 400, bt_exit, bt_exit.get_width(), bt_exit.get_height(), 0.95)
    buttonsMenuGroup.draw(screen)  # draw group buttons

def func_quiz1():
    global choice1, choice2, choice3, choice4
    screen.blit(bg_quiz1, (0, 0))
    timmie = ClassQuizTimmie(100, 250)
    timmie.draw()
    monster_group.draw(screen)
    choice1 = ClassGameButton(100, 575, q1_choice1, q1_choice1.get_width(), q1_choice1.get_height(), 0.75)
    choice2 = ClassGameButton(300, 575, q1_choice2, q1_choice2.get_width(), q1_choice2.get_height(), 0.75)
    choice3 = ClassGameButton(500, 575, q1_choice3, q1_choice3.get_width(), q1_choice3.get_height(), 0.75)
    choice4 = ClassGameButton(700, 575, q1_choice4, q1_choice4.get_width(), q1_choice4.get_height(), 0.75)
    buttonsGameGroup.draw(screen)
    threeHeart()
        
def func_quiz2():
    for i in buttonsGameGroup: # kill attribute in group 'buttonsGameGroup'
        i.kill()
    global choice1, choice2
    screen.blit(bg_quiz2, (0, 0))
    timmie = ClassQuizTimmie(100, 250)
    timmie.draw()
    monster_group.draw(screen)
    choice1 = ClassGameButton(100, 575, q2_choice1, q2_choice1.get_width(), q2_choice1.get_height(), 0.75)
    choice2 = ClassGameButton(300, 575, q2_choice2, q2_choice2.get_width(), q2_choice2.get_height(), 0.75)
    buttonsGameGroup.draw(screen)
    threeHeart()

def func_quiz3():
    global choice1, choice2, choice3, choice4
    for i in buttonsGameGroup: # kill attribute in group 'buttonsGameGroup'
        i.kill()
    screen.blit(bg_quiz3, (0, 0))
    timmie = ClassQuizTimmie(100, 250)
    timmie.draw()
    monster_group.draw(screen)
    choice1 = ClassGameButton(100, 575, q3_choice1, q3_choice1.get_width(), q3_choice1.get_height(), 0.75)
    choice2 = ClassGameButton(300, 575, q3_choice2, q3_choice2.get_width(), q3_choice2.get_height(), 0.75)
    choice3 = ClassGameButton(500, 575, q3_choice3, q3_choice3.get_width(), q3_choice3.get_height(), 0.75)
    choice4 = ClassGameButton(700, 575, q3_choice4, q3_choice4.get_width(), q3_choice4.get_height(), 0.75)
    buttonsGameGroup.draw(screen)
    threeHeart()

def func_quiz4():
    for i in buttonsGameGroup: # kill attribute in group 'buttonsGameGroup'
        i.kill()
    global choice1, choice2
    screen.blit(bg_quiz4, (0, 0))
    timmie = ClassQuizTimmie(100, 250)
    timmie.draw()
    monster_group.draw(screen)
    choice1 = ClassGameButton(100, 575, q4_choice1, q4_choice1.get_width(), q4_choice1.get_height(), 0.75)
    choice2 = ClassGameButton(300, 575, q4_choice2, q4_choice2.get_width(), q4_choice2.get_height(), 0.75)
    buttonsGameGroup.draw(screen)
    threeHeart()

def func_quiz5():
    global choice1, choice2, choice3, choice4
    for i in buttonsGameGroup: # kill attribute in group 'buttonsGameGroup'
        i.kill()
    screen.blit(bg_quiz5, (0, 0))
    timmie = ClassQuizTimmie(100, 250)
    timmie.draw()
    monster_group.draw(screen)
    choice1 = ClassGameButton(100, 575, q5_choice1, q5_choice1.get_width(), q5_choice1.get_height(), 0.75)
    choice2 = ClassGameButton(300, 575, q5_choice2, q5_choice2.get_width(), q5_choice2.get_height(), 0.75)
    choice3 = ClassGameButton(500, 575, q5_choice3, q5_choice3.get_width(), q5_choice3.get_height(), 0.75)
    choice4 = ClassGameButton(700, 575, q5_choice4, q5_choice4.get_width(), q5_choice4.get_height(), 0.75)
    buttonsGameGroup.draw(screen)
    threeHeart()

def main_animation():
    running = True    
    init_timmie()
    init_monster()      
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else: #event.type == pygame.KEYDOWN:
                timmieAni.compute()
            
        screen.blit(bg_game, (0,0))
        timmie_group.draw(screen) # draw character
        monster_group.draw(screen) #**** wait to edit ****
        timmie_group.update(0.2)
        print(timmieAni.checkAni)
        if(timmieAni.checkAni):
            if (next == 1):
                print("now is",next)
                main_quiz1()
            elif (next == 2):
                print("now is",next)
                main_quiz2()
            elif (next == 3):
                print("now is",next)
                main_quiz3()
            elif (next == 4):
                print("now is",next)
                main_quiz4()
            elif (next == 5):
                print("now is",next)
                main_quiz5()
            else:
                print("now is",next)
                print("Baka yarouu!")
                pygame.quit()
                sys.exit()
            # running = False
        pygame.display.update()
        clock.tick(15)

# ==============================  MENU  ====================================
def main_menu():
    global next
    running = True
    # ========== game loop ==========
    while running:
        func_menu()
        for event in pygame.event.get():  # check circumstance in the game
            if (event.type == pygame.QUIT):  # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(button_start.checkClick()):
                    button_start.update()
                    button_exit.update()
                    print("Start")
                    print("now is",next)
                    next = 1
                    main_animation() # animetion
                    print("I'm just going a main_quiz1")
                elif(button_exit.checkClick()):
                    print("Exit")
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# ============================== QUIZ 1 ====================================
def main_quiz1():
    global next
    running = True

    while running:
        func_quiz1()
        for event in pygame.event.get():  # check circumstance in the game
            if (event.type == pygame.QUIT):  # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(choice1.checkClickgm()):
                    print("false")
                    main_menu()
                elif (choice2.checkClickgm()):
                    choice1.updateGameBt()
                    choice2.updateGameBt()
                    choice3.updateGameBt()
                    choice4.updateGameBt()
                    print("true")
                    next = 2
                    main_animation()
                    print("false")
                elif (choice3.checkClickgm()):
                    print("false")
                    main_menu()
                elif (choice4.checkClickgm()):
                    print("false")
                    main_menu()
                else:
                    continue
    
        pygame.display.update()

# ============================== QUIZ 2 ====================================
def main_quiz2():
    global next
    func_quiz2()
    running = True
    # ========== game loop ==========
    while running:
        
        for event in pygame.event.get():  # check circumstance in the game
            if (event.type == pygame.QUIT):  # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(choice1.checkClickgm()):
                    choice1.updateGameBt()
                    choice2.updateGameBt()
                    print("true")
                    next = 3
                    main_animation()
                elif (choice2.checkClickgm()):
                    print("false")
                    main_menu()
                else:
                    continue

        pygame.display.update()

def main_quiz3():
    global next
    func_quiz3()
    running = True
    # ========== game loop ==========
    while running:
        
        for event in pygame.event.get():  # check circumstance in the game
            if (event.type == pygame.QUIT):  # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(choice1.checkClickgm()):
                    print("false")
                    main_menu()
                elif (choice2.checkClickgm()):
                    choice1.updateGameBt()
                    choice2.updateGameBt()
                    choice3.updateGameBt()
                    choice4.updateGameBt()
                    print("true")
                    next = 4
                    main_animation()
                elif (choice3.checkClickgm()):
                    print("false")
                    main_menu()
                elif (choice4.checkClickgm()):
                    print("false")
                    main_menu()
                else:
                    continue

        pygame.display.update()

def main_quiz4():
    global next
    func_quiz4()
    running = True
    # ========== game loop ==========
    while running:
        
        for event in pygame.event.get():  # check circumstance in the game
            if (event.type == pygame.QUIT):  # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(choice1.checkClickgm()):
                    choice1.updateGameBt()
                    choice2.updateGameBt()
                    print("true")
                    next = 5
                    main_animation()
                elif (choice2.checkClickgm()):
                    print("false")
                    main_menu()
                else:
                    continue

        pygame.display.update()  


def main_quiz5():
    global next
    func_quiz5()
    running = True
    # ========== game loop ==========
    while running:
        
        for event in pygame.event.get():  # check circumstance in the game
            if (event.type == pygame.QUIT):  # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(choice1.checkClickgm()):
                    print("false")
                    main_menu()
                elif (choice2.checkClickgm()):
                    choice1.updateGameBt()
                    choice2.updateGameBt()
                    choice3.updateGameBt()
                    choice4.updateGameBt()
                    print("true")
                    # now = 5
                    print("Congrat!!")
                    pygame.quit()
                    sys.exit()
                    # main_animation()
                elif (choice3.checkClickgm()):
                    print("false")
                    main_menu()
                elif (choice4.checkClickgm()):
                    print("false")
                    main_menu()
                else:
                    continue

        pygame.display.update() 

# ========== RUN ==========
main_menu()