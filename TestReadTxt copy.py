#from turtle import update
from operator import and_
from tkinter.font import BOLD
from turtle import width
import pygame
import sys
# import pandas
import json

# Opening JSON file


WIDTH = 1250
HEIGHT = 750
nowHt = 3
nextQuestion = 0 # now where am I 
a_data = {}
choiceButList = []
checkChoiceButList = []
score = 0
getdamage = False

pygame.init()  # initialize pygame
pygame.font.init()
# data = pandas.read_excel("projects\PyGame\pictures\objects\QuestionText.xlsx")
file = open("projects\PyGame\pictures\saveQuestion.json")
data = json.load(file)
# ===============================  CHARACTER  ====================================
# timmy
timmy = pygame.image.load("projects\PyGame\pictures\character\char_common.png")
ani_timmy= pygame.transform.scale(timmy, (int(timmy.get_width() * 0.25), int(timmy.get_height() * 0.25)))
timmycom = pygame.image.load("projects\PyGame\pictures\character\char_fight.png")
ani_timmycom = pygame.transform.scale(timmycom, (int(timmycom.get_width() * 0.25), int(timmycom.get_height() * 0.25)))
timmyhurt = pygame.image.load("projects\PyGame\pictures\character\char_damaged.png")
ani_timmyhurt = pygame.transform.scale(timmyhurt, (int(timmyhurt.get_width() * 0.25), int(timmyhurt.get_height() * 0.25)))
#monster
monster1 = pygame.image.load("projects\PyGame\pictures\character\monster1.png")
q1_monster = pygame.transform.scale(monster1, (int(monster1.get_width() * 0.55), int(monster1.get_height() * 0.55)))
# =================================  MENU  =======================================
# start/exit
menu = pygame.image.load("projects\PyGame\pictures/background/bgHome.jpg")
bg_menu = pygame.transform.scale(menu, (WIDTH, HEIGHT))  # set a size of bg

bt_start = pygame.image.load("projects/PyGame/pictures/buttons/start.png")
bt_exit = pygame.image.load("projects/PyGame/pictures/buttons/exit.png")

game = pygame.image.load("projects/PyGame/pictures/background/game.png")
bg_game = pygame.transform.scale(game, (WIDTH, HEIGHT))  # set a size of bg

ghost = pygame.image.load("projects/PyGame/pictures/background/special.png")
bg_ghost = pygame.transform.scale(ghost, (WIDTH, HEIGHT))

# ================================= QUIZ 1 =======================================
quiz1 = pygame.image.load("projects\PyGame\pictures/background/bg2.png")
bg_quiz1 = pygame.transform.scale(quiz1, (WIDTH, HEIGHT))
choicebg = pygame.image.load("projects\PyGame\pictures\choiceEasy.png")
wchoicebg = choicebg.get_width()/6
hchoice = choicebg.get_height()/6
fontChoice = pygame.font.SysFont('cambriacambriamath', 25, BOLD)
fontQuiz = pygame.font.SysFont('cambriacambriamath', 30, BOLD)
WHITE = (200, 200, 200)
GREEN = (166, 26, 0)
# q1_choice1 = pygame.image.load("projects/PyGame/pictures/buttons/quiz1_choice1.png")
# q1_choice2 = pygame.image.load("projects/PyGame/pictures/buttons/quiz1_choice2.png")
# q1_choice3 = pygame.image.load("projects/PyGame/pictures/buttons/quiz1_choice3.png")
# q1_choice4 = pygame.image.load("projects/PyGame/pictures/buttons/quiz1_choice4.png")
# # ================================= QUIZ 2 =======================================
# quiz2 = pygame.image.load("projects/PyGame/pictures/background/quiz2.png")
# bg_quiz2 = pygame.transform.scale(quiz2, (WIDTH, HEIGHT))
# q2_choice1 = pygame.image.load("projects/PyGame/pictures/buttons/quiz2_choice1.png")
# q2_choice2 = pygame.image.load("projects/PyGame/pictures/buttons/quiz2_choice2.png")
# # ================================= QUIZ 3 =======================================
# quiz3 = pygame.image.load("projects/PyGame/pictures/background/quiz3.png")
# bg_quiz3 = pygame.transform.scale(quiz3, (WIDTH, HEIGHT))
# q3_choice1 = pygame.image.load("projects/PyGame/pictures/buttons/quiz3_choice1.png")
# q3_choice2 = pygame.image.load("projects/PyGame/pictures/buttons/quiz3_choice2.png")
# q3_choice3 = pygame.image.load("projects/PyGame/pictures/buttons/quiz3_choice3.png")
# q3_choice4 = pygame.image.load("projects/PyGame/pictures/buttons/quiz3_choice4.png")
# # ================================= QUIZ 4 =======================================
# quiz4 = pygame.image.load("projects/PyGame/pictures/background/quiz4.png")
# bg_quiz4 = pygame.transform.scale(quiz4, (WIDTH, HEIGHT))
# q4_choice1 = pygame.image.load("projects/PyGame/pictures/buttons/quiz4_choice1.png")
# q4_choice2 = pygame.image.load("projects/PyGame/pictures/buttons/quiz4_choice2.png")
# # ================================= QUIZ 5 =======================================
# quiz5 = pygame.image.load("projects/PyGame/pictures/background/quiz5.png")
# bg_quiz5 = pygame.transform.scale(quiz5, (WIDTH, HEIGHT))
# q5_choice1 = pygame.image.load("projects/PyGame/pictures/buttons/quiz5_choice1.png")
# q5_choice2 = pygame.image.load("projects/PyGame/pictures/buttons/quiz5_choice2.png")
# q5_choice3 = pygame.image.load("projects/PyGame/pictures/buttons/quiz5_choice3.png")
# q5_choice4 = pygame.image.load("projects/PyGame/pictures/buttons/quiz5_choice4.png")
# ================================ [ START ] =====================================
pygame.display.set_caption("PROGUIZER")  # set head
pygame.display.set_icon(pygame.image.load("projects\PyGame\pictures\objects\icon.png"))

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

# def text(font, text, color):
#     return font.render(text, 1, color)

class Text(pygame.sprite.Sprite):  
    def __init__(self, x, y, image, width, hight, scale): 
        pygame.sprite.Sprite.__init__(self)
        # pygame.font.init
        self.image = pygame.transform.scale(choicebg, (int(width * scale), int(hight * scale)))  # rescale of button
        
        # choice1 = Text(100, 575, hello)
        # self.image = text
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y)
        # self.drawGameBt()
        self.clicked = False
        buttonsGameGroup.add(self)

    def drawGameBt(self, txt_choice, txt_quiz, pt_x, pt_y):
        # bt = pygame.transform.scale(choicebg, [self.rect.x, self.rect.x])
        choicetxt = fontChoice.render(txt_choice, 1, GREEN)
        choicequiz = fontQuiz.render(txt_quiz, 1, WHITE)

        screen.blit(self.image, [pt_x, pt_y])
        screen.blit(choicequiz, [WIDTH/2, 50])
        screen.blit(choicetxt, [pt_x + 20, pt_y + 45])
        # self.rect = [self.rect.x - wchoicebg, self.rect.y - hchoice]

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
        self.heart0 = pygame.transform.scale(self.heart, (int(self.heart.get_width() * scale), int(self.heart.get_height() * scale)))
        # self.rectx = self.char0_1.get_rect()
        self.rectht = self.heart0.get_rect()
        # self.rectx.center = (x, y)
        self.rectht.center = (x, y)

class ClassAnimeTimmie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imgCharCompute =[]
        self.imgCharHurt =[]
        self.imgCharCompute.append(ani_timmy)
        self.imgCharCompute.append(ani_timmycom)

        self.imgCharHurt.append(ani_timmy)
        self.imgCharHurt.append(ani_timmyhurt)

        self.current_imgCharCompute = 0
        self.current_imgCharHurt = 0

        self.compute_animation = False
        self.hurt_animation = False

        self.image = self.imgCharCompute[self.current_imgCharCompute]
        self.image = self.imgCharHurt[self.current_imgCharHurt]

        self.checkAni = False
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
    
    def compute(self):
        self.compute_animation = True

    def hurt(self):
        self.hurt_animation = True

    def update(self, speed): # speed ต้องบวกได้จำนวนเต็ม 0++
        if self.compute_animation == True:
            self.current_imgCharCompute += speed
            if int(self.current_imgCharCompute) >= len(self.imgCharCompute):
                self.current_imgCharCompute = 1
                # self.compute_animation = False
                self.checkAni = True
                print("enough")
            self.image = self.imgCharCompute[int(self.current_imgCharCompute)]
        if self.hurt_animation == True:
            self.current_imgCharHurt += speed
            if int(self.current_imgCharHurt) >= len(self.imgCharHurt):
                self.current_imgCharHurt = 1
                # self.compute_animation = False
                self.checkAni = True
            self.image = self.imgCharHurt[int(self.current_imgCharHurt)]
        

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

class quizTimmie(pygame.sprite.Sprite):
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
    monQ1 = ClassMonster(690, 223)
    monster_group.add(monQ1)

def init_timmie():
    global timmie_group, timmieAni
    timmie_group = pygame.sprite.Group()
    timmieAni = ClassAnimeTimmie(270, 270)
    timmie_group.add(timmieAni)
            
def threeHeart():    
    heart1 = ClassHeart(50, 45, 0.5)
    heart2 = ClassHeart(100, 45, 0.5)
    heart3 = ClassHeart(150, 45, 0.5)
    screen.blit(heart1.heart0, heart1.rectht)
    screen.blit(heart2.heart0, heart2.rectht)
    screen.blit(heart3.heart0, heart3.rectht)


def twoHeart():
        
    heart1 = ClassHeart(50, 45, 0.5)
    heart2 = ClassHeart(100, 45, 0.5)
    screen.blit(heart1.heart0, heart1.rectht)
    screen.blit(heart2.heart0, heart2.rectht)

def oneHeart():    
    heart1 = ClassHeart(50, 45, 0.5)
    screen.blit(heart1.heart0, heart1.rectht)

def checkHeart():
    global nowHt
    if(nowHt == 3):
        threeHeart()
    elif(nowHt == 2):
        twoHeart()
    elif(nowHt == 1):
        oneHeart()
    elif(nowHt == 0):
        screen.blit(bg_ghost, (0, 0))
        

def func_menu():
    global button_start, button_exit
    screen.blit(bg_menu, (0, 0))  # used bg
    button_start = ClassMenuButton((WIDTH/2 - bt_start.get_width()/2), 250, bt_start, bt_start.get_width(), bt_start.get_height(), 0.95)
    button_exit = ClassMenuButton((WIDTH/2 - bt_exit.get_width()/2), 400, bt_exit, bt_exit.get_width(), bt_exit.get_height(), 0.95)
    buttonsMenuGroup.draw(screen)  # draw group buttons


# for i in data['question']:
#     print(data['question'][i].get('question'))
# Closing file

# nextQuestion = 1

def quiz():
    pt_x = 50
    pt_y = 600
    checkQuestion = 1
    # position = (100, 580)
    for i in data['allThing']:
        # print(i)
        if (nextQuestion == checkQuestion) : 
            for y in data['allThing'][i]['allChoice'] :
                # print(y)
                choiceButton = Text(pt_x, pt_y, choicebg, choicebg.get_width(), choicebg.get_height(), 1.2)
                # read line ****
                txt_quiz = data['allThing'][i].get('question')
                txt_choice = data['allThing'][i]['allChoice'][y].get('choice')
                txt_check = data['allThing'][i]['allChoice'][y].get('check')
                choiceButton.drawGameBt(txt_choice, txt_quiz, pt_x, pt_y)
                choiceButList.append(choiceButton)
                checkChoiceButList.append(txt_check)
                pt_x += 300
            checkQuestion += 1
            # break
        else :
            checkQuestion += 1 
            # break
        
        # a_data.setdefault(i)
    
    file.close()

# def quiz():
#     pt_x = 100
#     pt_y = 620
#     # position = (100, 580)
#     for i in range(0, 5):
#         choice = Text(pt_x, pt_y, choicebg, choicebg.get_width(), choicebg.get_height(), 1)
#         # read line ****
#         text = data['Q5'][i]
#         choice.drawGameBt(text,pt_x, pt_y)
#         choiceList.append(choice)
#         pt_x += 300
#         # a_data.setdefault(i)


def func_quiz():
    # , choice2, choice3, choice4
    screen.blit(bg_quiz1, (0, 0))
    timmie = quizTimmie(270, 270)
    timmie.draw()
    monster_group.draw(screen)
    #font
    # hello = text(font, "Hello", BLACK)
    # hello = font.render("text", 1, WHITE)
    # choice1 = Text(100, 575, hello)
    # choice1.drawGameBt()
    quiz()
    # choice1 = Text(100, 575, choicebg, choicebg.get_width(), choicebg.get_height(), 0.75)
    # choice2 = ClassGameButton(300, 575, q1_choice2, q1_choice2.get_width(), q1_choice2.get_height(), 0.75)
    # choice3 = ClassGameButton(500, 575, q1_choice3, q1_choice3.get_width(), q1_choice3.get_height(), 0.75)
    # choice4 = ClassGameButton(700, 575, q1_choice4, q1_choice4.get_width(), q1_choice4.get_height(), 0.75)
    # buttonsGameGroup.draw(screen)
    # choice1.drawGameBt()
    # screen.blit(choice1, (100, 575))
    checkHeart()    

# def func_quiz2():
#     for i in buttonsGameGroup: # kill attribute in group 'buttonsGameGroup'
#         i.kill()
#     global choice1, choice2
#     screen.blit(bg_quiz2, (0, 0))
#     timmie = quizTimmie(130, 225)
#     timmie.draw()
#     monster_group.draw(screen)
#     choice1 = ClassGameButton(100, 575, q2_choice1, q2_choice1.get_width(), q2_choice1.get_height(), 0.75)
#     choice2 = ClassGameButton(300, 575, q2_choice2, q2_choice2.get_width(), q2_choice2.get_height(), 0.75)
#     buttonsGameGroup.draw(screen)
#     checkHeart()

# def func_quiz3():
#     global choice1, choice2, choice3, choice4
#     for i in buttonsGameGroup: # kill attribute in group 'buttonsGameGroup'
#         i.kill()
#     screen.blit(bg_quiz3, (0, 0))
#     timmie = quizTimmie(130, 225)
#     timmie.draw()
#     monster_group.draw(screen)
#     choice1 = ClassGameButton(100, 575, q3_choice1, q3_choice1.get_width(), q3_choice1.get_height(), 0.75)
#     choice2 = ClassGameButton(300, 575, q3_choice2, q3_choice2.get_width(), q3_choice2.get_height(), 0.75)
#     choice3 = ClassGameButton(500, 575, q3_choice3, q3_choice3.get_width(), q3_choice3.get_height(), 0.75)
#     choice4 = ClassGameButton(700, 575, q3_choice4, q3_choice4.get_width(), q3_choice4.get_height(), 0.75)
#     buttonsGameGroup.draw(screen)
#     checkHeart()

# def func_quiz4():
#     for i in buttonsGameGroup: # kill attribute in group 'buttonsGameGroup'
#         i.kill()
#     global choice1, choice2
#     screen.blit(bg_quiz4, (0, 0))
#     timmie = quizTimmie(130, 225)
#     timmie.draw()
#     monster_group.draw(screen)
#     choice1 = ClassGameButton(100, 575, q4_choice1, q4_choice1.get_width(), q4_choice1.get_height(), 0.75)
#     choice2 = ClassGameButton(300, 575, q4_choice2, q4_choice2.get_width(), q4_choice2.get_height(), 0.75)
#     buttonsGameGroup.draw(screen)
#     checkHeart()

# def func_quiz5():
#     global choice1, choice2, choice3, choice4
#     for i in buttonsGameGroup: # kill attribute in group 'buttonsGameGroup'
#         i.kill()
#     screen.blit(bg_quiz5, (0, 0))
#     timmie = quizTimmie(130, 225)
#     timmie.draw()
#     monster_group.draw(screen)
#     choice1 = ClassGameButton(100, 575, q5_choice1, q5_choice1.get_width(), q5_choice1.get_height(), 0.75)
#     choice2 = ClassGameButton(300, 575, q5_choice2, q5_choice2.get_width(), q5_choice2.get_height(), 0.75)
#     choice3 = ClassGameButton(500, 575, q5_choice3, q5_choice3.get_width(), q5_choice3.get_height(), 0.75)
#     choice4 = ClassGameButton(700, 575, q5_choice4, q5_choice4.get_width(), q5_choice4.get_height(), 0.75)
#     buttonsGameGroup.draw(screen)
#     checkHeart()

def main_animation():
    global getdamage
    running = True    
    init_timmie()
    init_monster()      
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                if (getdamage):
                    timmieAni.hurt() 
                    getdamage = False
                else:
                    timmieAni.compute()
            
        screen.blit(bg_quiz1, (0,0))
        timmie_group.draw(screen) # draw charactor
        monster_group.draw(screen)
        timmie_group.update(0.2)
        print(timmieAni.checkAni)
        if(timmieAni.checkAni):
            if (nextQuestion == (len(data['allThing'])+1)):
                print("Score is",score)
                print("Omedetou !!!! > () < !!!!")
                pygame.quit()
                sys.exit()
            else:
                main_quiz()
            # elif (next == 2):
            #     print("now is",next)
            #     main_quiz2()
            # elif (next == 3):
            #     print("now is",next)
            #     main_quiz3()
            # elif (next == 4):
            #     print("now is",next)
            #     main_quiz4()
            # elif (next == 5):
            #     print("now is",next)
            #     main_quiz5()
            # else:
            #     print("now is",next)
            #     print("Baka yarouu!")
            #     pygame.quit()
            #     sys.exit()
            
        pygame.display.update()
        clock.tick(15)

# =================================  MENU  =======================================
def main_menu():
    global nextQuestion, nowHt
    running = True
    func_menu()
    while running:
        for event in pygame.event.get():  # check circumstance in the game
            if (event.type == pygame.QUIT):  # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(button_start.checkClick()):
                    button_start.update()
                    button_exit.update()
                    print("Start")
                    print("now is",nextQuestion)
                    nextQuestion += 1
                    nowHt = 3
                    main_animation() # animetion
                    # checkHeart()
                    print("I'm just going a main_quiz1")
                elif(button_exit.checkClick()):
                    print("Exit")
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def checkChoice():
    global nextQuestion, nowHt, score, getdamage
    print(choiceButList)
    print(checkChoiceButList)
    # for i in range(0, len(choiceButList)):
    if (choiceButList[0].checkClickgm()):
        if (checkChoiceButList[0] == "True"):
            print("clicked TRUE")
            nextQuestion += 1
            score += 1
        else:
            print("clicked FALSE")
            nowHt -= 1
            nextQuestion += 1 
            getdamage = True
    elif (choiceButList[1].checkClickgm()):
        if (checkChoiceButList[1] == "True"):
            print("clicked TRUE")
            nextQuestion += 1
            score += 1
        else:
            print("clicked FALSE")
            nowHt -= 1
            nextQuestion += 1
            getdamage = True  
    elif (choiceButList[2].checkClickgm()):
        if (checkChoiceButList[2] == "True"):
            print("clicked TRUE")
            nextQuestion += 1
            score += 1
        else:
            print("clicked FALSE")
            nowHt -= 1
            nextQuestion += 1 
            getdamage = True 
    elif (choiceButList[3].checkClickgm()):
        if (checkChoiceButList[3] == "True"):
            print("clicked TRUE")
            nextQuestion += 1
            score += 1
        else:
            print("clicked FALSE")
            nowHt -= 1
            nextQuestion += 1
            getdamage = True  
   
    # else:
    #     if (choiceButList[0].checkClickgm() or choiceButList[1].checkClickgm() or choiceButList[2].checkClickgm() or choiceButList[3].checkClickgm()):
    #     print("clicked FALSE")
    #     nowHt -= 1
    #     nextQuestion += 1
    for i in range(0,len(choiceButList)):
        choiceButList[i].updateGameBt()
    
    # choiceButList[1].updateGameBt()
    # choiceButList[2].updateGameBt()
    # choiceButList[3].updateGameBt()
    choiceButList.clear()
    checkChoiceButList.clear()
    # choiceButList.remove
    print(checkChoiceButList)
    main_animation()
    # print(nextQuestion)
    
    # else :
    #     print("clicked FALSE")
    #     pygame.quit()
    #     sys.exit()



# ================================= QUIZ 1 =======================================
def main_quiz():
    global next, nowHt
    running = True
    func_quiz()
    while running:
        for event in pygame.event.get():  # check circumstance in the game
            if (event.type == pygame.QUIT):  # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                print("Click --> check")
                checkChoice()
                # if(choiceList[0].checkClickgm()):
                #     # print("false")
                #     print("clicked choice1")
                #     pygame.quit()
                #     sys.exit()
                #     # next = 1
                #     # nowHt -= 1
                #     # main_animation()
                # elif (choiceList[1].checkClickgm()):
                # #     choice1.updateGameBt()
                # #     choice2.updateGameBt()
                # #     choice3.updateGameBt()
                # #     choice4.updateGameBt()
                #         print("clicked choice2")
                #         pygame.quit()
                #         sys.exit()
                #     next = 2
                #     main_animation()
                #     print("false")
                # elif (choice3.checkClickgm()):
                #     print("false")
                #     next = 1
                #     nowHt -= 1
                #     main_animation()
                # elif (choice4.checkClickgm()):
                #     print("false")
                #     next = 1
                #     nowHt -= 1
                #     main_animation()
            else:
                continue
    
        pygame.display.update()

# # ================================= QUIZ 2 =======================================
# def main_quiz2():
#     global next, nowHt
#     running = True
    
#     while running:
#         func_quiz2()
        
#         for event in pygame.event.get():  # check circumstance in the game
#             if (event.type == pygame.QUIT):  # when press botton an exit
#                 pygame.quit()
#                 sys.exit()
#             if (event.type == pygame.MOUSEBUTTONDOWN):
#                 if(choice1.checkClickgm()):
#                     choice1.updateGameBt()
#                     choice2.updateGameBt()
#                     print("true")
#                     next = 3
#                     main_animation()
#                 elif (choice2.checkClickgm()):
#                     print("false")
#                     next = 2
#                     nowHt -= 1
#                     main_animation()
#                 else:
#                     continue

#         pygame.display.update()

# # ================================= QUIZ 3 =======================================
# def main_quiz3():
#     global next, nowHt
#     running = True
    
#     while running:
#         func_quiz3()
        
#         for event in pygame.event.get():  # check circumstance in the game
#             if (event.type == pygame.QUIT):  # when press botton an exit
#                 pygame.quit()
#                 sys.exit()
#             if (event.type == pygame.MOUSEBUTTONDOWN):
#                 if(choice1.checkClickgm()):
#                     print("false")
#                     next = 3
#                     nowHt -= 1
#                     main_animation()
#                 elif (choice2.checkClickgm()):
#                     print("false")
#                     next = 3
#                     nowHt -= 1
#                     main_animation()
#                 elif (choice3.checkClickgm()):
#                     choice1.updateGameBt()
#                     choice2.updateGameBt()
#                     choice3.updateGameBt()
#                     choice4.updateGameBt()
#                     print("true")
#                     next = 4
#                     main_animation()
#                 elif (choice4.checkClickgm()):
#                     print("false")
#                     next = 3
#                     nowHt -= 1
#                     main_animation()
#                 else:
#                     continue

#         pygame.display.update()

# # ================================= QUIZ 4 =======================================
# def main_quiz4():
#     global next, nowHt
#     running = True
    
#     while running:
#         func_quiz4()
        
#         for event in pygame.event.get():  # check circumstance in the game
#             if (event.type == pygame.QUIT):  # when press botton an exit
#                 pygame.quit()
#                 sys.exit()
#             if (event.type == pygame.MOUSEBUTTONDOWN):
#                 if(choice1.checkClickgm()):
#                     choice1.updateGameBt()
#                     choice2.updateGameBt()
#                     print("true")
#                     next = 5
#                     main_animation()
#                 elif (choice2.checkClickgm()):
#                     print("false")
#                     next = 4
#                     nowHt -= 1
#                     main_animation()
#                 else:
#                     continue

#         pygame.display.update()  

# # ================================= QUIZ 5 =======================================
# def main_quiz5():
#     global next, nowHt
#     running = True

#     while running:
#         func_quiz5()
        
#         for event in pygame.event.get():  # check circumstance in the game
#             if (event.type == pygame.QUIT):  # when press botton an exit
#                 pygame.quit()
#                 sys.exit()
#             if (event.type == pygame.MOUSEBUTTONDOWN):
#                 if(choice1.checkClickgm()):
#                     print("false")
#                     nowHt =- 1
#                     main_animation()
#                 elif (choice2.checkClickgm()):
#                     print("false")
#                     nowHt -= 1
#                     main_animation()
#                 elif (choice3.checkClickgm()):
#                     choice1.updateGameBt()
#                     choice2.updateGameBt()
#                     choice3.updateGameBt()
#                     choice4.updateGameBt()
#                     print("true")
#                     # now = 5
#                     print("Congrat!!")
#                     pygame.quit()
#                     sys.exit()
#                 elif (choice4.checkClickgm()):
#                     print("false")
#                     nowHt -= 1
#                     main_animation()
#                 else:
#                     continue

#         pygame.display.update() 

# ========== RUN ==========
main_menu()