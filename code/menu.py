#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png') #adicionando a imagem menu
        self.rect = self.surf.get_rect(left=0, top=0) #retângulo

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')  # apenas carregar a musica
        pygame.mixer_music.play(-1)  # para tocar a musica e manter o loop (-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # imagem no retangulo
            pygame.display.flip()
            #Fechar a janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fechar a janela
                    quit() #encerrando o jogo

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


