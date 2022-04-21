import pygame
import json
from moviepy.editor import *

WIDTH = 1250
HEIGHT = 750

class fileForPGZ:
    file = open("component\objects\question\questionTxt.json")
    data = json.load(file)
    cutscene1 = VideoFileClip("component\objects/video\cutscenes1.mp4")
    cutscene2 = VideoFileClip("component\objects/video\cutscenes2.mp4")
    
class pictureForPGZ:
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

    # =================================  MENU  =======================================
    # start/exit
    menu = pygame.image.load("component/background/bgMenu.png")
    scoreBg = pygame.image.load("component/background\score.png")
    bg_menu = pygame.transform.scale(menu, (WIDTH, HEIGHT))  # set a size of bg

    bt_start = pygame.image.load("component/buttons\start.png")
    bt_exit = pygame.image.load("component/buttons\exit.png")
    bt_next = pygame.image.load("component/buttons/next.png")
    bt_home = pygame.image.load("component\objects\objs\home.png")

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
    heart = pygame.image.load("component\objects\objs\heart.png")

    font_choice = pygame.font.Font('component/objects/font\Pixellari.ttf', 30)
    font_quiz = pygame.font.Font('component/objects/font\Pixellari.ttf', 30)
    font_score = pygame.font.Font('component/objects/font\Pixellari.ttf', 120)
    font_answer = pygame.font.Font('component/objects/font\Pixellari.ttf', 50)
    color_fQuiz = (240, 245, 245)
    color_fChoice = (100, 100, 200)

