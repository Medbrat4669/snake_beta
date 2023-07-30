import pygame
import time
import random

pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption('Snake')


game_over = False
x1 = dis_width/2
y1 = dis_height/2
snake_block = 10
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()
snake_speed = 15
font_style = pygame.font.SysFont(None, 50) #размер шрифта

"""Функция вывода сообщения"""
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

"""Функция перемещения"""
def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # еда по оси X
    food_y = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # еда по оси Y


    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
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
        dis.fill(white)

        pygame.draw.rect(dis, blue, [food_x, food_y, snake_block, snake_block])
        pygame.draw.ellipse(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()


    pygame.quit()

    quit()
gameLoop()