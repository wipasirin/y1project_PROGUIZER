
import pygame
global checkColor, characterNow
pygame.init
checkColor = 0
characterNow = 1

screen = pygame.display.set_mode([600, 400])
timmy1 = pygame.image.load("projects\projects\PyGame\pictures\ch1.png")  
ani_timmy1= pygame.transform.scale(timmy1, (int(timmy1.get_width() * 1.25), int(timmy1.get_height() * 1.25)))
timmy2 = pygame.image.load("projects\projects\PyGame\pictures\ch2.png")
ani_timmy2= pygame.transform.scale(timmy2, (int(timmy2.get_width() * 1.25), int(timmy2.get_height() * 1.25)))

def change_color_timmy():
    if checkColor % 2 == 0:
        characterNow = 1
        screen.blit(ani_timmy1, (0, 0))
    elif checkColor % 2 == 1:
        characterNow = 2
        screen.blit(ani_timmy2, (0, 0))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(ani_timmy1, (0,0))
    change_color_timmy()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                #change color
                print("color changing")
                checkColor -= 1

            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                #change color
                print("color changing")
                checkColor += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                print("color changed")
                #change color
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                print("color changed")
                #change color


    # Set the background color
    pygame.display.update()
  
pygame.quit()