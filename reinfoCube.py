
import math
import Cube
import pygame
import random
import neat
import os
import pickle
import copy


pygame.init()
colors_dic = {0: [[8, 4, 1], 'GREEN'],
              1: [[8, 5, 1], 'GREEN'],
              2: [[8, 6, 1], 'GREEN'],
              3: [[9, 4, 2], 'GREEN'],
              4: [[9, 5, 2], 'GREEN'],
              5: [[9, 6, 2], 'GREEN'],
              6: [[10, 4, 3], 'GREEN'],
              7: [[10, 5, 3], 'GREEN'],
              8: [[10, 6, 3], 'GREEN'],
              9: [[4, 4, 1], 'WHITE'],
              10: [[4, 5, 1], 'WHITE'],
              11: [[4, 6, 1], 'WHITE'],
              12: [[5, 4, 1], 'WHITE'],
              13: [[5, 5, 1], 'WHITE'],
              14: [[5, 6, 1], 'WHITE'],
              15: [[6, 4, 1], 'WHITE'],
              16: [[6, 5, 1], 'WHITE'],
              17: [[6, 6, 1], 'WHITE'],
              18: [[4, 8, 1], 'RED'],
              19: [[4, 9, 2], 'RED'],
              20: [[4, 10, 3], 'RED'],
              21: [[5, 8, 1], 'RED'],
              22: [[5, 9, 2], 'RED'],
              23: [[5, 10, 3], 'RED'],
              24: [[6, 8, 1], 'RED'],
              25: [[6, 9, 2], 'RED'],
              26: [[6, 10, 3], 'RED'],
              27: [[0, 4, 3], 'BLUE'],
              28: [[0, 5, 3], 'BLUE'],
              29: [[0, 6, 3], 'BLUE'],
              30: [[1, 4, 2], 'BLUE'],
              31: [[1, 5, 2], 'BLUE'],
              32: [[1, 6, 2], 'BLUE'],
              33: [[2, 4, 1], 'BLUE'],
              34: [[2, 5, 1], 'BLUE'],
              35: [[2, 6, 1], 'BLUE'],
              36: [[4, 12, 3], 'YELLOW'],
              37: [[4, 13, 3], 'YELLOW'],
              38: [[4, 14, 3], 'YELLOW'],
              39: [[5, 12, 3], 'YELLOW'],
              40: [[5, 13, 3], 'YELLOW'],
              41: [[5, 14, 3], 'YELLOW'],
              42: [[6, 12, 3], 'YELLOW'],
              43: [[6, 13, 3], 'YELLOW'],
              44: [[6, 14, 3], 'YELLOW'],
              45: [[4, 0, 3], 'ORANGE'],
              46: [[4, 1, 2], 'ORANGE'],
              47: [[4, 2, 1], 'ORANGE'],
              48: [[5, 0, 3], 'ORANGE'],
              49: [[5, 1, 2], 'ORANGE'],
              50: [[5, 2, 1], 'ORANGE'],
              51: [[6, 0, 3], 'ORANGE'],
              52: [[6, 1, 2], 'ORANGE'],
              53: [[6, 2, 1], 'ORANGE']}

WIDTH, HEIGHT = 1000, 1000  # 700,500
FPS = 100
delay = 250
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

RGB_COLORS_DIC = {"WHITE": WHITE, "RED": RED, "BLUE": BLUE,
                  "ORANGE": ORANGE, "GREEN": GREEN, "YELLOW": YELLOW}

CUBE_WIDTH, CUBE_HEIGHT = 100, 100

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI CUBE")


def OUTPUT_FUNC(output):

    out = int(output/15)
    if out>8:
        out=random.randint(0,8)
    return out


# def test_genomes(config):
    colors_dic_reset = copy.deepcopy(Cube.colors_dic)

    while True:
        with open(f"best_ai.pickle", "rb") as f:  # 1:135  2:200 3:300 4:401
            winner = pickle.load(f)

        run = True
        counter = 0
        clock = pygame.time.Clock()
        Cube.colors_dic = copy.deepcopy(colors_dic_reset)
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            if counter <= 50:
                MODE = Cube.random_color()
                Cube.color_handling(MODE)
                Cube.draw(0)
                counter += 1
            else:
                MODE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                factor = 0
                training_list = []
                # def g1(genomes,config1):
                Ccolors_dic = Cube.calculate_init()
                score, Color_Distance_Dic, weight = Cube.calculate_distance(
                    Ccolors_dic)
                for key, items in Color_Distance_Dic.items():
                    for i in items:
                        training_list.append(i)
                training_list = [x for row in training_list for x in row]
                net1 = neat.nn.FeedForwardNetwork.create(winner, config)
                output1 = net1.activate((training_list))
                factor = output1.index(max(output1))
                MODE[factor] = 1
                print(factor)
                Cube.color_handling(MODE)
                Cube.draw(score)
                # rating
                counter += 1


def eval_genomes(genomes, config):
    colors_dic_reset = copy.deepcopy(Cube.colors_dic)
    for genome1_id, genome1 in genomes:
        genome1.fitness = 0
        run = True
        counter = 0
        clock = pygame.time.Clock()
        clock.tick(60)
        Cube.colors_dic = copy.deepcopy(colors_dic_reset)
        Cube.draw(14, "RESET")
        pygame.time.delay(1000)
        while run:
            # init
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return 
            # random
            if counter ==-1:
                pass
            #     MODE = Cube.random_color()
            #     Cube.color_handling(MODE)
            #     Cube.draw(0, "RANDOM")
            #     counter += 1
            # start train
            else:
                MOVES_LIST = []
                training_list = []
                Ccolors_dic = Cube.calculate_init()
                score, Color_Distance_Dic, weight = Cube.calculate_distance(
                    Ccolors_dic)
                for key, items in Color_Distance_Dic.items():
                    for i in items:
                        training_list.append(i)
                training_list = [x for row in training_list for x in row]

                net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
                outputs = net1.activate((training_list))
                # print(outputs)
                for output in outputs:
                    factor = OUTPUT_FUNC(output)
                    MOVES_LIST.append(factor)
                # print(MOVES_LIST)
                for move in MOVES_LIST:
                    MODE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    MODE[move] = 1
                    Cube.color_handling(MODE)
                    Cube.draw(score, "START")
                Cube.draw(14, "DONE")
                pygame.time.delay(1000)
                # rating
                if weight > 1:
                    print("RECORD!", weight)
                if score >= 60:
                    genome1.fitness += score*3*weight
                    break
                if score >= 50:
                    genome1.fitness += score*2*weight
                    break
                if score >= 30:
                    genome1.fitness += int(score*1.5)*weight
                    break
                if score >= 20:
                    genome1.fitness += int(score*1.25)*weight
                    break
                genome1.fitness += int(score)*weight-8
                break


def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-106')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))

    p.add_reporter(neat.StatisticsReporter())
    p.add_reporter(neat.Checkpointer(1))

    p.run(eval_genomes, 100)
    # with open("best_ai.pickle", "wb") as f:
    #      pickle.dump(winner,f)


if __name__ == "__main__":

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config1.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    run_neat(config)
    # test_genomes(config)
