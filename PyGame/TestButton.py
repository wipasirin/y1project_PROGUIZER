import pygame

WIDTH = 750
HEIGHT = 500

# bg -- menu
bg_img1 = pygame.image.load("pictures\menu.png")
bg1 = pygame.transform.scale(bg_img1,(WIDTH,HEIGHT)) # set a size of bg

# bg -- game
bg_img2 = pygame.image.load("pictures\map.png")
bg2 = pygame.transform.scale(bg_img2,(WIDTH,HEIGHT)) # set a size of bg

#cursor_img = pygame.image.load("pictures\mary2.png")

# bt -- start
bt_start = pygame.image.load("pictures\start.png")
bt_exit = pygame.image.load("pictures\exit.png")

pygame.init # initialize pygame
pygame.display.set_caption("PROGUIZER") # set head

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # set a size of display

class Button: # create class button
    def __init__(self, x, y, image, scale): # constructor
        self.image = pygame.transform.scale(image, (int(scale*WIDTH), int(scale*HEIGHT))) # rescale of button
        self.rect = self.image.get_rect() # surface that suitable of object
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        pos = pygame.mouse.get_pos() # position of the mouse cursor
        screen.blit(self.image, [self.rect.x, self.rect.y])

        if(self.rect.collidepoint(pos)): # test if a point is inside a rectangle(button)
            mouse_presses = pygame.mouse.get_pressed()
            if ((mouse_presses[0] == 1) and (self.clicked == False)): #clicked left mouse key (left[0], middle[1], right[2])
                self.clicked = True

            if (mouse_presses[0] == 0): # don't clicked
                self.clicked = False

        return self.clicked

button_start = Button(300, 80, bt_start, 0.155) # create an object 'start button'
button_exit = Button(550, 340, bt_exit, 0.275) # create an object 'exit button'


screen.blit(bg1, (0,0)) # used bg
button_start.draw() # called obj method
button_exit.draw()
running = True
# ========== game loop ==========
while running:
    
     
    for event in pygame.event.get(): # check circumstance in the game
        if (event.type == pygame.QUIT) : # when press botton an exit
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if(button_start.draw()):
                print("Start")
                screen.blit(bg2, (0,0))
            if(button_exit.draw()):
                print("Exit")
                running = False

    pygame.display.update() # same pygame.display.flip() : to updating display
    
pygame.quit()