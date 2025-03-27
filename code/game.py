#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        # Inicializa o Pygame
        pygame.init()

        # Configura a janela
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Dimensões da janela
        pygame.display.set_caption("Meu Jogo com Menu")  # Título da janela

        # Controle de execução
        self.running = True

        # Instancia o menu
        self.menu = Menu(self.window)

    def run(self):
        while True:
            menu = Menu (self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass

