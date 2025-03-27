#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png') #adicionando a imagem menu
        self.rect = self.surf.get_rect(left=0, top=0) #retângulo

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')  # apenas carregar a musica
        pygame.mixer_music.play(-1)  # para tocar a musica e manter o loop (-1)

        # DESENHANDO O MENU (IMAGENS)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # imagem no retangulo
            self.menu_text(text_size=50, text="Mountain", text_color=(COLOR_ORANGE), text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(text_size =50, text="Shooter", text_color=(COLOR_ORANGE), text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=(COLOR_YELLOW),
                                   text_center_pos=((WIN_WIDTH / 2), 170 + 30 * i)) #deixando o texto amarelo
                else:
                    self.menu_text(text_size =20,text=MENU_OPTION[i], text_color=(COLOR_WHITE),
                                   text_center_pos=((WIN_WIDTH / 2), 170 + 30 * i))

            #Fechar a janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fechar a janela
                    quit() #encerrando o jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #trocar de cor quando a apertar a seta para baixo (KEY DOW)
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1 #incrementar
                        else:
                            menu_option = 0 #voltar para o inicio das opções (KEY UP)
                    if event.key == pygame.K_UP: #trocar de cor quando a apertar a seta para cima
                        if menu_option > 0:
                            menu_option -= 1 #decrementar
                        else:
                            menu_option = len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN:  # Tecla Enter
                        return MENU_OPTION[menu_option]  # Retorna a opção selecionada (REINICIA O WHILE)
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


