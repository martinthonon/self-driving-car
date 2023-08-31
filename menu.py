import pygame

class Menu:
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # pygame.display.set_caption("Pathfinder Menu")
        self.font = pygame.font.Font(None, 36)
        self.mode = ["NEAT", "Interactif"]
        self.mode_index = 0
        self.map = ["Easy", "Medium", "Hard"]
        self.map_index = 0
        self.pop_size = ["10", "20", "30", "40", "50"]
        self.pop_index = 0
        self.start_text = self.font.render("Start Game", True, "white")
        self.mode_text = self.font.render(self.mode[0], True, "white")
        self.map_text = self.font.render(self.map[0], True, "gray")
        self.pop_text = self.font.render(self.pop_size[0], True, "gray")
        self.quit_text = self.font.render("Quit", True,"gray")
        self.selected_option = 0

    def draw(self):
        self.screen.fill((0, 0, 0))
        start_color = ("white") if self.selected_option == 0 else ("gray")
        mode_color = ("white") if self.selected_option == 1 else ("gray")
        map_color = ("white") if self.selected_option == 2 else ("gray")
        pop_color  = ("white") if self.selected_option == 3 else ("gray")
        quit_color = ("white") if self.selected_option == 4 else ("gray")
        self.start_text = self.font.render("Start Game", True, start_color)
        self.mode_text = self.font.render(self.mode[self.mode_index], True, mode_color)
        self.map_text = self.font.render(self.map[self.map_index], True, map_color)
        self.pop_text = self.font.render(self.pop_size[self.pop_index], True, pop_color)
        self.quit_text = self.font.render("Quit", True, quit_color)
        self.screen.blit(self.start_text, (self.screen_width // 2 - 50, self.screen_height // 2 - 120))
        self.screen.blit(self.mode_text, (self.screen_width // 2 - 50, self.screen_height // 2 - 90))
        self.screen.blit(self.map_text, (self.screen_width // 2 - 50, self.screen_height // 2 - 60))
        self.screen.blit(self.pop_text, (self.screen_width // 2 - 50, self.screen_height // 2 - 30))
        self.screen.blit(self.quit_text, (self.screen_width // 2 - 50, self.screen_height // 2 + 0))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                key = event.key
                selected_option_mode = self.selected_option % 5

                match key:
                    case pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % 5
                    case pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % 5
                    case pygame.K_RIGHT if selected_option_mode == 1:
                        self.mode_index = (self.mode_index + 1) % 2
                    case pygame.K_LEFT if selected_option_mode == 1:
                        self.mode_index = (self.mode_index - 1) % 2
                    case pygame.K_RIGHT if selected_option_mode == 2:
                        self.map_index = (self.map_index + 1) % 3
                    case pygame.K_LEFT if selected_option_mode == 2:
                        self.map_index = (self.map_index - 1) % 3
                    case pygame.K_RIGHT if selected_option_mode == 3:
                        self.pop_index = (self.pop_index + 1) % 5
                    case pygame.K_LEFT if selected_option_mode == 3:
                        self.pop_index = (self.pop_index - 1) % 5
                    case pygame.K_RETURN if selected_option_mode == 0:
                        return "start", self.mode[self.mode_index], \
                        self.map[self.map_index], self.pop_size[self.pop_index]
                    case pygame.K_RETURN if selected_option_mode == 4:
                        pygame.quit()
                        exit()
        return None

