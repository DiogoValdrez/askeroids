import pygame
import time
import random
pygame.init()
white=(225,225,225)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
width=600
height=400
scr=pygame.display.set_mode([width,height])
pygame.display.set_caption("Snake")
clock=pygame.time.Clock()
snake_block=10
snake_speed=15
font_style=pygame.font.SysFont("bahnschrift",25)
def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(scr,black,[x[0],x[1],snake_block,snake_block])
def message(msg,color):
    mesg=font_style.render(msg,True,color)
    scr.blit(mesg,[width/6,height/2.5])
def gameLoop():
    game_over=False
    game_close=False
    x1=width/2
    y1=height/2
    x1_change=0
    y1_change=0
    snake_list=[]
    Lenght_of_snake=1
    foodx=round(random.randrange(0,width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,height-snake_block)/10.0)*10.0
    while not game_over:
        while game_close==True:
            scr.fill(blue)
            message("You lost!Press E-Exit or P-Play Again",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_e:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_p:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-snake_block
                elif event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=snake_block
            if event.type==pygame.QUIT:
                game_over=True    
        if x1>=width or x1<0 or y1>=height or y1<0:
            game_close=True
        x1+=x1_change
        y1+=y1_change
        scr.fill(blue)
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list)>Lenght_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_head:
                game_close=True
        our_snake(snake_block,snake_list) 
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,width-snake_block)/10.0)*10.0
            foody=round(random.randrange(0,height-snake_block)/10.0)*10.0
            Lenght_of_snake+=1
        pygame.draw.rect(scr,green,(foodx,foody,snake_block,snake_block))
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()
gameLoop()