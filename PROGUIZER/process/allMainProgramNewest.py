#from turtle import update
from operator import and_
from tkinter.font import BOLD
from turtle import goto, width
import webbrowser
import pygame
import sys
# import pandas
import json

from _initObject.FileAndPictureForPGZ import fileForPGZ
from FileAndPictureForPGZ import pictureForPGZ

pygame.init()  
pygame.font.init()

WIDTH = 1250
HEIGHT = 750

fileOpened = fileForPGZ()
pictureOpened = pictureForPGZ()

def init_values():
    global animation_cha, animation_chafight, animation_chahurt, nowHt
    global nextQuestion, a_data, choiceButList, checkChoiceButList, score, getdamage
    global character, checkCharacter, characterNow, goToShowKey
    global txt_choice, txt_quiz, txt_web

    nowHt = 3
    nextQuestion = 0 # now where am I 
    a_data = {}
    choiceButList = []
    checkChoiceButList = []
    score = 0
    getdamage = False
    character = 0
    checkCharacter = 0
    characterNow = 1
    goToShowKey = 0

# ================================ [ START ] =====================================
pygame.display.set_caption("PROGUIZER")  # set head
# pygame.display.set_icon(pygame.image.load("component/objects\objs\icon.png"))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # set a size of display
buttonsMenuGroup = pygame.sprite.Group()
buttonsGameGroup = pygame.sprite.Group()


class ClassMenuButton(pygame.sprite.Sprite):  # create class button
    def __init__(self, x, y, image, width, hight, scale):
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

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

class Text(pygame.sprite.Sprite):  
    def __init__(self, x, y, image, width, hight, scale): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pictureOpened.bg_choice, (int(width * scale), int(hight * scale)))  # rescale of button      
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y)
        self.clicked = False
        buttonsGameGroup.add(self)

    def drawGameBt(self, txt_choice, txt_quiz, pt_x, pt_y):
        screen.blit(self.image, [pt_x, pt_y])
        # ิblit txt
        blit_text(screen, txt_quiz, (WIDTH/2 - 250, 50), pictureOpened.font_quiz, pictureOpened.color_fQuiz)
        blit_text(screen, txt_choice, (pt_x + 50, pt_y + 25), pictureOpened.font_choice, pictureOpened.color_fChoice)

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


# ================================  MONSTER  =====================================
class ClassAniMonster_die(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        super().__init__()
        self.imgMon =[]
        self.animation_monDie =[]
        if (nextQuestion == 2):
            self.imgMon.append(pictureOpened.q1_1)
            self.imgMon.append(pictureOpened.q1_2)
        elif (nextQuestion == 4):
            self.imgMon.append(pictureOpened.q3_1)
            self.imgMon.append(pictureOpened.q3_2)
            self.imgMon.append(pictureOpened.q3_3)
            self.imgMon.append(pictureOpened.q3_4)
        elif (nextQuestion == 7):
            self.imgMon.append(pictureOpened.q6_1)
            self.imgMon.append(pictureOpened.q6_2)
            self.imgMon.append(pictureOpened.q6_3)
            self.imgMon.append(pictureOpened.q6_4)
            self.imgMon.append(pictureOpened.q6_5)
            self.imgMon.append(pictureOpened.q6_6)
            self.imgMon.append(pictureOpened.q6_7)
            self.imgMon.append(pictureOpened.q6_8)
            self.imgMon.append(pictureOpened.q6_9)
            self.imgMon.append(pictureOpened.q6_10)
            self.imgMon.append(pictureOpened.q6_11)
            self.imgMon.append(pictureOpened.q6_12)
            self.imgMon.append(pictureOpened.q6_13)
            self.imgMon.append(pictureOpened.q6_14)
            self.imgMon.append(pictureOpened.q6_15)
            self.imgMon.append(pictureOpened.q6_16)
        elif (nextQuestion == 9):
            self.imgMon.append(pictureOpened.q8_1)
            self.imgMon.append(pictureOpened.q8_2)
        elif (nextQuestion == 12):
            self.imgMon.append(pictureOpened.q11_1)
            self.imgMon.append(pictureOpened.q11_2)
            self.imgMon.append(pictureOpened.q11_3)
            self.imgMon.append(pictureOpened.q11_4)
            self.imgMon.append(pictureOpened.q11_5)
            self.imgMon.append(pictureOpened.q11_6)
            self.imgMon.append(pictureOpened.q11_7)
        elif (nextQuestion == 15):
            self.imgMon.append(pictureOpened.q14_1)
            self.imgMon.append(pictureOpened.q14_2)
            self.imgMon.append(pictureOpened.q14_3)
            self.imgMon.append(pictureOpened.q14_4)
            self.imgMon.append(pictureOpened.q14_5)
            self.imgMon.append(pictureOpened.q14_6)
            self.imgMon.append(pictureOpened.q14_7)
        elif (nextQuestion == 20):
            self.imgMon.append(pictureOpened.q19_1)
            self.imgMon.append(pictureOpened.q19_2)
            self.imgMon.append(pictureOpened.q19_3)
            self.imgMon.append(pictureOpened.q19_4)
            self.imgMon.append(pictureOpened.q19_5)
            self.imgMon.append(pictureOpened.q19_6)
            self.imgMon.append(pictureOpened.q19_7)
            self.imgMon.append(pictureOpened.q19_8)
        for i in self.imgMon:
            mon = pygame.transform.scale(i, (int(i.get_width() * scale), int(i.get_height() * scale)))
            self.animation_monDie.append(mon)
        
        self.current_imgChar = 0
        self.death_animation = False
        self.image = self.animation_monDie[self.current_imgChar]
        self.checkAni = False
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
    
    def death(self):
        self.death_animation = True

    def update(self, speed): # speed ต้องบวกได้จำนวนเต็ม 0++
        if self.death_animation == True:
            self.current_imgChar += speed
            if int(self.current_imgChar) >= len(self.animation_monDie):
                self.current_imgChar = 1
                self.checkAni = True
                print("enough")
        
        self.image = self.animation_monDie[int(self.current_imgChar)]

class ClassMonster(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width, hight, scale):
        super().__init__()
        self.image = pygame.transform.scale(image, (int(width * scale), int(hight * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

def init_monster(image_mon, x, y, scale):
    global monster_group, monster
    monster_group = pygame.sprite.Group()
    monster = ClassMonster(x, y, image_mon, image_mon.get_width(), image_mon.get_height(), scale)
    monster_group.add(monster)

def change_monster():
    if(nextQuestion <= 1):
        image_mon = pictureOpened.q1_monster
        x, y, scale = 750, 280, 0.70
    elif(nextQuestion <= 3):
        if(nextQuestion == 2):
            image_mon = pictureOpened.q2_monster
        else:
            image_mon = pictureOpened.q3_monster
        x, y, scale = 750, 280, 0.90
    elif(nextQuestion <= 6):
        if(nextQuestion == 4):
            image_mon = pictureOpened.q4_monster
        elif(nextQuestion == 5):
            image_mon = pictureOpened.q5_monster
        else:
            image_mon = pictureOpened.q6_monster
        x, y, scale = 750, 290, 0.70
    elif(nextQuestion <= 8):
        image_mon = pictureOpened.q7_monster
        x, y, scale = 750, 290, 0.75
    elif(nextQuestion <= 11):
        if(nextQuestion == 9):
            image_mon = pictureOpened.q9_monster
        else:
            image_mon = pictureOpened.q10_monster
        x, y, scale = 750, 275, 0.35
    elif(nextQuestion <= 14):
        if(nextQuestion == 14):
            image_mon = pictureOpened.q14_monster
        else:
            image_mon = pictureOpened.q12_monster
        x, y, scale = 690, 62, 0.65
    elif(nextQuestion <= 19):
        if(nextQuestion == 15):
            image_mon = pictureOpened.q15_monster
        elif(nextQuestion == 16):
            image_mon = pictureOpened.q16_monster
        elif(nextQuestion == 17):
            image_mon = pictureOpened.q17_monster
        elif(nextQuestion == 18):
            image_mon = pictureOpened.q18_monster
        else:
            image_mon = pictureOpened.q19_monster
        x, y, scale = 690, 223, 0.55
    elif(nextQuestion <= 20):
        x, y, scale = 800, 270, 0.25
        if(character == 0):
            image_mon = pictureOpened.q20_1_monster
        elif(character == 1):
            image_mon = pictureOpened.q20_2_monster
    if (nextQuestion < (len(fileOpened.data['allThing'])+1)):
        init_monster(image_mon, x, y, scale)

# ============================== key answer =====================================
def showKey():
    global goToShowKey, score, nextQuestion, getdamage, nowHt, nextButton, running, nextButton, keyButton, txt_web
    running = True
    if goToShowKey == 1:# False answer
        nowHt -= 1
        while running:
            screen.blit(pictureOpened.bg_ghost, (0, 0))
            nextButton = ClassMenuButton(500, 650, pictureOpened.bt_start, 150, 50, 1.25)
            keyButton = ClassMenuButton(500, 325, pictureOpened.bt_d, pictureOpened.bt_d.get_width(), pictureOpened.bt_d.get_height(), 1)
            nextButton.draw()
            keyButton.draw()
            getdamage = True
            for event in pygame.event.get():
                if event ==  pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (nextButton.checkClick()):
                    nextQuestion += 1
                    nextButton.update()
                    running = False
                elif(keyButton.checkClick()):
                    # for i in fileOpened.data["allThing"]:
                        # if nextQuestion == 
                    webbrowser.open(txt_web)
                pygame.display.update()
    elif goToShowKey == 0:
        nextQuestion += 1
        score += 1

# =============================== show score =========================================
def showScore():
    global running, scoreButton, homeButton, closeButton
    running = True
    while running:
        screen.blit(pictureOpened.bg_menu, (0, 0))
        scoreButton = ClassMenuButton(500, 650, pictureOpened.bt_start, 150, 50, 1.25)
        scoreButton.draw()
        homeButton = ClassMenuButton(500, 650, pictureOpened.bt_a, 150, 50, 1.25)
        closeButton = ClassMenuButton(700, 650, pictureOpened.bt_d, 150, 50, 1.25)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
                pygame.exit()
                sys.exit()
        if (nowHt == 0):
            screen.blit(pictureOpened.bg_ghost, (0, 0))
            homeButton.draw()
            closeButton.draw()
            if (homeButton.checkClick()):
                for i in buttonsMenuGroup:
                    i.kill()
                homeButton.update()
                closeButton.update()
                running = False
                main_menu()
            elif (closeButton.checkClick()):
                pygame.quit()
                sys.exit()

        pygame.display.update()

# ===============================  CHARACTER  ====================================
class ClassAnimeCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imgCharCompute =[]
        self.imgCharHurt =[]
        self.imgCharCompute.append(animation_cha)
        self.imgCharCompute.append(animation_chafight)

        self.imgCharHurt.append(animation_cha)
        self.imgCharHurt.append(animation_chahurt)

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
                self.checkAni = True
                print("enough")
            self.image = self.imgCharCompute[int(self.current_imgCharCompute)]

        if self.hurt_animation == True:
            self.current_imgCharHurt += speed
            if int(self.current_imgCharHurt) >= len(self.imgCharHurt):
                self.current_imgCharHurt = 1
                self.checkAni = True
            self.image = self.imgCharHurt[int(self.current_imgCharHurt)]
        
class quizCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = animation_chafight
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]   
    def draw(self):
        screen.blit(self.image,[self.rect.x, self.rect.y])

def init_character():
    global timmie_group, timmieAni
    timmie_group = pygame.sprite.Group()
    timmieAni = ClassAnimeCharacter(270, 270)
    timmie_group.add(timmieAni)


# =================================  HEART  ======================================
class ClassHeart(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.heart = pygame.image.load('PROGUIZER\component\objects\objs\heart.png')
        self.heart0 = pygame.transform.scale(self.heart, (int(self.heart.get_width() * scale), int(self.heart.get_height() * scale)))
        self.rectht = self.heart0.get_rect()
        self.rectht.center = (x, y)

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
        showScore()

def quiz():
    global txt_web
    pt_x = 20
    pt_y = 583
    countToChange_pt_y = 0
    checkNextQuestion = 1
    for i in fileOpened.data['allThing']:
        if (nextQuestion == checkNextQuestion) : 
            for y in fileOpened.data['allThing'][i]['allChoice'] :
                choiceButton = Text(pt_x, pt_y, pictureOpened.bg_choice, pictureOpened.bg_choice.get_width(), pictureOpened.bg_choice.get_height(), 1)
                # read line
                txt_quiz = fileOpened.data['allThing'][i].get('question')
                txt_web = fileOpened.data["allThing"][i].get("web")
                txt_choice = fileOpened.data['allThing'][i]['allChoice'][y].get('choice')
                txt_check = fileOpened.data['allThing'][i]['allChoice'][y].get('check')
                choiceButton.drawGameBt(txt_choice, txt_quiz, pt_x, pt_y)
                choiceButList.append(choiceButton)
                checkChoiceButList.append(txt_check)
                if (countToChange_pt_y >= 1):
                    pt_x = 20
                    pt_y += 85
                    countToChange_pt_y = 0
                else: 
                    pt_x += 615
                    countToChange_pt_y = 1
            checkNextQuestion += 1
        else :
            checkNextQuestion += 1 
    fileOpened.file.close()

def checkBgQuiz():
    if(nextQuestion <= 7):
        bg_quiz = pictureOpened.bg_quizLv1
    elif(nextQuestion <= 14):
        bg_quiz = pictureOpened.bg_quizLv2
    else:
        bg_quiz = pictureOpened.bg_quizLv3
    return bg_quiz

def init_Animonster():
    global killMon, animation_monDie
    animation_monDie = pygame.sprite.Group()
    if (nextQuestion == 2):
        x, y, scale = 750, 280, 0.70        
    elif (nextQuestion == 4):
        x, y, scale = 750, 280, 0.90
    elif (nextQuestion == 7):
        x, y, scale = 750, 290, 0.70
    elif (nextQuestion == 9):
        x, y, scale = 750, 290, 0.75
    elif (nextQuestion == 12):
        x, y, scale = 750, 275, 0.35
    elif (nextQuestion == 15):
        x, y, scale = 690, 62, 0.65
    elif (nextQuestion == 20):
        x, y, scale = 690, 223, 0.55  
    killMon = ClassAniMonster_die(x, y, scale)
    animation_monDie.add(killMon)

def monster_animation():
    running = True
    init_Animonster()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                pygame.quit()
                sys.exit()
            else:
                killMon.death() 

        bg_quiz = checkBgQuiz()    
        screen.blit(bg_quiz, (0,0))
        timmie_group.draw(screen) # draw charactor
        animation_monDie.draw(screen)
        animation_monDie.update(0.2)
        print(timmieAni.checkAni)
        if(killMon.checkAni):
            # main_quiz()
            running = False
        pygame.display.update()
        clock.tick(15)

def func_quiz():
    bg_quiz = checkBgQuiz()
    screen.blit(bg_quiz, (0, 0))
    timmie = quizCharacter(270, 270)
    timmie.draw()
    monster_group.draw(screen)
    quiz()
    checkHeart()    

def main_animation():
    global getdamage
    running = True    
    init_character()
    # init_monster()      
    change_monster()
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
        bg_quiz = checkBgQuiz()    
        screen.blit(bg_quiz, (0,0))
        timmie_group.draw(screen) # draw charactor
        timmie_group.update(0.2)
        print(timmieAni.checkAni)
        if(timmieAni.checkAni):
            # monster_group.draw(screen)
            if (nextQuestion == (len(fileOpened.data['allThing'])+1)):
                print("Score is",score)
                print("Omedetou !!!! > () < !!!!")
                pygame.quit()
                sys.exit()
            elif ((nextQuestion == 2) or (nextQuestion == 4) or (nextQuestion == 7) or (nextQuestion == 9) or (nextQuestion == 12) or (nextQuestion == 15) or (nextQuestion == 20)):
                monster_animation()
                monster_group.draw(screen)
                main_quiz()
            else:
                monster_group.draw(screen)
                main_quiz()
        pygame.display.update()
        clock.tick(15)

def changeCharacter():
    global checkCharacter, characterNow
    if checkCharacter % 2 == 0:
        characterNow = 1
        screen.blit(pictureOpened.ani_timmy, ((WIDTH/2 - 40), 250))
        screen.blit(pictureOpened.name_timmy, ((WIDTH/4 + 183), 400))
    elif checkCharacter % 2 == 1:
        characterNow = 2
        screen.blit(pictureOpened.ani_ohmmy, ((WIDTH/2 - 40), 250))
        screen.blit(pictureOpened.name_ohmmy, ((WIDTH/4 + 183), 400))

def main_Character():
    global animation_cha, animation_chafight, animation_chahurt
    if(character == 0):
        animation_cha = pictureOpened.ani_timmy
        animation_chafight = pictureOpened.ani_timmyfight
        animation_chahurt = pictureOpened.ani_timmyhurt
    elif(character == 1):
        animation_cha = pictureOpened.ani_ohmmy
        animation_chafight = pictureOpened.ani_ohmmyfight
        animation_chahurt = pictureOpened.ani_ohmmyhurt

# =================================  MENU  =======================================
def func_menu():
    global button_start, button_exit
    screen.blit(pictureOpened.bg_menu, (0, 0))  # used bg
    # screen.blit(logo, ((WIDTH/2 - 500), 10))
    button_logo = ClassMenuButton((WIDTH/2 - 195), 5, pictureOpened.logo, pictureOpened.logo.get_width(), pictureOpened.logo.get_height(), 0.55)
    button_a = ClassMenuButton((WIDTH/2 - 310), 300, pictureOpened.bt_a, pictureOpened.bt_a.get_width(), pictureOpened.bt_a.get_height(), 0.65)
    button_d = ClassMenuButton((WIDTH/2 + 130), 300, pictureOpened.bt_d, pictureOpened.bt_d.get_width(), pictureOpened.bt_d.get_height(), 0.65)
    button_start = ClassMenuButton((WIDTH/2 - 250), 600, pictureOpened.bt_start, pictureOpened.bt_start.get_width(), pictureOpened.bt_start.get_height(), 0.75)
    button_exit = ClassMenuButton((WIDTH/2 + 30), 600, pictureOpened.bt_exit, pictureOpened.bt_exit.get_width(), pictureOpened.bt_exit.get_height(), 0.75)
    buttonsMenuGroup.draw(screen)  # draw group buttons

def main_menu():
    global nextQuestion, nowHt,checkCharacter, character
    running = True
    init_values()
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
                    main_Character()
                    main_animation() # animetion
                elif(button_exit.checkClick()):
                    print("Exit")
                    pygame.quit()
                    sys.exit()
            if (event.type == pygame.KEYDOWN):
                screen.blit(pictureOpened.instead_menu,(WIDTH/3 + 59, HEIGHT/2 - 145))
                if (event.key == pygame.K_LEFT or event.key == ord("a")):
                    #change color
                    print("color changing")
                    checkCharacter -= 1
                    if (character == 0):
                        character = 1
                    elif (character == 1):
                        character = 0
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    #change color
                    print("color changing")
                    checkCharacter += 1
                    if (character == 0):
                        character = 1
                    elif (character == 1):
                        character = 0
            changeCharacter()
        pygame.display.update()

def checkChoice():
    global nextQuestion, nowHt, score, getdamage, goToShowKey
    print(choiceButList)
    print(checkChoiceButList)
    if (choiceButList[0].checkClickgm()):
        if (checkChoiceButList[0] == "True"):
            print("clicked TRUE")
            goToShowKey = 0
            showKey()
            
        else:
            print("clicked FALSE")
            goToShowKey = 1
            showKey()
            
    elif (choiceButList[1].checkClickgm()):
        if (checkChoiceButList[1] == "True"):
            print("clicked TRUE")
            goToShowKey = 0
            showKey()
            
        else:
            print("clicked FALSE")
            goToShowKey = 1
            showKey()
    elif (choiceButList[2].checkClickgm()):
        if (checkChoiceButList[2] == "True"):
            print("clicked TRUE")
            goToShowKey = 0
            showKey()
        else:
            print("clicked FALSE")
            goToShowKey = 1
            showKey()
    elif (choiceButList[3].checkClickgm()):
        if (checkChoiceButList[3] == "True"):
            print("clicked TRUE")
            goToShowKey = 0
            showKey()
        else:
            print("clicked FALSE")
            goToShowKey = 1
            showKey()
   
    for i in range(0,len(choiceButList)):
        choiceButList[i].updateGameBt()
    choiceButList.clear()
    checkChoiceButList.clear()
    print(checkChoiceButList)
    main_animation()

# ================================= QUIZ =======================================
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
            else:
                continue
        pygame.display.update()

# ========== RUN ==========
main_menu()
# getWebLink()