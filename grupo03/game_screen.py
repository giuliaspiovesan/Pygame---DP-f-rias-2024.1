import pygame
import random
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from banco_palavras import lista_palavras

class Retangulo:
    def __init__(self, x_input, y_input, vel_y, img_input):
        self.x_input = x_input
        self.y_input = y_input
        self.vel_y = vel_y
        self.img_input = img_input
    def update(self):
        if self.y_input < HEIGHT:
            self.y_input += self.vel_y
        else:
            self.y_input = -100
            self.x_input = random.randint(0, WIDTH-self.img_input.get_width())
    def draw(self, window):
        window.blit(self.img_input, (self.x_input, self.y_input))

def game_screen(window):
    clock = pygame.time.Clock()
    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    img_input = dicionario_de_arquivos['img_input'] 
    ret = Retangulo(random.randint(0, WIDTH-img_input.get_width()), -100, 1, img_input)

    pontos = 0
    vidas = 3
    i = 3 
    conta_jogadas = 1
    texto_digitado = ''

    font = dicionario_de_arquivos['font']

    som_sucesso = pygame.mixer.Sound('grupo03/assets/snd/success.wav')
    som_wah = pygame.mixer.Sound('grupo03/assets/snd/wah-wah.wav')

    def sorteia_palavra(tam):
        selecionadas = []
        for pal in lista_palavras:
            if len(pal) == tam:
                selecionadas.append(pal)
        sorteada = random.choice(selecionadas)
        return sorteada
    palavra = sorteia_palavra(i)

    while state != DONE:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            elif event.type == pygame.KEYDOWN:
                letra = event.unicode
                if letra.isalpha():
                    texto_digitado += letra

        ret.update()

        if ret.y_input >= HEIGHT:
            if texto_digitado == palavra:
                pontos += 1
                som_sucesso.play()
                texto_digitado = ''
                ret.y_input = -100
                ret.x_input = random.randint(0, WIDTH-img_input.get_width())
                conta_jogadas += 1
                palavra = sorteia_palavra(i)
            else:
                vidas -= 1
                ret.vel_y += 1
                som_wah.play()
                if vidas > 0:
                    texto_digitado = ''
                    ret.y_input = -100
                    ret.x_input = random.randint(0, WIDTH-img_input.get_width())
                    conta_jogadas += 1
                    palavra = sorteia_palavra(i)   
        if conta_jogadas == 3:
            conta_jogadas = 0
            i += 1
        if vidas == 0:
            with open('ranking.txt', 'a') as file:
                file.write(f'{pontos}\n')
            pontuacoes = []
            with open('ranking.txt', 'r') as file:
                for line in file:
                    pontuacao = int(line.strip())
                    pontuacoes.append(pontuacao)
            pontuacoes.sort(reverse=True)
            return 'game over', pontos, pontuacoes[:10]
        
         
        texto = font.render(palavra, True, (255, 255, 255))
        digitado = font.render(texto_digitado, True, (0, 0, 0))
        txt_vidas = font.render(f'Vidas: {vidas}', True, (255, 255, 255))
        txt_pontos = font.render(f'Pontos: {pontos}', True, (255, 255, 255))
        ydig = ret.y_input + (ret.img_input.get_height() / 2) + (ret.img_input.get_height() / 4) - digitado.get_height() / 2
        xpal = ret.x_input + (ret.img_input.get_width() - texto.get_width()) / 2

        window.fill(BLACK)  
        ret.draw(window) 
        window.blit(texto, (xpal, ret.y_input))
        window.blit(digitado, (xpal, ydig))
        window.blit(txt_vidas, (30, 50))
        window.blit(txt_pontos, (30, 80))
        pygame.display.update()  

    return state