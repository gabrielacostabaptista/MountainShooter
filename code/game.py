#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
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

        while self.running:  # Loop principal
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Evento de sair
                    self.running = False

            # Atualiza o menu
            self.menu.run()

        # Encerra o Pygame
        pygame.quit()

