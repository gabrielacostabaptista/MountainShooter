#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)  # Retângulo
        self.running = True
        self.menu_option = 0
        self.font_name = "Lucida Sans Typewriter"
        self.text_size_title = 50
        self.text_size_option = 20

        # Configurar música
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

    def run(self):
        while self.running:
            # Desenhar o menu
            self.window.blit(source=self.surf, dest=self.rect)  # Imagem no retângulo
            self.draw_menu()

            # Lidar com eventos
            self.handle_events()

            # Atualizar a tela
            pygame.display.flip()

        return MENU_OPTION[self.menu_option]  # Retorna a opção selecionada

    def draw_menu(self):
        """Desenha os elementos do menu na tela."""
        # Desenhar títulos
        self.menu_text(self.text_size_title, "Mountain", COLOR_ORANGE, (WIN_WIDTH / 2, 70))
        self.menu_text(self.text_size_title, "Shooter", COLOR_ORANGE, (WIN_WIDTH / 2, 120))

        # Desenhar opções
        for i in range(len(MENU_OPTION)):
            color = COLOR_YELLOW if i == self.menu_option else COLOR_WHITE
            self.menu_text(self.text_size_option, MENU_OPTION[i], color, (WIN_WIDTH / 2, 170 + 30 * i))

    def handle_events(self):
        """Lida com os eventos de entrada."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.menu_option = (self.menu_option + 1) % len(MENU_OPTION)  # Ciclado
                if event.key == pygame.K_UP:
                    self.menu_option = (self.menu_option - 1) % len(MENU_OPTION)
                if event.key == pygame.K_RETURN:  # Seleção de opção
                    self.running = False

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Renderiza e exibe o texto no menu."""
        text_font: Font = pygame.font.SysFont(name=self.font_name, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
