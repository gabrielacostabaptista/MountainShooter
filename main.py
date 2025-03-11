import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 480))  # Configura a janela do jogo
    pygame.display.set_caption("Mountain Shooter")

    #Checando os eventos
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #fechando a janela
                running = False

    pygame.quit() #encerrando o pygame

if __name__ == "__main__":
    main()