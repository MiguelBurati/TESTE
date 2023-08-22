import pygame

pygame.init()

win = pygame.display.set_mode((1300, 800))
pygame.display.set_caption("Pong")

RED = (255, 0, 0)

x = 75
y = 330

a = 1210
b = 330

width = 20
height = 110
vel = 2

position_x = 1300
position_y = 800
velocity_x = 1
velocity_y = 1

pontos_esq = 0
pontos_dir = 0

font = pygame.font.SysFont('arial', 130, True, False)

drawGroup = pygame.sprite.Group()

barra = pygame.sprite.Sprite(drawGroup)
barra.image = pygame.image.load("pixil-frame-0.png")
barra.image = pygame.transform.scale(barra.image, [5, 800])
barra.rect = pygame.Rect(650, 4, 0, 0)

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    position_x += velocity_x
    position_y += velocity_y

    if position_x > 1240:
        velocity_x = -1
    elif position_x < 0:
        velocity_x = 1

    if position_y > 765:
        velocity_y = -1
    elif position_y < 0:
        velocity_y = 1

    #  MOVIMENTANDO--------------------------------------->

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y > 0:
        y -= vel

    if keys[pygame.K_DOWN] and y < 800-height:
        y += vel

    if keys[pygame.K_w] and b > 0:
        b -= vel

    if keys[pygame.K_s] and b < 800-height:
        b += vel

    #  DESENHANDO--------------------------------------->

    win.fill((0,0,0))

    pygame.draw.rect(win, (55, 55, 55), (60, 0, 4, 1300))
    pygame.draw.rect(win, (55, 55, 55), (1240, 0, 4, 1300))
    drawGroup.draw(win)

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height), 2) #BARRA ESQUERDA
    pygame.draw.rect(win, (255, 0, 0), (a, b, width, height), 2) #BARRA DIREITA

    mensagem_esq = f'{pontos_esq}'
    mensagem_dir = f'{pontos_dir}'
    texto_formatado_esq = font.render(mensagem_esq, False, (255, 255, 255)) #PONTUAÇÃO DA ESQUERDA
    texto_formatado_dir = font.render(mensagem_esq, False, (255, 255, 255)) #PONTUAÇÃO DA DIREITA

    pygame.draw.ellipse(win, RED, [position_x, position_y, 40, 40])

    win.blit(texto_formatado_dir, (315, 1))
    win.blit(texto_formatado_esq, (955, 1))
    pygame.display.update()
pygame.quit()