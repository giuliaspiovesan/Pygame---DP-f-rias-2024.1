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
    x_input = random.randint(0, WIDTH-img_input.get_width())
    y_input = -100
    vel_y = 1

    pontos = 0
    vidas = 3
    i = 3 # contar o tamanho das palavras
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
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            elif event.type == pygame.KEYDOWN:
                letra = event.unicode
                if letra.isalpha():
                    texto_digitado += letra



        if y_input < HEIGHT:
            y_input += vel_y

        elif y_input >= HEIGHT:
            if texto_digitado == palavra:
                pontos += 1
                som_sucesso.play()
                texto_digitado = ''
                y_input = -100
                x_input = random.randint(0, WIDTH-img_input.get_width())
                conta_jogadas += 1
                palavra = sorteia_palavra(i)

            else:
                vidas -= 1
                vel_y += 1
                som_wah.play()
                if vidas > 0:
                    texto_digitado = ''
                    y_input = -100
                    x_input = random.randint(0, WIDTH-img_input.get_width())
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

            
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor preta
        window.blit(img_input, (x_input, y_input))  # Desenha imagem input na tela
        texto = font.render(palavra, True, (255, 255, 255))
        xpal = x_input + (img_input.get_width() - texto.get_width()) / 2
        window.blit(texto, (xpal, y_input))

        digitado = font.render(texto_digitado, True, (0, 0, 0))
        ydig = y_input + (img_input.get_height() / 2) + (img_input.get_height() / 4) - digitado.get_height() / 2
        window.blit(digitado, (xpal, ydig))

        txt_vidas = font.render(f'Vidas: {vidas}', True, (255, 255, 255))
        window.blit(txt_vidas, (30, 50))

        txt_pontos = font.render(f'Pontos: {pontos}', True, (255, 255, 255))
        window.blit(txt_pontos, (30, 80))
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state