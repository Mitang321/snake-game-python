

import pygame
import sys
import random


pygame.init()


width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)


clock = pygame.time.Clock()


def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (width / 2, 15)
    window.blit(score_surface, score_rect)


def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    window.fill(black)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.sleep(2)
    wait_for_key()


def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                main()


def pause_game():
    paused = True
    my_font = pygame.font.SysFont('times new roman', 50)
    pause_surface = my_font.render('Paused', True, red)
    pause_rect = pause_surface.get_rect()
    pause_rect.midtop = (width / 2, height / 4)
    window.blit(pause_surface, pause_rect)
    pygame.display.flip()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                    return


def main():
    global change_to, snake_direction, food_pos, food_spawn, score

    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    snake_direction = 'RIGHT'
    change_to = snake_direction

    food_pos = [random.randrange(1, (width//10))
                * 10, random.randrange(1, (height//10)) * 10]
    food_spawn = True

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                elif event.key == pygame.K_p:
                    pause_game()

        if change_to == 'UP' and not snake_direction == 'DOWN':
            snake_direction = 'UP'
        if change_to == 'DOWN' and not snake_direction == 'UP':
            snake_direction = 'DOWN'
        if change_to == 'LEFT' and not snake_direction == 'RIGHT':
            snake_direction = 'LEFT'
        if change_to == 'RIGHT' and not snake_direction == 'LEFT':
            snake_direction = 'RIGHT'

        if snake_direction == 'UP':
            snake_pos[1]
