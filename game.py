import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
brown = (139, 69, 19)
orange = (255, 165, 0)
beige = (245, 245, 220)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25) #размер шрифта
score_font = pygame.font.SysFont("comicsansms", 35) #шрифт счета


def our_snake(snake_block, snake_list):
   for x in snake_list:
       pygame.draw.ellipse(dis, black, [x[0], x[1], snake_block, snake_block])

"""Функция вывода сообщения"""
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

"""Функция перемещения"""
def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1 
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # еда по оси X
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 # еда по оси Y


    while not game_over:
        while game_close == True:
            dis.fill(beige)
            message("Потрачено! Нажмите ESC для выхода или Space для повторной игры", brown)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(beige)

        pygame.draw.rect(dis, orange, [food_x, food_y, snake_block, snake_block])
        snake_head = [] # список c показателем длины змеи при движениях
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0] # чтобы не увеличив при движении
        for x in snake_list[:-1]:
            if x == snake_head:
               game_close = True
        our_snake(snake_block, snake_list)
        pygame.display.update()
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
 
gameLoop()