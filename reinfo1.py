
import game 
import pygame
import random
import neat
import os
import pickle
import threading



def eval_genomes(genomes,config):
    WIDTH,HEIGHT=800,580
    BALL_RADIUS=7
    #WINNING_SCORE=3
    FPS=60

    WHITE=(255,255,255)
    BLACK=(0,0,0)
    RED=(255,0,0)
    PADDLE_WIDTH,PADDLE_HEIGHT=20,100
    SCORE_FONT=pygame.font.SysFont("comicsans",50)
    WIN=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("alice pong")
    hit=0
    left_hit=0
    right_hit=0
    ball=game.Ball(WIDTH//2,HEIGHT//2,BALL_RADIUS,hit,left_hit,right_hit)

    for i,(genome1_id,genome1) in  enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome2_id,genome2 in  genomes[i+1:]:
            if genome2.fitness== None :
                genome2.fitness=0 
            else:
                genome2.fitness
            run =True
            left_score=0
            right_score=0
            hit=0
            left_hit=0
            right_hit=0
            count_down=3
            clock=pygame.time.Clock()
            tl=0
            tr=0
            r=0
            l=0
            left_paddle=game.Paddle(10,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
            right_paddle=game.Paddle(WIDTH-10-PADDLE_WIDTH,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
            re=0
            re1=0
            while run:
                factor=0
                factor2=0
              
                keys=pygame.key.get_pressed()

                
                clock.tick(60)
                
                game.draw(WIN,[left_paddle,right_paddle],ball,left_score,right_score)
                
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        run=False
                        break

                
                
                ball_y_axis,ball_x_axis=ball.move(left_paddle,right_paddle,l,r)
                count=ball.hit_count(left_paddle,right_paddle)
                left_count=ball.left_hit_count(left_paddle)
                right_count=ball.right_hit_count(right_paddle)
                left_paddle_y_axis=left_paddle.move_info()
                right_paddle_y_axis=right_paddle.move_info()
                
                if ball.x-7<20 : #
                    right_score+=1
                    ball.reset(False)
                    
                elif ball.x+7>(WIDTH-20): #
                    left_score+=1
                    ball.reset(True)
                    
                info=game.game_info(left_score,right_score,count,left_paddle_y_axis,right_paddle_y_axis,ball_y_axis,ball_x_axis,PADDLE_WIDTH,WIDTH,left_count,right_count)
                info_list=info.output()
                if r==0 and l==0:
                    re1+=1
                else:
                    re1=0
                
                if 560<info_list[5] and info_list[5]<600:
                    re+=1
                else:
                    re=0
                if re>=300 or re1>=400:
                    if random.random()>0.5:
                        left_score+=1
                        ball.reset(True)
                    else:
                        left_score+=1
                        ball.reset(False)
                    
                print(info_list[5])
                # def g1(genomes,config1): 
                #1
                net1=neat.nn.FeedForwardNetwork.create(genome1, config)
                output1=net1.activate((info_list[3],info_list[4],info_list[5],info_list[6],info_list[10]))
                factor=output1.index(max(output1))
                
                if factor==0:
                    U_r=False
                    D_r=False
                if factor==1:
                    U_r=True
                    D_r=False
                    tr=0
                if factor==2:
                    U_r=False
                    D_r=True
                    tr=0
                if factor==3:
                    U_r=True
                    D_r=False
                    tr+=(1/60)
                if factor==4:
                    U_r=False
                    D_r=True
                    tr+=(1/60)
                    # return [U_r,D_r,tl]
                
                
                
                #print(info_list[8],info_list[9])
                # def g2(genomes,config2):
                #2
                net2=neat.nn.FeedForwardNetwork.create(genome2, config)
                output2=net2.activate((info_list[3],info_list[4],info_list[5],info_list[7],info_list[10]))
                
                factor2=output2.index(max(output2))
                   

        
                if factor2==0:
                    U_l=False
                    D_l=False
                if factor2==1:
                    U_l=True
                    D_l=False
                    tl=0 
                if factor2==2:
                    U_l=False
                    D_l=True
                    tl=0
                if factor2==3:
                    U_l=True
                    D_l=False
                    tl+=(1/60)
                if factor2==4:
                    U_l=False
                    D_l=True
                    tl+=(1/60)
                #     return [U_l,D_l,tr]
                # g1=g1(genomes,config1)
                # g2=g2(genomes,config2)
                left_paddle.HANDLE_LEFT_MOVE(keys,tl,U_l,D_l)
                right_paddle.HANDLE_RIGHT_MOVE(keys,tr,U_r,D_r)
                right_paddle_v=right_paddle.HANDLE_RIGHT_MOVE(keys,tr,U_r,D_r)
                left_paddle_v=left_paddle.HANDLE_LEFT_MOVE(keys,tl,U_l,D_l)
                r=right_paddle_v
                l=left_paddle_v 

                        
                if left_score>=1 or right_score >=1 or ball.hit_count(left_paddle,right_paddle)>100:
                    
                    genome1.fitness+=info_list[9]
                    genome2.fitness+=info_list[8]                 
                    break

def test_genomes(config):
    WIDTH,HEIGHT=800,580
    BALL_RADIUS=7
    WINNING_SCORE=3
    FPS=60

    WHITE=(255,255,255)
    BLACK=(0,0,0)
    RED=(255,0,0)
    PADDLE_WIDTH,PADDLE_HEIGHT=20,100
    SCORE_FONT=pygame.font.SysFont("comicsans",50)
    WIN=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("alice pong")
    hit=0
    left_hit=0
    right_hit=0
    ball=game.Ball(WIDTH//2,HEIGHT//2,BALL_RADIUS,hit,left_hit,right_hit)
    


    run =True
    left_score=0
    right_score=0
    hit=0
    left_hit=0
    right_hit=0
    count_down=3
    clock=pygame.time.Clock()
    tl=0
    tr=0
    r=0
    l=0
    left_paddle=game.Paddle(10,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
    right_paddle=game.Paddle(WIDTH-10-PADDLE_WIDTH,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
    re=0
    re1=0
    factor=0
    factor1=0
    level=1
    while True:
        with open(f"best_ai.pickle{level}", "rb") as f: # 1:135  2:200 3:300 4:401
            winner=pickle.load(f)
        pygame.time.delay(1000)
        run=True
        while run:
            factor1=0
            factor=0
            keys=pygame.key.get_pressed()

            
            clock.tick(60)
            
            
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    break

            
            
            ball_y_axis,ball_x_axis,ball_v=ball.move(left_paddle,right_paddle,l,r)
            count=ball.hit_count(left_paddle,right_paddle)
            left_count=ball.left_hit_count(left_paddle)
            right_count=ball.right_hit_count(right_paddle)
            left_paddle_y_axis=left_paddle.move_info()
            right_paddle_y_axis=right_paddle.move_info()
            if ball_v>450:
                color=RED
            else:
                color=WHITE
            game.draw(WIN,[left_paddle,right_paddle],ball,color,left_score,right_score)
            if ball.x<0 : #
                right_score+=1
                game.draw(WIN,[left_paddle,right_paddle],ball,color,left_score,right_score)
                count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
                WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
                pygame.display.update()
                pygame.time.delay(1000)
                count_down+=-1
                game.draw(WIN,[left_paddle,right_paddle],ball,color,left_score,right_score)
                count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
                WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
                pygame.display.update()
                pygame.time.delay(1000)
                count_down+=-1
                game.draw(WIN,[left_paddle,right_paddle],ball,color,left_score,right_score)
                count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
                WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
                pygame.display.update()
                pygame.time.delay(1000)
                count_down=3
                ball.reset(False)
                
            elif ball.x>(WIDTH): #
                left_score+=1
                game.draw(WIN,[left_paddle,right_paddle],ball,color,left_score,right_score)
                count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
                WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
                pygame.display.update()
                pygame.time.delay(1000)
                count_down+=-1
                game.draw(WIN,[left_paddle,right_paddle],ball,color,left_score,right_score)
                count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
                WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
                pygame.display.update()
                pygame.time.delay(1000)
                count_down+=-1
                game.draw(WIN,[left_paddle,right_paddle],ball,color,left_score,right_score)
                count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
                WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
                pygame.display.update()
                pygame.time.delay(1000)
                count_down=3
                ball.reset(True)
                
            info=game.game_info(left_score,right_score,count,left_paddle_y_axis,right_paddle_y_axis,ball_y_axis,ball_x_axis,PADDLE_WIDTH,WIDTH,left_count,right_count)
            info_list=info.output()
            if r==0 and l==0:
                re1+=1
            else:
                re1=0
            
            if 560<info_list[5] and info_list[5]<600:
                re+=1
            else:
                re=0
            if re>=300 or re1>=400:
                if random.random()>0.5:
        
                    ball.reset(True)
                else:
                    ball.reset(False)
                

            net1=neat.nn.FeedForwardNetwork.create(winner, config)
            output1=net1.activate((info_list[3],info_list[4],info_list[5],info_list[6],info_list[10]))
            factor=output1.index(max(output1))
            
            if factor==0:
                U_r=False
                D_r=False
            if factor==1:
                U_r=True
                D_r=False
                tr=0
            if factor==2:
                U_r=False
                D_r=True
                tr=0
            if factor==3:
                U_r=True
                D_r=False
                tr+=(1/60)
            if factor==4:
                U_r=False
                D_r=True
                tr+=(1/60)   

            
            if keys[pygame.K_SPACE]:

                U_l=False
                D_l=False
            else:
                if keys[pygame.K_LSHIFT]:
                    tl+=(1/60)
                else:
                    tl=0

                if keys[pygame.K_z]:
                    factor1=0
                if keys[pygame.K_r]:
                    factor1=1
                if keys[pygame.K_f]:
                    factor1=2
                if keys[pygame.K_v]:
                    factor1=3
                if keys[pygame.K_b]:
                    factor1=4
                if factor1==0:
                    U_l=False
                    D_l=False
                if factor1==1:
                    U_l=True
                    D_l=False
                    
                if factor1==2:
                    U_l=False
                    D_l=True
                    
                if factor1==3:
                    U_l=True
                    D_l=False
                    tl+=(1/60)
                if factor1==4:
                    U_l=False
                    D_l=True
                    tl+=(1/60)
            
           
            left_paddle.HANDLE_LEFT_MOVE(keys,tl,U_l,D_l)
            right_paddle.HANDLE_RIGHT_MOVE(keys,tr,U_r,D_r)
            right_paddle_v=right_paddle.HANDLE_RIGHT_MOVE(keys,tr,U_r,D_r)
            left_paddle_v=left_paddle.HANDLE_LEFT_MOVE(keys,tl,U_l,D_l)
            r=right_paddle_v
            l=left_paddle_v
            won=False
            if left_score>=WINNING_SCORE:
                win_text="left player win"
                won=True
            if right_score>=WINNING_SCORE:
                win_text="right player win"
                won=True
            if won==True:
                game.draw(WIN,[left_paddle,right_paddle],ball,color,left_score,right_score)
                text=SCORE_FONT.render(f"{win_text}",1,WHITE)
                WIN.blit(text,(WIDTH//2-text.get_width()//2,HEIGHT//2-text.get_height()//2))
                pygame.display.update()
                pygame.time.delay(5000)
                run=False
                if random.random()>0.5:

                    ball.reset(True)
                else:
                    ball.reset(False)
                left_paddle.reset()
                right_paddle.reset()
                left_score=0
                right_score=0
            if keys[pygame.K_q]:
                if random.random()>0.5:

                    ball.reset(True)
                else:
                    ball.reset(False)

        print(level)       # ball.reset_hit_count()
        level+=1


    ############################################################

# def test_ai(config):
#     WIDTH,HEIGHT=800,580
#     BALL_RADIUS=7
#     #WINNING_SCORE=3
#     FPS=60
#     WHITE=(255,255,255)
#     BLACK=(0,0,0)
#     RED=(255,0,0)
#     PADDLE_WIDTH,PADDLE_HEIGHT=20,100
#     SCORE_FONT=pygame.font.SysFont("comicsans",50)
#     WIN=pygame.display.set_mode((WIDTH,HEIGHT))
#     pygame.display.set_caption("alice pong")
#     hit=0
#     left_hit=0
#     right_hit=0
#     ball=game.Ball(WIDTH//2,HEIGHT//2,BALL_RADIUS,hit,left_hit,right_hit)

#     with open("best_ai1.pickle", "rb") as f:
#       winner1=pickle.load(f)
#     with open("best_ai.pickle2", "rb") as f:
#       winner2=pickle.load(f)
#     run =True
#     left_score=0
#     right_score=0
#     hit=0
#     left_hit=0
#     right_hit=0
#     count_down=3
#     clock=pygame.time.Clock()
#     tl=0
#     tr=0
#     r=0
#     l=0
#     left_paddle=game.Paddle(10,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
#     right_paddle=game.Paddle(WIDTH-10-PADDLE_WIDTH,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
    
    
#     while run:
#         keys=pygame.key.get_pressed()

        
#         clock.tick(FPS)
        
#         game.draw(WIN,[left_paddle,right_paddle],ball,left_score,right_score)
        
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 run=False
#                 break

        
        
#         ball_y_axis,ball_x_axis=ball.move(left_paddle,right_paddle,l,r)
#         count=ball.hit_count(left_paddle,right_paddle)
#         left_count=ball.left_hit_count(left_paddle)
#         right_count=ball.right_hit_count(right_paddle)
#         left_paddle_y_axis=left_paddle.move_info()
#         right_paddle_y_axis=right_paddle.move_info()
        
#         if ball.x-7<20 : #
#             right_score+=1
#             ball.reset(False)
            
#         elif ball.x+7>(WIDTH-20): #
#             left_score+=1
#             ball.reset(True)
            
#         info=game.game_info(left_score,right_score,count,left_paddle_y_axis,right_paddle_y_axis,ball_y_axis,ball_x_axis,PADDLE_WIDTH,WIDTH,left_count,right_count)
#         info_list=info.output()
#         if 560<info_list[5] and info_list[5]<600:
#             re+=1
#         else:
#             re=0
#         if re>=300:
#             if random.random()>0.5:
#                 ball.reset(True)
#             else:
#                 ball.reset(False)
#         #print(info_list)
#         #1
#         net1=neat.nn.FeedForwardNetwork.create(winner1, config)
#         output1=net1.activate((info_list[3],info_list[4],info_list[5],info_list[6],info_list[10]))
#         factor=output1.index(max(output1))
#         if factor==0:
#             U_r=False
#             D_r=False
#         if factor==1:
#             U_r=True
#             D_r=False
#             tl=0
#         if factor==2:
#             U_r=False
#             D_r=True
#             tl=0
#         if factor==3:
#             U_r=True
#             D_r=False
#             tl+=(1/60)
#         if factor==4:
#             U_r=False
#             D_r=True
#             tl+=(1/60)
        

        
#         2
#         net2=neat.nn.FeedForwardNetwork.create(winner2, config)
#         output2=net2.activate((info_list[3],info_list[4],info_list[5],info_list[7],info_list[10]))
#         factor=output2.index(max(output2))
#         if factor==0:
#             U_l=False
#             D_l=False
#         if factor==1:
#             U_l=True
#             D_l=False
#             tr=0 
#         if factor==2:
#             U_l=False
#             D_l=True
#             tr=0
#         if factor==3:
#             U_l=False
#             D_l=True
#             tr+=(1/60)
#         if factor==4:
#             U_l=False
#             D_l=True
#             tr+=(1/60)
        
#         left_paddle.HANDLE_LEFT_MOVE(keys,tl,U_l,D_l)
#         right_paddle.HANDLE_RIGHT_MOVE(keys,tr,U_r,D_r)
#         right_paddle_v=right_paddle.HANDLE_RIGHT_MOVE(keys,tr,U_r,D_r)
#         left_paddle_v=left_paddle.HANDLE_LEFT_MOVE(keys,tl,U_l,D_l)
#         r=right_paddle_v
#         l=left_paddle_v 


#     pygame.quit()
                   
    
# def run_g2(c2):
#     p2= neat.Population(config)
#     p2.add_reporter(neat.StdOutReporter(True))
    
#     p2.add_reporter(neat.StatisticsReporter())
#     p2.add_reporter(neat.Checkpointer(1))
#     p2.run(g2,c2)
   

#     # 2 >> left # 1 >> right
# def run_all():
#     local_dir = os.path.dirname(__file__)
#     config_path = os.path.join(local_dir, "config1.txt")

#     config1 = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                          neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                          config_path)
#     local_dir = os.path.dirname(__file__)
#     config_path = os.path.join(local_dir, "config2.txt")

#     config2 = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                          neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                          config_path)
#     p1= neat.Population(config)
#     p1.add_reporter(neat.StdOutReporter(True))
    
#     p1.add_reporter(neat.StatisticsReporter())
#     p1.add_reporter(neat.Checkpointer(1))
 
#     p1.run(g1,config1)
#     thread=threading.Thread(target=run_g2,args=(config2))
#     thread.start()              


    

def run_neat(config):
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-388')
    #p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    
    p.add_reporter(neat.StatisticsReporter())
    p.add_reporter(neat.Checkpointer(1))

    p.run(eval_genomes, 100)
    # with open("best_ai.pickle", "wb") as f:
    #     pickle.dump(winner,f)




if __name__== "__main__":

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config1.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    #run_neat(config)
    test_genomes(config)
    