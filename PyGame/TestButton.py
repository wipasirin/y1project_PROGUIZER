import pygame
import sys

WIDTH = 750
HEIGHT = 500
clock = pygame.time.Clock()
# ===== background =======
# -- menu
bg_img1 = pygame.image.load("pictures\menu.png")
bg1 = pygame.transform.scale(bg_img1,(WIDTH,HEIGHT)) # set a size of bg
# -- gameplay1
bg_img2 = pygame.image.load("pictures\map.png")
bg2 = pygame.transform.scale(bg_img2,(WIDTH,HEIGHT)) # set a size of bg
# -- gameplay2
bg_img3 = pygame.image.load("pictures\Bg2.png")
bg3 = pygame.transform.scale(bg_img3,(WIDTH,HEIGHT)) # set a size of bg
# -- gameplay3
bg_img4 = pygame.image.load("pictures\Bg1.png")
bg4 = pygame.transform.scale(bg_img4,(WIDTH,HEIGHT)) # set a size of bg

# ====== button ===========
# -- start/exit
bt_start = pygame.image.load("pictures\start.png")
bt_exit = pygame.image.load("pictures\exit.png")
# -- true/false
bt_true = pygame.image.load("pictures\True.png")
bt_false = pygame.image.load("pictures\False.png")


pygame.init # initialize pygame
pygame.display.set_caption("PROGUIZER") # set head

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # set a size of display
buttons = pygame.sprite.Group()

class Button(pygame.sprite.Sprite): # create class button 
    #pos = pygame.mouse.get_pos() # position of the mouse cursor
    def __init__(self, x, y, image, scale): # constructor
        #super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (int(scale*WIDTH), int(scale*HEIGHT))) # rescale of button
        self.rect = self.image.get_rect() # surface that suitable of object
        self.rect.topleft = (x, y)
        self.clicked = False
        buttons.add(self)
    

    def draw(self):
        screen.blit(self.image, [self.rect.x, self.rect.y])
        #self.checkClick()

    def checkClick(self):
        #self.clicked = False
        pos = pygame.mouse.get_pos()
        if(self.rect.collidepoint(pos)): # test if a point is inside a rectangle(button)
            print("in rect", self)
            if (pygame.mouse.get_pressed()[0] and (self.clicked == False)): #clicked left mouse key (left[0], middle[1], right[2])
                self.clicked = True
                #return True
            elif(self.clicked == True): 
                self.clicked = False
        
        #else: self.clicked = False
        #else:
            #print(self.clicked,62) 
            #if(self.clicked == True): 
                #self.clicked = False
            #    if (pygame.mouse.get_pressed()[0] and (self.clicked == False) and self.rect.collidepoint(pos)): #clicked left mouse key (left[0], middle[1], right[2])
                    #self.clicked = True
                
        print(self.clicked,70)
        return self.clicked



def menu_button():
    global button_start, button_exit
    screen.blit(bg1, (0,0)) # used bg
    for sprites in buttons:
        sprites.kill()
    button_start = Button(300, 80, bt_start, 0.155) # create an object 'start button'
    button_exit = Button(550, 340, bt_exit, 0.275) # create an object 'exit button'
    button_start.draw() # called obj method
    button_exit.draw()

def checkquiz2():
    #if (event.type == pygame.MOUSEBUTTONDOWN):
        #print(button_true.checkClick())
        #button_true.checkClick()
        if(button_true.checkClick()):
            print(button_true.checkClick())
            print("true")
            #screen.blit(bg4, (0,0))
            #quiz2()
        elif(button_false.checkClick()):
            print("false")
            menu_button()
        

def quiz2():
    global button_true, button_false 
    screen.blit(bg3, (0,0))
    for sprites in buttons:
        sprites.kill()
    button_true = Button(150, 350, bt_true, 0.155)
    button_false = Button(475, 350, bt_false, 0.155)
    button_true.draw()
    button_false.draw()
    checkquiz2()    

def checkquiz1():
    #if (event.type == pygame.MOUSEBUTTONDOWN):
        #print(button_true.checkClick())
        #button_true.checkClick()
        if(button_true.checkClick()):
            print(button_true.checkClick())
            print("true")
            #screen.blit(bg4, (0,0))
            quiz2()
        elif(button_false.checkClick()):
            print("false")
            menu_button()
        

def quiz1():
    global button_true, button_false 
    screen.blit(bg2, (0,0))
    for sprites in buttons:
        sprites.kill()
    button_true = Button(150, 350, bt_true, 0.155)
    button_false = Button(475, 350, bt_false, 0.155)
    button_true.draw()
    button_false.draw()
    checkquiz1()


def main_menu():
    running = True
    pygame.display.set_caption("Menu")
    # ========== game loop ========== 
    while running:
        for event in pygame.event.get(): # check circumstance in the game
            if (event.type == pygame.QUIT) : # when press botton an exit
                running = False
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if(button_start.checkClick()):
                    print(buttons,"menu")
                    print("Start")
                    quiz1()
                elif(button_exit.checkClick()):
                    print("Exit")
                    running = False

        pygame.display.update() # same pygame.display.flip() : to updating display
    pygame.quit()




# ========== RUN ==========
menu_button()
main_menu()
