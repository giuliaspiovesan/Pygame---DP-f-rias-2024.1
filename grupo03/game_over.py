import pygame
import random
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos

def game_over(window, pontos, ranking):
    clock = pygame.time.Clock()
    dicionario_de_arquivos = carrega_arquivos()
    font_resto = dicionario_de_arquivos['font']
    font = dicionario_de_arquivos['font_media']

    DONE = 0
    PLAYING = 1
    state = PLAYING
    
    while state != DONE:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE

        txt_game = font.render('GAME OVER!!', True, (255, 0, 0))
        txt_pnt = font_resto.render(f'Pontuação: {pontos}', True, (255, 255, 255))
        txt_top10 = font_resto.render('Top 10 pontos: ', True, (255,255,255))

        window.fill((0, 0, 0))
        window.blit(txt_game, (100,50))
        window.blit(txt_pnt, (550,50))
        window.blit(txt_top10, (300, 150))

        for i in range(len(ranking[:10])):
            txt_rank = font_resto.render(f'{ranking[i]}', True, (255,255,255))
            window.blit(txt_rank, (450,200+i*50))

        pygame.display.update()  

    return state
