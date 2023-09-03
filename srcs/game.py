import neat
import pygame
import sys
import os
from car import Car


class Game:
    def __init__(self, map):
        self.screen_width = 1373
        self.screen_height = 960
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.track = pygame.image.load(os.path.join("assets", map + ".png"))

    def run(self):
        global cars
        cars = []
        cars.append(pygame.sprite.GroupSingle(Car(self.screen)))

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                cars[0].sprite.direction = -1
            elif keys[pygame.K_RIGHT]:
                cars[0].sprite.direction = 1
            else:
                cars[0].sprite.direction = 0

            self.screen.blit(self.track, (0, 0))
            if not cars[0].sprite.alive:
                    cars.pop(0)
                    break
            cars[0].draw(self.screen)
            cars[0].update()
           

            pygame.display.update()

        pygame.quit()
        sys.exit()


    def run_neat(self,pop_size, config_path):
        config = neat.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            config_path
        )
        config.pop_size = int(pop_size, 10)
        pop = neat.Population(config)
        pop.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        pop.add_reporter(stats)
        pop.run(self.eval_genomes)

    def eval_genomes(self, genomes, config):
        global cars, ge, nets

        cars = []
        ge = []
        nets = []

        for genome_id, genome in genomes:
            cars.append(pygame.sprite.GroupSingle(Car(self.screen)))
            ge.append(genome)
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            nets.append(net)
            genome.fitness = 0
        self.start_game_loop()
            

    def start_game_loop(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.track, (0, 0))

            if len(cars) == 0:
                break

            for i, car in enumerate(cars):
                ge[i].fitness += 1
                if not car.sprite.alive:
                    self.remove(i)

            for i, car in enumerate(cars):
                output = nets[i].activate(car.sprite.data())
                if output[0] > 0.7:
                    car.sprite.direction = 1
                if output[1] > 0.7:
                    car.sprite.direction = -1
                if output[0] <= 0.7 and output[1] <= 0.7:
                    car.sprite.direction = 0

            for car in cars:
                car.draw(self.screen)
                car.update()
            pygame.display.update()

    def remove(self, index):
        cars.pop(index)
        ge.pop(index)
        nets.pop(index)