
import pygame
import random
pygame.init()



WIDTH,HEIGHT=800,580#700,500
BALL_RADIUS=7
WINNING_SCORE=3
FPS=60
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,255,0)


PADDLE_WIDTH,PADDLE_HEIGHT=20,100

SCORE_FONT=pygame.font.SysFont("comicsans",50)
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("alice pong")



class game_info:
    def __init__(self,left_score,right_score,hit_count,left_paddle_y_axis,right_paddle_y_axis,ball_y_axis,ball_x_axis,PADDLE_WIDTH,WIDTH,left_hit,right_hit):
        self.left_score=left_score
        self.right_score=right_score
        self.hit_count=hit_count
        self.left_paddle_y_axis=left_paddle_y_axis
        self.right_paddle_y_axis=(right_paddle_y_axis)
        self.ball_y_axis=(ball_y_axis)
        self.ball_x_axis=(ball_x_axis)
        self.l_abs_dis=(pow((abs(pow((ball_x_axis-PADDLE_WIDTH),2))+abs(pow((left_paddle_y_axis-ball_y_axis),2))),0.5))
        self.r_abs_dis=(pow((abs(pow((WIDTH-ball_x_axis-PADDLE_WIDTH),2))+abs(pow((right_paddle_y_axis-ball_y_axis),2))),0.5))
        self.left_hit=(left_hit)
        self.right_hit=(right_hit)
    def output(self):
        return [
        self.left_score,
        self.right_score,
        self.hit_count,
        self.left_paddle_y_axis,#
        self.right_paddle_y_axis,#
        self.ball_y_axis,#
        self.l_abs_dis,
        self.r_abs_dis,#
        self.left_hit,
        self.right_hit,
        self.ball_x_axis#
        ]

class Paddle:

    COLOR=WHITE
    VELOCITY=6#4
    ACCELERATE=10

    
    def __init__(self,x,y,width,height):
        self.x=self.ori_x=x
        self.y=self.ori_y=y
        self.width=width
        self.height=height

    def draw(self,win):
        pygame.draw.rect(win,self.COLOR,(self.x,self.y,self.width,self.height))

    def move_info(self):
        return self.y
    def reset(self):
        self.x=self.ori_x
        self.y=self.ori_y
     

    def HANDLE_LEFT_MOVE(self,keys,t,U_l,D_l):
        self.VELOCITY=6
        self.VELOCITY+=self.ACCELERATE*t

        if self.VELOCITY>=20:
                self.VELOCITY=20
        if keys[pygame.K_w] and self.y-self.VELOCITY>=0 or U_l==True and self.y-self.VELOCITY>=0:
                self.y-=self.VELOCITY
                return (-1*self.VELOCITY )
        elif keys[pygame.K_w] and self.y-self.VELOCITY<0  or U_l==True and self.y-self.VELOCITY<0:
                return (-1*self.VELOCITY )

       
        if keys[pygame.K_s] and self.y+PADDLE_HEIGHT+self.VELOCITY<=HEIGHT or D_l==True and self.y+PADDLE_HEIGHT+self.VELOCITY<=HEIGHT :
                self.y+=self.VELOCITY 
                return self.VELOCITY 
        elif keys[pygame.K_s] and self.y+PADDLE_HEIGHT+self.VELOCITY>HEIGHT or D_l==True and self.y+PADDLE_HEIGHT+self.VELOCITY>HEIGHT:
                return self.VELOCITY 
        if keys[pygame.K_w]==False and keys[pygame.K_s]==False or U_l==False and D_l==False:
                self.VELOCITY=0
                return self.VELOCITY    
        
    def HANDLE_RIGHT_MOVE(self,keys,t,U_r,D_r):
        self.VELOCITY=6
        self.VELOCITY+=self.ACCELERATE*t

        if self.VELOCITY>=20:
                self.VELOCITY=20
        if keys[pygame.K_UP] and self.y-self.VELOCITY>=0 or U_r==True and self.y-self.VELOCITY>=0:
                self.y-=self.VELOCITY
                return (-1*self.VELOCITY )
        elif keys[pygame.K_UP] and self.y-self.VELOCITY<0  or U_r==True and self.y-self.VELOCITY<0:
                return (-1*self.VELOCITY )

       
        if keys[pygame.K_DOWN] and self.y+PADDLE_HEIGHT+self.VELOCITY<=HEIGHT or D_r==True and self.y+PADDLE_HEIGHT+self.VELOCITY<=HEIGHT :
                self.y+=self.VELOCITY 
                return self.VELOCITY 
        elif keys[pygame.K_DOWN] and self.y+PADDLE_HEIGHT+self.VELOCITY>HEIGHT or D_r==True and self.y+PADDLE_HEIGHT+self.VELOCITY>HEIGHT:
                return self.VELOCITY 
        if keys[pygame.K_UP]==False and keys[pygame.K_DOWN]==False or U_r==False and D_r==False:
                self.VELOCITY=0
                return self.VELOCITY     
         


class Ball:

    MAX_VEL=10
    COLOR=WHITE
    
    def __init__(self,x,y,radius,hit,left_hit,right_hit):
        self.x=self.ori_x=x
        self.y=self.ori_y=y
        self.radius=radius
        self.hit=self.ori_hit=hit
        self.left_hit=self.ori_left_hit=left_hit
        self.right_hit=self.ori_right_hit=right_hit
        if random.random()>0.5:
            a=+1
        else:
            a=-1
        if random.random()>0.5:      
            b=+1
        else:
            b=-1
        self.x_vel =-1*a*self.MAX_VEL
        self.y_vel=self.MAX_VEL*(b*(random.random()))*0.5
    def draw(self,win,color):
        
        pygame.draw.circle(win,color,(self.x,self.y),self.radius)
        hit_text=SCORE_FONT.render(f"{self.hit}",1,RED)
        win.blit(hit_text,(WIDTH//2-hit_text.get_width()//2,20))

    def move(self,left_paddle,right_paddle,left_paddle_v,right_paddle_v):
        k=1
        if self.y+self.radius>=right_paddle.y and self.x>right_paddle.x or self.y-self.radius<=right_paddle.y+right_paddle.height and self.x>right_paddle.x:
            self.y_vel*=-1
        if self.y-self.radius<=0:
            self.y_vel*=-1
        if self.y+self.radius>=HEIGHT:
            self.y_vel*=-1
        if self.x+self.radius>=right_paddle.x and  self.y<=right_paddle.y+right_paddle.height and self.y>=right_paddle.y:
            # self.x_vel*=-1
            # mid_dis=right_paddle.y+right_paddle.height//2-self.y
            # ratio=(right_paddle.height//2)/self.MAX_VEL
            # vel=mid_dis/ratio
            # self.y_vel=-1*vel
            self.y_vel+=(k*right_paddle_v)
            self.x_vel*=-1
        if self.y+self.radius>=left_paddle.y and self.x<left_paddle.x or self.y-self.radius<=left_paddle.y+left_paddle.height and self.x<left_paddle.x:
            self.y_vel*=-1
        if self.x-self.radius<=left_paddle.x +left_paddle.width and  self.y<=left_paddle.y+left_paddle.height and self.y>=left_paddle.y:
            # self.x_vel*=-1
            # mid_dis=left_paddle.y+left_paddle.height//2-self.y
            # ratio=(left_paddle.height//2)/self.MAX_VEL
            # vel=mid_dis/ratio
            # self.y_vel=-1*vel
            self.y_vel+=(k*left_paddle_v)
            self.x_vel*=-1
        if self.y_vel>=20:
            self.y_vel=20
        self.x+=self.x_vel 
        self.y+=self.y_vel
        return self.y,self.x,pow(self.x_vel,2)+pow(self.y_vel,2)
    def reset(self,left):
        
        if random.random()>0.5:
            a=+1
        else:
            a=-1
        
        if left==True:
            self.x=(3/2)*self.ori_x
        else:
            self.x=(1/2)*self.ori_x
        self.y=self.ori_y
        self.x_vel =-1*self.x_vel
        self.y_vel=-1*self.x_vel*(a*(random.random()))*0.5
        self.hit=self.ori_hit
        self.left_hit=self.ori_left_hit
        self.right_hit=self.ori_right_hit

    def reset_hit_count(self):
        self.hit=self.ori_hit

    def hit_count(self,left_paddle,right_paddle):
        if self.x+self.radius>=right_paddle.x and  self.y<=right_paddle.y+right_paddle.height and self.y>=right_paddle.y:
            self.hit+=1
        elif self.x-self.radius<=left_paddle.x +left_paddle.width and  self.y<=left_paddle.y+left_paddle.height and self.y>=left_paddle.y:
            self.hit+=1
        return self.hit
    def left_hit_count(self,left_paddle):
        if self.x-self.radius<=left_paddle.x +left_paddle.width and  self.y<=left_paddle.y+left_paddle.height and self.y>=left_paddle.y:
            self.left_hit+=1
        return self.left_hit
    def right_hit_count(self,right_paddle):
        if self.x+self.radius>=right_paddle.x and  self.y<=right_paddle.y+right_paddle.height and self.y>=right_paddle.y:
            self.right_hit+=1
        return self.right_hit  



def draw(win,paddles,ball,color,left_score,right_score):

    win.fill(BLACK)
    leftscore_text=SCORE_FONT.render(f"{left_score}",1,WHITE)
    rightscore_text=SCORE_FONT.render(f"{right_score}",1,WHITE)
    win.blit(leftscore_text,(WIDTH//4-leftscore_text.get_width()//2,20))
    win.blit(rightscore_text,(WIDTH*(3/4)-rightscore_text.get_width()//2,20))
    for paddle in paddles:
        paddle.draw(win)
    for i in range(10,WIDTH,HEIGHT//20):
        if i %4==1:
            continue
        pygame.draw.rect(win,WHITE,(WIDTH//2-5,i,10,HEIGHT//20))
    ball.draw(win,color)
    
    pygame.display.update()




def main():
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
    re1=0
    
    left_paddle=Paddle(10,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
    right_paddle=Paddle(WIDTH-10-PADDLE_WIDTH,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
    ball=Ball(WIDTH//2,HEIGHT//2,BALL_RADIUS,hit,left_hit,right_hit)
    ball_v=0
    while run:
        keys=pygame.key.get_pressed()
        keys[pygame.K_w]==True
        if keys[pygame.K_LSHIFT]:
            tl+=(1/60)
        else:
            tl=0
        if keys[pygame.K_RETURN]:
            tr+=(1/60)
        else:
            tr=0
        

        clock.tick(60)
       
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        U_l=0
        D_l=0
        U_r=0
        D_r=0


        left_paddle.HANDLE_LEFT_MOVE(keys,tl,U_l,D_l)
        right_paddle.HANDLE_RIGHT_MOVE(keys,tr,U_r,D_r)
        right_paddle_v=right_paddle.HANDLE_RIGHT_MOVE(keys,tr,U_r,D_r)
        left_paddle_v=left_paddle.HANDLE_LEFT_MOVE(keys,tl,U_l,D_l)
       
        
        ball_y_axis,ball_x_axis,ball_v=ball.move(left_paddle,right_paddle,left_paddle_v,right_paddle_v)
        count=ball.hit_count(left_paddle,right_paddle)
        left_count=ball.left_hit_count(left_paddle)
        right_count=ball.right_hit_count(right_paddle)
        left_paddle_y_axis=left_paddle.move_info()
        right_paddle_y_axis=right_paddle.move_info()
        if ball_v>900:
            color=RED
        else:
            color=WHITE
        draw(WIN,[left_paddle,right_paddle],ball,color,left_score,right_score)
        if ball.x<0 :
            right_score+=1
            draw(WIN,[left_paddle,right_paddle],ball,left_score,right_score)
            count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
            WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
            pygame.display.update()
            pygame.time.delay(1000)
            count_down+=-1
            draw(WIN,[left_paddle,right_paddle],ball,left_score,right_score)
            count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
            WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
            pygame.display.update()
            pygame.time.delay(1000)
            count_down+=-1
            draw(WIN,[left_paddle,right_paddle],ball,left_score,right_score)
            count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
            WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
            pygame.display.update()
            pygame.time.delay(1000)
            count_down=3
            ball.reset(False)
            
        elif ball.x>WIDTH:
            left_score+=1
            draw(WIN,[left_paddle,right_paddle],ball,left_score,right_score)
            count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
            WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
            pygame.display.update()
            pygame.time.delay(1000)
            count_down+=-1
            draw(WIN,[left_paddle,right_paddle],ball,left_score,right_score)
            count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
            WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
            pygame.display.update()
            pygame.time.delay(1000)
            count_down+=-1
            draw(WIN,[left_paddle,right_paddle],ball,left_score,right_score)
            count_down_=SCORE_FONT.render(f"{count_down}",1,RED)
            WIN.blit(count_down_,(WIDTH//2-count_down_.get_width()//2,HEIGHT//2-count_down_.get_height()//2))
            pygame.display.update()
            pygame.time.delay(1000)
            count_down=3

            ball.reset(True)
            
        info=game_info(left_score,right_score,count,left_paddle_y_axis,right_paddle_y_axis,ball_y_axis,ball_x_axis,PADDLE_WIDTH,WIDTH,left_count,right_count)
        info_list=info.output()
        if right_paddle_v==0 and left_paddle_v==0:
            re1+=1
        else:
            re1=0
        
        if re1>=300:
            if random.random()>0.5:
                re1=0
                ball.reset(True)
            else:
                rel=0
                ball.reset(False)
        
       
        
        # [                             
        # self.left_score,              0
        # self.right_score,             1
        # self.hit_count,               2         
        # self.left_paddle_y_axis,      3
        # self.right_paddle_y_axis,     4
        # self.ball_y_axis,             5
        # self.l_abs_dis,               6
        # self.r_abs_dis                7
        # self.left_hit,          8
        # self.right_hit,         9
        # self.ball_x_axis
        # ]
       
        won=False
        if left_score>=WINNING_SCORE:
            win_text="left player win"
            won=True
        if right_score>=WINNING_SCORE:
            win_text="right player win"
            won=True
        if won==True:
            text=SCORE_FONT.render(f"{win_text}",1,WHITE)
            WIN.blit(text,(WIDTH//2-text.get_width()//2,HEIGHT//2-text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score=0
            right_score=0
            ball.reset_hit_count()
            
           

        

            
    pygame.quit()
if __name__== "__main__":
    main()
  