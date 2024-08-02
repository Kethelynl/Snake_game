#criar loop infinito
#desenhar os objetos na tela
#fazer logica de fim de jogo
#pegar as interações do usúario

import pygame
import random

pygame.init()

#criar tela

pygame.display.set_caption("Jogo Snake")
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#definindo cores

preto = (0, 0, 0)
branca = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
amarelo = (0, 0, 255)

# parametros

tamanho_quatrado = 20
velocidade = 15

def gerar_comida():

    comidaX = round(random.randrange(0, largura - tamanho_quatrado) / 20.0) * 20
    comidaY = round(random.randrange(0, altura - tamanho_quatrado) / 20.0) * 20
    return comidaX, comidaY

def desenhar_comida(tamanho, comidaX, comidaY):
    pygame.draw.rect(tela, verde, [comidaX, comidaY, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont('Helvetica', 35)
    texto = fonte.render(f'Pontos: {pontuacao}', True, amarelo)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN: #tecla para baixo
        velocidadeX = 0
        velocidadeY = tamanho_quatrado
    if tecla == pygame.K_UP:
        velocidadeX = 0
        velocidadeY = -tamanho_quatrado
    if tecla == pygame.K_RIGHT:
        velocidadeX = tamanho_quatrado
        velocidadeY = 0
    if tecla == pygame.K_LEFT:
        velocidadeX = -tamanho_quatrado
        velocidadeY = 0

    return velocidadeX, velocidadeY
def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidadeX = 0
    velocidadeY = 0

    tamanho_cobra = 1
    pixels = []

    comidaX, comidaY = gerar_comida()

    while not fim_jogo:

        tela.fill(preto) # pega a cor para colocar na tela
        for evento in pygame.event.get(): #retorna todos os eventos que o usuário fez.
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidadeX, velocidadeY = selecionar_velocidade(evento.key)


        #desenha comida
        desenhar_comida(tamanho_quatrado, comidaX, comidaY)

        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        # atualizar a posição da cobra
        x += velocidadeX
        y += velocidadeY

        #desenhar cobra
        #caminhada da cobra
        pixels.append([x,  y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        #se a cobra bateu no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        desenhar_cobra(tamanho_quatrado, pixels)

        desenhar_pontuacao(tamanho_cobra - 1)
        pygame.display.update()

        if x == comidaX and y == comidaY:
            tamanho_cobra += 1
            comidaX, comidaY = gerar_comida()
        relogio.tick(24)
rodar_jogo()