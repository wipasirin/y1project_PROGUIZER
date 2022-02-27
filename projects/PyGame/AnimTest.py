import pygame

WIDTH = 750
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg_img1 = pygame.image.load("projects\projects\PyGame\pictures\Bg1.png")
bg1 = pygame.transform.scale(bg_img1,(WIDTH,HEIGHT))

class animate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.char = [pygame.image.load('projects/projects/PyGame/pictures/ch1.png'), pygame.image.load('projects/projects/PyGame/pictures/ch2.png')]
        # self.char0_1 = pygame.transform.scale((int(self.char[0].get_width() * scale)), (int(self.char[0].get_height() * scale)))
        # self.char1 = pygame.image.load('projects/PyGame/pictures/ch2.png')
        self.rect = [self.char[0].get_rect(), self.char[1].get_rect()]
        # self.rect1 = self.char1.get_rect()
        self.rect[0].center = (x, y)
        self.rect[1].center = (x, y)
        # self.rect[2].center = (x, y)

    def draw(self, i):
        for i in range (2):
            screen.blit(self.char[i], self.rect[i])
            i += 1

# x = 200
# y = 200
# scale = 2
running = True
user = animate(150, 400)
# user1 = animate(150, 400)
while running:
    screen.blit(bg1, (0, 0))
    user.draw(0)
    # screen.blit(user.char0_1, user.rect)
    # screen.blit(user1.char1, user1.rect1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()