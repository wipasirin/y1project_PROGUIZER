#from turtle import update
from operator import and_
from tkinter.font import BOLD
from turtle import width
import pygame
import sys
# import pandas
import json
pygame.init()  
pygame.font.init()

WIDTH = 1250
HEIGHT = 750
# Opening JSON file
def init_values():
    global animation_cha, animation_chafight, animation_chahurt, nowHt
    global nextQuestion, a_data, choiceButList, checkChoiceButList, score, getdamage
    global character, checkCharacter, characterNow
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

# initialize pygame
file = open("component\objects\question\questionTxt.json")
data = json.load(file)
# pygame.mixer.music.load('projects\PyGame\pictures\objects\music4.mp3')
# pygame.mixer.music.play()

# ===============================  CHARACTER  ====================================
# timmy
timmy = pygame.image.load("component\characters\character/timmy.png")
timmycom = pygame.image.load("component\characters\character/timmy_fight.png")
timmyhurt = pygame.image.load("component\characters\character/timmy_hurt.png")
ani_timmy= pygame.transform.scale(timmy, (int(timmy.get_width() * 0.25), int(timmy.get_height() * 0.25)))
ani_timmyfight = pygame.transform.scale(timmycom, (int(timmycom.get_width() * 0.25), int(timmycom.get_height() * 0.25)))
ani_timmyhurt = pygame.transform.scale(timmyhurt, (int(timmyhurt.get_width() * 0.25), int(timmyhurt.get_height() * 0.25)))
# ohmmy
ohmmy = pygame.image.load("component\characters\character\ohmmy.png")
ohmmycom = pygame.image.load("component\characters\character/ohmmy_fight.png")
ohmmyhurt = pygame.image.load("component\characters\character/ohmmy_hurt.png")
ani_ohmmy= pygame.transform.scale(ohmmy, (int(ohmmy.get_width() * 0.25), int(ohmmy.get_height() * 0.25)))
ani_ohmmyfight = pygame.transform.scale(ohmmycom, (int(ohmmycom.get_width() * 0.25), int(ohmmycom.get_height() * 0.25)))
ani_ohmmyhurt = pygame.transform.scale(ohmmyhurt, (int(ohmmyhurt.get_width() * 0.25), int(ohmmyhurt.get_height() * 0.25)))

# ================================  MONSTER  =====================================
q1_monster = pygame.image.load("component\characters\monster\monster1.png")
q2_monster = pygame.image.load("component\characters\monster\monster2.png")
q3_monster = pygame.image.load("component\characters\monster\monster3.png")
q4_monster = pygame.image.load("component\characters\monster\P2_monster4.png")
q5_monster = pygame.image.load("component\characters\monster\P5_monster5.png")
q6_monster = pygame.image.load("component\characters\monster\P7_monster6.png")
q7_monster = pygame.image.load("component\characters\monster\monster7and8.png")
q8_monster = pygame.image.load("component\characters\monster\monster7and8.png")
q9_monster = pygame.image.load("component\characters\monster\monster9.png")
q10_monster = pygame.image.load("component\characters\monster\monster10and11.png")
q11_monster = pygame.image.load("component\characters\monster\monster10and11.png")
q12_monster = pygame.image.load("component\characters\monster\monster12.png")
q13_monster = pygame.image.load("component\characters\monster\monster13.png")
q14_monster = pygame.image.load("component\characters\monster\monster14.png")
q15_monster = pygame.image.load("component\characters\monster\monster15.png")
q16_monster = pygame.image.load("component\characters\monster\monster16.png")
q17_monster = pygame.image.load("component\characters\monster\monster17.png")
q18_monster = pygame.image.load("component\characters\monster\monster18.png")
q19_monster = pygame.image.load("component\characters\monster\monster19.png")
q20_1_monster = pygame.image.load("component\characters\monster\monster20_1.png")
q20_2_monster = pygame.image.load("component\characters\monster\monster20_2.png")

# ===== animation ====== 
# q1
q1_1 = pygame.image.load("component\characters\monster\monster1.png")
q1_2 = pygame.image.load("component\characters\monster\monster1_1.png")
# q3
q3_1 = pygame.image.load("component\characters\monster\monster2.png")
q3_2 = pygame.image.load("component\characters\monster\monster3.png")
q3_3 = pygame.image.load("component\characters\monster\monster3_1.png")
q3_4 = pygame.image.load("component\characters\monster\monster3_2.png")
# q6
q6_1 = pygame.image.load("component\characters\monster\P1.png")
q6_2 = pygame.image.load("component\characters\monster\P2_monster4.png")
q6_3 = pygame.image.load("component\characters\monster\P1.png")
q6_4 = pygame.image.load("component\characters\monster\P2_monster4.png")
q6_5 = pygame.image.load("component\characters\monster\P3.png")
q6_6 = pygame.image.load("component\characters\monster\P4.png")
q6_7 = pygame.image.load("component\characters\monster\P5_monster5.png")
q6_8 = pygame.image.load("component\characters\monster\P4.png")
q6_9 = pygame.image.load("component\characters\monster\P5_monster5.png")
q6_10 = pygame.image.load("component\characters\monster\P4.png")
q6_11 = pygame.image.load("component\characters\monster\P5_monster5.png")
q6_12 = pygame.image.load("component\characters\monster\P6.png")
q6_13 = pygame.image.load("component\characters\monster\P7_monster6.png")
q6_14 = pygame.image.load("component\characters\monster\P6.png")
q6_15 = pygame.image.load("component\characters\monster\P7_monster6.png")
q6_16 = pygame.image.load("component\characters\monster\P8.png")
# q8
q8_1 = pygame.image.load("component\characters\monster\monster7and8.png")
q8_2 = pygame.image.load("component\characters\monster\monster7and8_1.png")
# q11
q11_1 = pygame.image.load("component\characters\monster\monster9.png")
q11_2 = pygame.image.load("component\characters\monster\monster10and11.png")
q11_3 = pygame.image.load("component\characters\monster\monster10and11_1.png")
q11_4 = pygame.image.load("component\characters\monster\monster10and11_2.png")
q11_5 = pygame.image.load("component\characters\monster\monster10and11_3.png")
q11_6 = pygame.image.load("component\characters\monster\monster10and11_4.png")
q11_7 = pygame.image.load("component\characters\monster\monster10and11_5.png")
# q14
q14_1 = pygame.image.load("component\characters\monster\monster12.png")
q14_2 = pygame.image.load("component\characters\monster\monster13.png")
q14_3 = pygame.image.load("component\characters\monster\monster14_1.png")
q14_4 = pygame.image.load("component\characters\monster\monster14_2.png")
q14_5 = pygame.image.load("component\characters\monster\monster14_3.png")
q14_6 = pygame.image.load("component\characters\monster\monster14_4.png")
q14_7 = pygame.image.load("component\characters\monster\monster14_5.png")
# q19
q19_1 = pygame.image.load("component\characters\monster\monster15.png")
q19_2 = pygame.image.load("component\characters\monster\monster16.png")
q19_3 = pygame.image.load("component\characters\monster\monster17.png")
q19_4 = pygame.image.load("component\characters\monster\monster18.png")
q19_5 = pygame.image.load("component\characters\monster\monster19.png")
q19_6 = pygame.image.load("component\characters\monster\monster19_1.png")
q19_7 = pygame.image.load("component\characters\monster\monster19_2.png")
q19_8 = pygame.image.load("component\characters\monster\monster19_3.png")
# q20
# q20_1 = pygame.image.load("component\characters\monster\monster1.png")
# =================================  MENU  =======================================
# start/exit
menu = pygame.image.load("component/background/bgMenu.png")
bg_menu = pygame.transform.scale(menu, (WIDTH, HEIGHT))  # set a size of bg

bt_start = pygame.image.load("component/buttons\start.png")
bt_exit = pygame.image.load("component/buttons\exit.png")

ghost = pygame.image.load("component/background\special.png")
bg_ghost = pygame.transform.scale(ghost, (WIDTH, HEIGHT))

logo = pygame.image.load("component/objects\objs\logo.png")

instead = pygame.image.load("component/background\Capture.PNG")
instead_menu = pygame.transform.scale(instead, (int(instead.get_width() * 0.80), int(instead.get_height() * 0.80)))

bt_a = pygame.image.load("component/objects\objs\A.png")
bt_d = pygame.image.load("component/objects\objs\D.png")
name_timmy = pygame.image.load("component/objects\objs/timmy.png")
name_ohmmy = pygame.image.load("component/objects\objs\Ohmmy.png")
# ================================== QUIZ ========================================
bgQuizLv1 = pygame.image.load("component/background/bgLevel1.png")
bg_quizLv1 = pygame.transform.scale(bgQuizLv1, (WIDTH, HEIGHT))

bgQuizLv2 = pygame.image.load("component/background/bgLevel2.png")
bg_quizLv2 = pygame.transform.scale(bgQuizLv2, (WIDTH, HEIGHT))

bgQuizLv3 = pygame.image.load("component/background/bgLevel3.png")
bg_quizLv3 = pygame.transform.scale(bgQuizLv3, (WIDTH, HEIGHT))

bg_choice = pygame.image.load("component/buttons\choice.png")

font_choice = pygame.font.Font('component/objects/font\Pixellari.ttf', 30)
font_quiz = pygame.font.Font('component/objects/font\Pixellari.ttf', 30)
color_fQuiz = (200, 200, 200)
color_fChoice = (100, 100, 200)

# ================================ [ START ] =====================================
pygame.display.set_caption("PROGUIZER")  # set head
pygame.display.set_icon(pygame.image.load("component/objects\objs\icon.png"))

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
        self.image = pygame.transform.scale(bg_choice, (int(width * scale), int(hight * scale)))  # rescale of button      
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y)
        self.clicked = False
        buttonsGameGroup.add(self)

    def drawGameBt(self, txt_choice, txt_quiz, pt_x, pt_y):
        screen.blit(self.image, [pt_x, pt_y])
        # ิblit txt
        blit_text(screen, txt_quiz, (WIDTH/2 - 250, 50), font_quiz, color_fQuiz)
        blit_text(screen, txt_choice, (pt_x + 50, pt_y + 25), font_choice, color_fChoice)

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
            self.imgMon.append(q1_1)
            self.imgMon.append(q1_2)
        elif (nextQuestion == 4):
            self.imgMon.append(q3_1)
            self.imgMon.append(q3_2)
            self.imgMon.append(q3_3)
            self.imgMon.append(q3_4)
        elif (nextQuestion == 7):
            self.imgMon.append(q6_1)
            self.imgMon.append(q6_2)
            self.imgMon.append(q6_3)
            self.imgMon.append(q6_4)
            self.imgMon.append(q6_5)
            self.imgMon.append(q6_6)
            self.imgMon.append(q6_7)
            self.imgMon.append(q6_8)
            self.imgMon.append(q6_9)
            self.imgMon.append(q6_10)
            self.imgMon.append(q6_11)
            self.imgMon.append(q6_12)
            self.imgMon.append(q6_13)
            self.imgMon.append(q6_14)
            self.imgMon.append(q6_15)
            self.imgMon.append(q6_16)
        elif (nextQuestion == 9):
            self.imgMon.append(q8_1)
            self.imgMon.append(q8_2)
        elif (nextQuestion == 12):
            self.imgMon.append(q11_1)
            self.imgMon.append(q11_2)
            self.imgMon.append(q11_3)
            self.imgMon.append(q11_4)
            self.imgMon.append(q11_5)
            self.imgMon.append(q11_6)
            self.imgMon.append(q11_7)
        elif (nextQuestion == 15):
            self.imgMon.append(q14_1)
            self.imgMon.append(q14_2)
            self.imgMon.append(q14_3)
            self.imgMon.append(q14_4)
            self.imgMon.append(q14_5)
            self.imgMon.append(q14_6)
            self.imgMon.append(q14_7)
        elif (nextQuestion == 20):
            self.imgMon.append(q19_1)
            self.imgMon.append(q19_2)
            self.imgMon.append(q19_3)
            self.imgMon.append(q19_4)
            self.imgMon.append(q19_5)
            self.imgMon.append(q19_6)
            self.imgMon.append(q19_7)
            self.imgMon.append(q19_8)
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
        image_mon = q1_monster
        x, y, scale = 750, 280, 0.70
    elif(nextQuestion <= 3):
        if(nextQuestion == 2):
            image_mon = q2_monster
        else:
            image_mon = q3_monster
        x, y, scale = 750, 280, 0.90
    elif(nextQuestion <= 6):
        if(nextQuestion == 4):
            image_mon = q4_monster
        elif(nextQuestion == 5):
            image_mon = q5_monster
        else:
            image_mon = q6_monster
        x, y, scale = 750, 290, 0.70
    elif(nextQuestion <= 8):
        image_mon = q7_monster
        x, y, scale = 750, 290, 0.75
    elif(nextQuestion <= 11):
        if(nextQuestion == 9):
            image_mon = q9_monster
        else:
            image_mon = q10_monster
        x, y, scale = 750, 275, 0.35
    elif(nextQuestion <= 14):
        if(nextQuestion == 14):
            image_mon = q14_monster
        else:
            image_mon = q12_monster
        x, y, scale = 690, 62, 0.65
    elif(nextQuestion <= 19):
        if(nextQuestion == 15):
            image_mon = q15_monster
        elif(nextQuestion == 16):
            image_mon = q16_monster
        elif(nextQuestion == 17):
            image_mon = q17_monster
        elif(nextQuestion == 18):
            image_mon = q18_monster
        else:
            image_mon = q19_monster
        x, y, scale = 690, 223, 0.55
    elif(nextQuestion <= 20):
        x, y, scale = 800, 270, 0.25
        if(character == 0):
            image_mon = q20_1_monster
        elif(character == 1):
            image_mon = q20_2_monster
    if (nextQuestion < (len(data['allThing'])+1)):
        init_monster(image_mon, x, y, scale)

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
        self.heart = pygame.image.load('component\objects\objs\heart.png')
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
        screen.blit(bg_ghost, (0, 0))  

def quiz():
    pt_x = 20
    pt_y = 583
    countToChange_pt_y = 0
    checkNextQuestion = 1
    for i in data['allThing']:
        if (nextQuestion == checkNextQuestion) : 
            for y in data['allThing'][i]['allChoice'] :
                choiceButton = Text(pt_x, pt_y, bg_choice, bg_choice.get_width(), bg_choice.get_height(), 1)
                # read line
                txt_quiz = data['allThing'][i].get('question')
                txt_choice = data['allThing'][i]['allChoice'][y].get('choice')
                txt_check = data['allThing'][i]['allChoice'][y].get('check')
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
    file.close()

def checkBgQuiz():
    if(nextQuestion <= 7):
        bg_quiz = bg_quizLv1
    elif(nextQuestion <= 14):
        bg_quiz = bg_quizLv2
    else:
        bg_quiz = bg_quizLv3
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
            if (nextQuestion == (len(data['allThing'])+1)):
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
        screen.blit(ani_timmy, ((WIDTH/2 - 40), 250))
        screen.blit(name_timmy, ((WIDTH/4 + 183), 400))
    elif checkCharacter % 2 == 1:
        characterNow = 2
        screen.blit(ani_ohmmy, ((WIDTH/2 - 40), 250))
        screen.blit(name_ohmmy, ((WIDTH/4 + 183), 400))

def main_Character():
    global animation_cha, animation_chafight, animation_chahurt
    if(character == 0):
        animation_cha = ani_timmy
        animation_chafight = ani_timmyfight
        animation_chahurt = ani_timmyhurt
    elif(character == 1):
        animation_cha = ani_ohmmy
        animation_chafight = ani_ohmmyfight
        animation_chahurt = ani_ohmmyhurt

# =================================  MENU  =======================================
def func_menu():
    global button_start, button_exit
    screen.blit(bg_menu, (0, 0))  # used bg
    # screen.blit(logo, ((WIDTH/2 - 500), 10))
    button_logo = ClassMenuButton((WIDTH/2 - 195), 5, logo, logo.get_width(), logo.get_height(), 0.55)
    button_a = ClassMenuButton((WIDTH/2 - 310), 300, bt_a, bt_a.get_width(), bt_a.get_height(), 0.65)
    button_d = ClassMenuButton((WIDTH/2 + 130), 300, bt_d, bt_d.get_width(), bt_d.get_height(), 0.65)
    button_start = ClassMenuButton((WIDTH/2 - 250), 600, bt_start, bt_start.get_width(), bt_start.get_height(), 0.75)
    button_exit = ClassMenuButton((WIDTH/2 + 30), 600, bt_exit, bt_exit.get_width(), bt_exit.get_height(), 0.75)
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
                screen.blit(instead_menu,(WIDTH/3 + 59, HEIGHT/2 - 145))
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
    global nextQuestion, nowHt, score, getdamage
    print(choiceButList)
    print(checkChoiceButList)
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