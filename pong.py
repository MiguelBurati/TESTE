import pygame

pygame.init()

gameClock = pygame.time.Clock()

tela = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Pong")

RED = (255, 0, 0)
BLACK = (0, 0, 0)


width = 20
height = 20

x = 600-height
velocity_x = 15
y = 350-width
velocity_y = 15

vel = 1

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x += velocity_x

    if x > 1200-width:    
        velocity_x = -15
    elif x < 0:
        velocity_x = 15
    tela.fill(BLACK)
    pygame.draw.ellipse(tela, RED, (x, y, width, height))


    pygame.display.update()

    gameClock.tick(60)
pygame.quit()