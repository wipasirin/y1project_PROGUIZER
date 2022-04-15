import webbrowser
import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg_img1 = pygame.image.load("projects\projects\PyGame\pictures/background/bg1_pixel.png")
bg1 = pygame.transform.scale(bg_img1,(WIDTH,HEIGHT))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clicked = False
#draw button
start = pygame.Rect(50, 50, 350, 40)
startColor = WHITE
menuColor = BLACK
smallfont = pygame.font.SysFont('Arial', 35)

class text:
    green = (0, 255, 0)
def text(font, text, color):
    return font.render(text, 1, color)
# #font
hello = text(smallfont, "Hello", BLACK)
webLink = text(smallfont, "Click for key web", BLACK)
# #game loop
running = True
while running:
    screen.fill(menuColor)
    screen.blit(bg1, (0, 0)) #background
    pygame.draw.rect(screen, startColor, start)
    mx, my = pygame.mouse.get_pos()
    screen.blit(webLink, (60, 50))
    if clicked:
        if start.collidepoint((mx, my)):
            webbrowser.open("https://stackoverflow.com/questions/68592269/how-can-i-make-a-button-that-goes-to-website-in-pygame")
    clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if event.button == 1:
                clicked = True   

    pygame.display.update() #update
