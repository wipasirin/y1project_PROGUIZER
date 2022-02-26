#from turtle import update
import pygame
import sys

WIDTH = 750
HEIGHT = 500
clock = pygame.time.Clock()
# ===== background =======
# -- menu
bg_img1 = pygame.image.load("projects\PyGame\pictures\menu.png")
bg1 = pygame.transform.scale(bg_img1,(WIDTH,HEIGHT)) # set a size of bg
# -- gameplay1
bg_img2 = pygame.image.load("projects\PyGame\pictures\BGpx2.png")
bg2 = pygame.transform.scale(bg_img2,(WIDTH,HEIGHT)) # set a size of bg
# -- gameplay2
bg_img3 = pygame.image.load("projects\PyGame\pictures\Bg2.png")
bg3 = pygame.transform.scale(bg_img3,(WIDTH,HEIGHT)) # set a size of bg
# -- gameplay3
bg_img4 = pygame.image.load("projects\PyGame\pictures\Bg1.png")
bg4 = pygame.transform.scale(bg_img4,(WIDTH,HEIGHT)) # set a size of bg

# ====== button ===========
# -- start/exit
bt_start = pygame.image.load("projects\PyGame\pictures\start.png")
bt_exit = pygame.image.load("projects\PyGame\pictures\exit.png")
# -- true/false
bt_true = pygame.image.load("projects\PyGame\pictures\True.png")
bt_false = pygame.image.load("projects\PyGame\pictures\False.png")


pygame.init # initialize pygame
pygame.display.set_caption("PROGUIZER") # set head

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # set a size of display
buttons_menu = pygame.sprite.Group()
buttons_game = pygame.sprite.Group()

class Button_menu(pygame.sprite.Sprite): # create class button 
    #pos = pygame.mouse.get_pos() # position of the mouse cursor
    def __init__(self, x, y, image, scale): # constructor
        #super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (int(scale*WIDTH), int(scale*HEIGHT))) # rescale of button
        self.rect = self.image.get_rect() # surface that suitable of object
        self.rect.topleft = (x, y)
        self.clicked = False
        buttons_menu.add(self)
 
    def update(self):
        del self#.image
        # del self.rect
        # del self.clicked


    def draw(self):
        screen.blit(self.image, [self.rect.x, self.rect.y])

    def checkClick(self):
        print("I'm checking")
        pos = pygame.mouse.get_pos()
        if(hasattr(self, 'rect')):
            if(self.rect.collidepoint(pos)): # test if a point is inside a rectangle(button)
                print("in rect", self)
                if (pygame.mouse.get_pressed()[0] and (self.clicked == False)): #clicked left mouse key (left[0], middle[1], right[2])
                    self.clicked = True
                elif(self.clicked == True and pygame.mouse.get_pressed()[0]): 
                    self.clicked = False
        else:
            self.clicked = False
            
        return self.clicked

class Button_game(pygame.sprite.Sprite): # create class button 
    #pos = pygame.mouse.get_pos() # position of the mouse cursor
    def __init__(self, x, y, image, scale): # constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (int(scale*WIDTH), int(scale*HEIGHT))) # rescale of button
        self.rect = self.image.get_rect() # surface that suitable of object
        self.rect.topleft = (x, y)
        self.clicked = False
        buttons_game.add(self)
 
    def drawgm(self):
        screen.blit(self.image, [self.rect.x, self.rect.y])

    def updategm(self):
        del self#.image
        # del self.rect
        # del self.clicked

    def checkClickgm(self):
        print("I'm checking")
        pos = pygame.mouse.get_pos()
        if(hasattr(self, 'rect')):
            if(self.rect.collidepoint(pos)): # test if a point is inside a rectangle(button)
                print("in rect", self)
                if (pygame.mouse.get_pressed()[0] and (self.clicked == False)): #clicked left mouse key (left[0], middle[1], right[2])
                    self.clicked = True
                elif(self.clicked == True and pygame.mouse.get_pressed()[0]): 
                    self.clicked = False
        else:
            self.clicked = False
        #elif(self.clicked == True):
            #print(self.clicked,62) 
            #if(self.clicked == True): 
            #self.clicked = False
            #if(pygame.mouse.get_pressed()[0] and (self.clicked == False) and self.rect.collidepoint(pos)): #clicked left mouse key (left[0], middle[1], right[2])
                    #self.clicked = True
                
        #print(self.clicked,70)
        return self.clicked

def menu_button():
    global button_start, button_exit
    screen.blit(bg1, (0,0)) # used bg
    # for sprites in buttons_menu:
    #     sprites.kill()
    button_start = Button_menu(300, 80, bt_start, 0.155) # create an object 'start button'
    button_exit = Button_menu(550, 340, bt_exit, 0.275) # create an object 'exit button'
    buttons_menu.draw(screen) # called obj method
    #button_exit.draw()

# def checkquiz2():
#     #if (event.type == pygame.MOUSEBUTTONDOWN):
#         #print(button_true.checkClick())
#         #button_true.checkClick()
#         if(button_true.checkClick()):
#             print(button_true.checkClick())
#             print("true")
#             #screen.blit(bg4, (0,0))
#             #quiz2()
#         elif(button_false.checkClick()):
#             print("false")
#             menu_button()
        
def quiz1():
    global button_true, button_false 
    screen.blit(bg2, (0,0))
    # for sprites in buttons_menu:
    #     sprites.kill()
    button_true = Button_game(150, 350, bt_true, 0.155)
    button_false = Button_game(475, 350, bt_false, 0.155)
    buttons_game.draw(screen)

def quiz2():
    global button_true, button_false 
    screen.blit(bg3, (0,0))
    # for sprites in buttons:
    #     sprites.kill()
    button_true = Button_game(475, 350, bt_true, 0.155)
    button_false = Button_game(150, 350, bt_false, 0.155)
    buttons_game.draw(screen)

# def checkquiz1():
#     #if (event.type == pygame.MOUSEBUTTONDOWN):
#         #print(button_true.checkClick())
#         #button_true.checkClick()
#         if(button_true.checkClickgm()):
#             # print(button_true.checkClick())
#             print("true")
#             #screen.blit(bg4, (0,0))
#             #quiz2()
#         elif(button_false.checkClickgm()):
#             print("false")
#             menu_button()
#         else:
#             print("What?")    
        
def main_menu():
    
    menu_button()
    running = True
    
    # ========== game loop ========== 
    while running:
        for event in pygame.event.get(): # check circumstance in the game
            if (event.type == pygame.QUIT) : # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(button_start.checkClick()):
                    button_start.update()
                    button_exit.update()
                    print("Start")
                    main_quiz1()
                    print("I'm just going a main_quiz1")
                elif(button_exit.checkClick()):
                    print("Exit")
                    running = False

        pygame.display.update() # same pygame.display.flip() : to updating display
    # pygame.quit()

def main_quiz1():
    quiz1()
    running = True
    
    # ========== game loop ========== 
    while running:
        for event in pygame.event.get(): # check circumstance in the game
            if (event.type == pygame.QUIT) : # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(button_true.checkClickgm()):
                    button_true.updategm()
                    button_false.updategm()
                    print("true")
                    main_quiz2()
                    print("I'm just going a main_quiz")
                elif(button_false.checkClickgm()):
                    print("false")
                    main_menu()

        pygame.display.update() # same pygame.display.flip() : to updating display
    
    # pygame.quit()

def main_quiz2():
    quiz2()
    running = True
    
    # ========== game loop ========== 
    while running:
        for event in pygame.event.get(): # check circumstance in the game
            if (event.type == pygame.QUIT) : # when press botton an exit
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(button_true.checkClickgm()):
                    button_true.updategm()
                    button_false.updategm()
                    print("true")
                    screen.blit(bg4, (0,0))
                elif(button_false.checkClickgm()):
                    print("false")
                    main_menu()
                    # running = False

        pygame.display.update()
    # pygame.quit()


# ========== RUN ==========
main_menu()
