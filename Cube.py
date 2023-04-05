
import pygame
import random
import copy
import numpy as np
import math
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
random_colors_dic = {0: [[8, 4, 1], 'BLUE'], 1: [[8, 5, 1], 'GREEN'], 2: [[8, 6, 1], 'YELLOW'], 3: [[9, 4, 2], 'BLUE'], 4: [[9, 5, 2], 'RED'], 5: [[9, 6, 2], 'YELLOW'], 6: [[10, 4, 3], 'BLUE'], 7: [[10, 5, 3], 'YELLOW'], 8: [[10, 6, 3], 'ORANGE'], 9: [[4, 4, 1], 'RED'], 10: [[4, 5, 1], 'ORANGE'], 11: [[4, 6, 1], 'BLUE'], 12: [[5, 4, 1], 'WHITE'], 13: [[5, 5, 1], 'YELLOW'], 14: [[5, 6, 1], 'RED'], 15: [[6, 4, 1], 'YELLOW'], 16: [[6, 5, 1], 'YELLOW'], 17: [[6, 6, 1], 'GREEN'], 18: [[4, 8, 1], 'ORANGE'], 19: [[4, 9, 2], 'YELLOW'], 20: [[4, 10, 3], 'RED'], 21: [[5, 8, 1], 'WHITE'], 22: [[5, 9, 2], 'GREEN'], 23: [[5, 10, 3], 'GREEN'], 24: [[6, 8, 1], 'RED'], 25: [[6, 9, 2], 'RED'], 26: [[6, 10, 3], 'WHITE'], 27: [[0, 4, 3], 'YELLOW'], 28: [[0, 5, 3], 'BLUE'], 29: [[0, 6, 3], 'GREEN'], 30: [[1, 4, 2], 'WHITE'], 31: [[1, 5, 2], 'ORANGE'], 32: [[1, 6, 2], 'BLUE'], 33: [[2, 4, 1], 'YELLOW'], 34: [[2, 5, 1], 'GREEN'], 35: [[2, 6, 1], 'WHITE'], 36: [[4, 12, 3], 'WHITE'], 37: [[4, 13, 3], 'ORANGE'], 38: [[4, 14, 3], 'GREEN'], 39: [[5, 12, 3], 'WHITE'], 40: [[5, 13, 3], 'WHITE'], 41: [[5, 14, 3], 'RED'], 42: [[6, 12, 3], 'GREEN'], 43: [[6, 13, 3], 'ORANGE'], 44: [[6, 14, 3], 'RED'], 45: [[4, 0, 3], 'ORANGE'], 46: [[4, 1, 2], 'BLUE'], 47: [[4, 2, 1], 'BLUE'], 48: [[5, 0, 3], 'GREEN'], 49: [[5, 1, 2], 'BLUE'], 50: [[5, 2, 1], 'ORANGE'], 51: [[6, 0, 3], 'WHITE'], 52: [[6, 1, 2], 'RED'], 53: [[6, 2, 1], 'ORANGE']}
colors_dic=random_colors_dic
WIDTH, HEIGHT = 1000, 1000  # 700,500
FPS = 60
delay = 300
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
TEXT_FONT = pygame.font.SysFont("comicsans", 30)
SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI CUBE")


def Transition_Mode(len_T1, len_T2, T1_colors, T2_colors, counterclockwise):
    colors_dic_Temp = copy.deepcopy(colors_dic)
    if counterclockwise == True:
        for i, key in enumerate(T1_colors):
            i = i+2
            if i >= len_T1:
                i = i-(len_T1)
            colors_dic[key][1] = colors_dic_Temp[T1_colors[i]][1]

        for i, key in enumerate(T2_colors):
            i = i+3
            if i >= len_T2:
                i = i-(len_T2)
            colors_dic[key][1] = colors_dic_Temp[T2_colors[i]][1]
    else:
        for i, key in enumerate(reversed(T1_colors)):  # down

            i = (len_T1-1-i)-2
            colors_dic[key][1] = colors_dic_Temp[T1_colors[i]][1]
        for i, key in enumerate(reversed(T2_colors)):  # down

            i = (len_T2-1-i)-3
            colors_dic[key][1] = colors_dic_Temp[T2_colors[i]][1]


def color_handling(MODE):
    keys = pygame.key.get_pressed()
    T1_colors = []
    T2_colors = []
    counterclockwise = True
    if keys[pygame.K_1] or MODE[0]:  # mode1
        T1_colors = [
            9, 12, 15, 16, 17, 14, 11, 10  # plane transition
        ]
        T2_colors = [
            47, 50, 53, 0, 1, 2, 24, 21, 18, 35, 34, 33  # bar transition
        ]
    if keys[pygame.K_2] or MODE[1]:  # mode2
        T1_colors = [
            # plane transition
        ]
        T2_colors = [
            46, 49, 52, 3, 4, 5, 25, 22, 19, 32, 31, 30                      # bar transition
        ]
    if keys[pygame.K_3] or MODE[2]:  # mode3
        T1_colors = [
            38, 41, 44, 43, 42, 39, 36, 37  # plane transition
        ]
        T2_colors = [

            45, 48, 51, 6, 7, 8, 26, 23, 20, 29, 28, 27  # bar transition
        ]
    if keys[pygame.K_4] or MODE[3]:  # mode4
        T1_colors = [
            27, 30, 33, 34, 35, 32, 29, 28,  # plane transition
        ]
        T2_colors = [
            45, 46, 47, 9, 10, 11, 18, 19, 20, 36, 37, 38   # bar transition
        ]
    if keys[pygame.K_5] or MODE[4]:  # mode5
        T1_colors = [
            # plane transition
        ]
        T2_colors = [
            48, 49, 50, 12, 13, 14, 21, 22, 23, 39, 40, 41  # bar transition
        ]
    if keys[pygame.K_6] or MODE[5]:  # mode6
        T1_colors = [
            0, 3, 6, 7, 8, 5, 2, 1   # plane transition
        ]
        T2_colors = [
            44, 43, 42, 26, 25, 24, 17, 16, 15, 53, 52, 51  # bar transition
        ]
    if keys[pygame.K_7] or MODE[6]:  # mode7
        T1_colors = [
            50, 53, 52, 51, 48, 45, 46, 47   # plane transition
        ]
        T2_colors = [
            9, 12, 15, 0, 3, 6, 44, 41, 38, 27, 30, 33  # bar transition
        ]
    if keys[pygame.K_8] or MODE[7]:  # mode8
        T1_colors = [
            # plane transition
        ]
        T2_colors = [
            10, 13, 16, 1, 4, 7, 43, 40, 37, 28, 31, 34  # bar transition
        ]
    if keys[pygame.K_9] or MODE[8]:  # mode9
        T1_colors = [
            18, 21, 24, 25, 26, 23, 20, 19  # plane transition
        ]
        T2_colors = [
            11, 14, 17, 2, 5, 8, 42, 39, 36, 29, 32, 35  # bar transition
        ]

    # if keys[pygame.K_LEFT] or MODE[9]:
    #     len_T1 = len(T1_colors)
    #     len_T2 = len(T2_colors)
    #     counterclockwise=True
    
    #     Transition_Mode(len_T1,len_T2,T1_colors,T2_colors,counterclockwise)
    # if keys[pygame.K_RIGHT] or MODE[10]:
    
    len_T1 = len(T1_colors)
    len_T2 = len(T2_colors)
    pygame.time.delay(delay)
    # counterclockwise=False
    Transition_Mode(len_T1, len_T2, T1_colors, T2_colors, counterclockwise)




def random_color():
    random_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        if random.random() > 0.5:
            r = 1
        else:
            r = 0
        random_list.append(r)
    random.shuffle(random_list)
    if random.random() > 0.5:
        random_list[9] = 1
        random_list[10] = 0
    else:
        random_list[9] = 0
        random_list[10] = 1
    MODE = random_list
    return MODE


def draw(score,TEXT):
    WIN.fill(BLACK)

    for key, value in colors_dic.items():
        RGB_color = RGB_COLORS_DIC[value[1]]
        pygame.draw.rect(
            WIN, RGB_color, (40*value[0][0]+250, 40*value[0][1]+100, 30, 30))
    text = SCORE_FONT.render(f"{score}", 1, WHITE)
    WIN.blit(text, (150, 150))
    text=  TEXT_FONT.render(f"mode : {TEXT}",1,WHITE)
    WIN.blit(text,(700,600))
    pygame.display.update()


def calculate_init():

    Ccolors_dic = copy.deepcopy(colors_dic)
    # d = {"GREEN": 1, "WHITE": 2, "YELLOW": 3, "RED": 4, "BLUE": 5, "ORANGE": 6}
    # training_list=[]
    for key, value in Ccolors_dic.items():
        # training_list.append(d[value[1]])
        ###########
        STD_value = value[0]
        if key in [3, 4, 5]:
            STD_value[0] = STD_value[0]-1
        if key in [19, 22, 25]:
            STD_value[1] = STD_value[1]-1
        if key in [32, 31, 30]:
            STD_value[0] = STD_value[0]+1
        if key in [46, 49, 52]:
            STD_value[1] = STD_value[1]+1
        if key in [6, 7, 8]:
            STD_value[0] = STD_value[0]-2
        if key in [20, 23, 26]:
            STD_value[1] = STD_value[1]-2
        if key in [27, 28, 29]:
            STD_value[0] = STD_value[0]+2
        if key in [45, 48, 51]:
            STD_value[1] = STD_value[1]+2
        if key in range(36, 45):
            STD_value[1] = STD_value[1]-8
        if key not in range(9,18):
          if key in range(36,45):
            STD_value[2]+=2
          else:
            STD_value[2]+=1

    return Ccolors_dic  # ,training_list


def calculate_distance(Ccolors_dic):
    weight=1
    graphical_score = 0
    optimal_std_array = np.array(
        [3.40388474, 2.35147393, 3.16797051, 3.40388474, 2.17913987,
         2.17913987])
    GREEN_std = 0
    WHITE_std = 0
    YELLOW_std = 0
    RED_std = 0
    BLUE_std = 0
    ORANGE_std = 0
    Color_Distance_Dic = {"GREEN": [], "WHITE": [],
                          "YELLOW": [], "RED": [], "BLUE": [], "ORANGE": []}
    for key, value in Ccolors_dic.items():
        Color_Distance_Dic[value[1]].append(value[0])
    #####################################################
    for key, value in Color_Distance_Dic.items():
        sumX = 0
        sumY = 0
        sumZ = 0
        varX = 0
        varY = 0
        varZ = 0
        for point in value:
            sumX += point[0]
            sumY += point[1]
            sumZ += point[2]
        meanX = (sumX/6)
        meanY = (sumY/6)
        meanZ = (sumZ/6)
        for point in value:
            varX += (point[0]-meanX)**2
            varY += (point[1]-meanY)**2
            varZ += (point[2]-meanZ)**2
        varX = varX/6
        varY = varY/6
        varZ = varZ/6
        if key == "GREEN":
            GREEN_std = (varX**0.5+varY**0.5+varZ**0.5)/3
        if key == "WHITE":
            WHITE_std = (varX**0.5+varY**0.5+varZ**0.5)/3
        if key == "YELLOW":
            YELLOW_std = (varX**0.5+varY**0.5+varZ**0.5)/3
        if key == "BLUE":
            BLUE_std = (varX**0.5+varY**0.5+varZ**0.5)/3
        if key == "ORANGE":
            ORANGE_std = (varX**0.5+varY**0.5+varZ**0.5)/3
        if key == "RED":
            RED_std = (varX**0.5+varY**0.5+varZ**0.5)/3
    std_array = np.array(
        [GREEN_std, WHITE_std, YELLOW_std, RED_std, BLUE_std, ORANGE_std])
    np_sum = np.sum((optimal_std_array-std_array)**2)
    if np_sum == 0:
        np_distance_score = float('inf')
    else:
        np_distance_score = np_sum**-0.5
    sigmoid_score = 1/(1+math.exp(-np_distance_score))
    ####################################################################################################
    for key, value in Color_Distance_Dic.items():
        value = np.array(value)
        color_score=0
        for point1 in value:
            for point2 in value:
                distance = np.sum(np.abs(point1-point2))

                if distance == 1:
                    graphical_score += 1
                    color_score+=1
        if color_score>=14:
            weight+=5
    graphical_score = graphical_score/2
    score = 100*((1000*sigmoid_score-640)/360)*0.3+graphical_score/72*70
    return int(score), Color_Distance_Dic,weight


def main():
    run = True
    clock = pygame.time.Clock()
    r = -1
    MODE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            r = -r
            pygame.time.delay(100)

        if r > 0:
            global delay
            delay = 0
            MODE = random_color()
            # counter+=1
            # if counter==100:
            #     r=-r
        else:
            delay = 300
            MODE = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Ccolors_dic= calculate_init()
        print(Ccolors_dic)
        score,Color_Distance_Dic,weight = calculate_distance(Ccolors_dic)

        color_handling(MODE)
        draw(score,"GAME")
    pygame.quit()


if __name__ == "__main__":
    main()
