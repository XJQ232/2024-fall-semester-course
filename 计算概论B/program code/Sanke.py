import pygame
import time
import random

# 初始化 Pygame
pygame.init()

# 使用系统中支持中文的字体
font_path = "C:/Windows/Fonts/msyh.ttc"  # 微软雅黑字体路径
font_style = pygame.font.Font(font_path, 25)
score_font = pygame.font.Font(font_path, 35)

# 定义一些颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 屏幕宽度和高度
dis_width = 600
dis_height = 400

# 创建窗口
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('贪吃蛇游戏')

# 定义时钟
clock = pygame.time.Clock()

# 定义蛇的大小和速度
snake_block = 10
snake_speed = 15


# 显示得分
def your_score(score):
    value = score_font.render("你的得分: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# 蛇的绘制
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# 显示消息
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


# 游戏主循环
def gameLoop():
    game_over = False
    game_close = False

    # 蛇的初始位置
    x1 = dis_width / 2
    y1 = dis_height / 2

    # 蛇的移动
    x1_change = 0
    y1_change = 0

    # 蛇的身体
    snake_list = []
    length_of_snake = 1

    # 食物的位置
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("你输了! 按Q退出游戏或按C重新开始", red)  # 使用支持中文的字体显示消息
            your_score(length_of_snake - 1)
            pygame.display.update()

            # 检查玩家是否想重新开始或退出
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # 处理按键事件
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

        # 检查蛇是否撞墙
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # 绘制食物
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # 更新蛇的位置
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # 检查蛇是否撞到自己
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # 绘制蛇
        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # 检查是否吃到食物
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # 控制游戏速度
        clock.tick(snake_speed)

    pygame.quit()
    quit()


# 启动游戏
gameLoop()
