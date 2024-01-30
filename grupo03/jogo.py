import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_over import game_over
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pega palavras!')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state, pontos, ranking = game_screen(window)
    elif state == 'game over':
        state = game_over(window, pontos, ranking)
    else:
        state = QUIT

pygame.quit()  

