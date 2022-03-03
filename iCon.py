import pygame
pygame.init()

screen = pygame.display.set_mode([600, 400])
  
# Take image as input
img = pygame.image.load('pictures\ProgressPictures\heart.png')
  
# Set image as icon
pygame.display.set_icon(img)
  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Set the background color
    screen.fill((255, 255, 0))
    pygame.display.update()
  
pygame.quit()