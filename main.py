

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


eat_sound = pygame.mixer.Sound('eat_sound.wav')
game_over_sound = pygame.mixer.Sound('game_over_sound.wav')


clock = pygame.time.Clock()


def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (width / 2, 15)
    window.blit(score_surface, score_rect)


def display_message(message, size, color, y_offset):
    font = pygame.font.SysFont('times new roman', size)
    message_surface = font.render(message, True, color)
    message_rect = message_surface.get_rect()
    message_rect.midtop = (width / 2, height / 2 + y_offset)
    window.blit(message_surface, message_rect)


def welcome_screen():
    window.fill(black)
    display_message('Welcome to Snake Game!', 50, white, -50)
    display_message('Press ENTER to Start', 30, white, 50)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return


def game_over():
    game_over_sound.play()
    window.fill(black)
    display_message('Your Score is : ' + str(score), 50, red, -50)
    display_message('Press ENTER to Restart', 30, white, 50)
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
                if event.key == pygame.K_RETURN:
                    main()


def pause_game():
    paused = True
    window.fill(black)
    display_message('Paused', 50, red, 0)
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
            snake_pos[1] -= 10
        if snake_direction == 'DOWN':
            snake_pos[1] += 10
        if snake_direction == 'LEFT':
            snake_pos[0] -= 10
        if snake_direction == 'RIGHT':
            snake_pos[0] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            food_spawn = False
            score += 10
            eat_sound.play()  # Play sound effect for eating food
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(
                1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        food_spawn = True

        window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(window, green, pygame.Rect(
                pos[0], pos[1], 10, 10))

        pygame.draw.rect(window, red, pygame.Rect(
            food_pos[0], food_pos[1], 10, 10))

        for block in snake_body[1:]:
            if snake_pos == block:
                game_over()

        if snake_pos[0] < 0 or snake_pos[0] > width-10 or snake_pos[1] < 0 or snake_pos[1] > height-10:
            game_over()

        show_score(white, 'times new roman', 20)

        pygame.display.update()

        clock.tick(30)


if __name__ == '__main__':
    welcome_screen()
    main()
