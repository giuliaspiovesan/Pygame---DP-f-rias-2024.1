import pygame
import random
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos

def game_over(window, pontos):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()
    font_titulo = dicionario_de_arquivos['font']
    font_grande = pygame.font.Font(None, 50)  # Tamanho grande
    font_pequena = pygame.font.Font(None, 30)  # Tamanho pequeno

    DONE = 0
    PLAYING = 1
    state = PLAYING
    
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
        
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor preta
        txt_game = font_titulo.render('GAME OVER!!', True, (255, 0, 0))
        txt_pnt = font_pequena.render(f'Sua pontuação final foi de {pontos} ponto(s)', True, (255, 255, 255))

        # Define as posições dos textos
        pos_txt_game = (250, 200)
        pos_txt_pnt = (100, 400)

        # Renderiza os textos nas posições definidas
        window.blit(txt_game, pos_txt_game)
        window.blit(txt_pnt, pos_txt_pnt)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
