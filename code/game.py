#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 480))  # Configura a janela do jogo

    def run(self):
        while True: #chamar o MENU
            menu = Menu(self.window)
            menu.run()
            pass


            #for event in pygame.event.get():
            #    if event.type == pygame.QUIT:  # fechando a janela
            #       running = False

        #pygame.quit()  # encerrando o pygame


