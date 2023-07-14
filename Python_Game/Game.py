import pygame
import random

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

# defining colors
White = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# defining global variables
points = 0


def green_balls(i, j):
    """generates green balls by using pygame built-in draw function whenever called"""
    pygame.draw.circle(gameDisplay, green, [i, j], 10)


def red_balls(i, j):
    """generates red balls by using pygame built-in draw function whenever called"""
    pygame.draw.circle(gameDisplay, red, [i, j], 10)


def cart(x):
    """generates a rectangle as our cart as a box we control using pygame built-in draw function"""
    pygame.draw.rect(gameDisplay, White, [x, 500, 100, 100])


def GameLoop():
    """This is the main game loop"""
    over = False
    x = 350
    x_change = 0
    global points

    green_balls_list = []
    for i in range(10):
        i = random.randint(10, 790)
        ball_speed = random.randint(1, 10)
        green_balls_list.append([i, 0, ball_speed])

    red_balls_list = []
    for i in range(3):
        i = random.randint(10, 790)
        ball_speed = random.randint(1, 10)
        red_balls_list.append([i, 0, ball_speed])

    while not over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = +10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(black)

        for i in green_balls_list:
            i[1] += i[2]
            green_balls(i[0], i[1])

            if i[1] > 590:
                i[1] = 0
                i[0] = random.randint(10, 790)

            if i[1] == 500 and (x < i[0] < x + 100):
                points += 1

        for i in red_balls_list:
            i[1] += i[2]
            red_balls(i[0], i[1])

            if i[1] > 590:
                i[1] = 0
                i[0] = random.randint(10, 790)

            if i[1] == 500 and (x < i[0] < x + 100):
                over = True

        cart(x)
        pygame.display.update()

        clock.tick(60)


GameLoop()
print(points)
pygame.quit()
quit()
