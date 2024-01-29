import pygame
import random
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from banco_palavras import lista_palavras

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    img_input = dicionario_de_arquivos['img_input'] #imagem do input
    x_input = random.randint(0, WIDTH)
    y_input = -1
    vel_y = 1

    font = dicionario_de_arquivos['font']
    def sorteia_palavra(tam):
        selecionadas = []
        for pal in lista_palavras:
            if len(pal) == tam:
                selecionadas.append(pal)
        sorteada = random.choice(selecionadas)
        return sorteada
    
    palavra = sorteia_palavra(3)
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
        if y_input < HEIGHT:
            y_input += vel_y
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(img_input, (x_input, y_input)) #desenha imagem input na tela
        texto = font.render(palavra, True, (255,255,255))
        xpal = x_input + (img_input.get_width() - texto.get_width()) / 2
        window.blit(texto, (xpal, y_input)) 
        
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
