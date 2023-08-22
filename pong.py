import pygame

pygame.init()

#DEFINIR O FPS ------------->
gameClock = pygame.time.Clock()

#DEFINIÇÃO DAS DIMENSÕES DA TELA ------------->
tela = pygame.display.set_mode((1200, 700))

#NOME Q EXIBE NA BARRA SUPERIOR ------------->
pygame.display.set_caption("Pong")

# CORES ------------->

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# DEFININDO A FONTE (TIPO, TAMANHO, NEGRITO, ITALICO) ------------->

fonte = pygame.font.SysFont("arial", 70, True, False)
pontos_esq = 0
pontos_dir = 0

# CONFUGURAÇÕES DA BOLINHA ----------------------->

width = 30
height = 30

x = 700-height
y = 350-width
velocity_x = 10
velocity_y = 10

# CONFIGURAÇÕES DAS RAQUETES ------------------------->

heightRet = 115
widthRet = 25

xRet_esq = 40
yRet_esq = 330

xRet_dir = 1140
yRet_dir = 330

vel = 10

# IMPORTANDO E REESCALANDO A LINHA PONTILHADA ------------>

image = pygame.image.load('pixil-frame-0.png')
image = pygame.transform.scale(image, (4, 700))

# CONDIÇÃO PRA RODAR ---------------------------->

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # DEFININDO RECONHECEDOR DE TECLAS --------------------->

    keys = pygame.key.get_pressed()

    # CONFIGURAÇÕES DA PONTUAÇÃO ---------------------->

    mensagem_esq = f"{pontos_esq}"
    formatacao_esq = fonte.render(mensagem_esq, False, WHITE)

    mensagem_dir = f"{pontos_dir}"
    formatacao_dir = fonte.render(mensagem_dir, False, WHITE)

    # MOVIMENTAÇÃO DA BOLINHA ---------------------------->

    x += velocity_x
    y += velocity_y

    if x > 1200-width:    
        velocity_x = -10
        pontos_esq += 1
    elif x < 0:
        velocity_x = 10
        pontos_dir += 1
    if y > 700-width:
        velocity_y = -10
    elif y < 0:
        velocity_y = 10

    # MOVIMENTAÇÃO DAS RAQUETES -------------------------->

    if keys[pygame.K_w] and yRet_esq > 0:
        yRet_esq -= vel
    if keys[pygame.K_s] and yRet_esq < 700-heightRet:
        yRet_esq += vel

    if keys[pygame.K_UP] and yRet_dir > 0:
        yRet_dir -= vel
    if keys[pygame.K_DOWN] and yRet_dir < 700-heightRet:
        yRet_dir += vel

    # DESENHAR NA TELA --------------------------------->

    tela.fill(BLACK)

    tela.blit(image, (600, 3))
    
    tela.blit(formatacao_esq, (300, 40))
    tela.blit(formatacao_dir,(900, 40))
    
    # DEFINIÇÃO DA BOLA E DAS RAQUETES (ONDE, COR, POSIÇÃO INICIAL E DIMENSÕES) ----------------->

    bola = pygame.draw.ellipse(tela, RED, (x, y, width, height))
    raquete_esq = pygame.draw.rect(tela, WHITE, (xRet_esq, yRet_esq, widthRet, heightRet), 2)
    raquete_dir = pygame.draw.rect(tela, WHITE, (xRet_dir, yRet_dir, widthRet, heightRet), 2)

    # RECONHECER COLISÃO ------------->

    if bola.colliderect(raquete_esq):
        velocity_x = 10
    if bola.colliderect(raquete_dir):
        velocity_x = -10

    # JOGO RODANDO A 74 FPS -------------->
    gameClock.tick(74)

    # ATUALIZAÇÃO DA TELA DURANTE O LOOP
    pygame.display.update()
pygame.quit()