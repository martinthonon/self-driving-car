import pygame
import os
from menu import Menu
from game import Game

pygame.init()

def main():

    menu = Menu()
    
    running = True
    while running:
        option = menu.handle_events()
        if option is not None and option[0] == "start":
            game = Game(option[2])
            if option[1] == "Interactif":
                game.run()
            pop_size = option[3]
            config_path = os.path.join('config.txt') 
            game.run_neat(pop_size, config_path)
        
        menu.draw()
        pygame.display.flip()

if __name__ == '__main__':
    main()
    