import pygame
from random import randrange

(width, height) = (1000, 800)
sizeOfSquare = 40
(gameWidth, gameHeight) = (width//sizeOfSquare, height//sizeOfSquare)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()


snake = [[gameHeight//2, gameWidth//2]]
dir = 0 # 0: North. 1: East, 2: South, 3: West
apple = [randrange(gameHeight), randrange(gameWidth)]
running = True

def gameOver(row, col):
    if row < 0 or row >= gameHeight or col < 0 or col >= gameWidth or snake.count([row, col]) > 1:
        return True
    return False

delay = 750000
count = 0
while running:
    if count != delay:
        count += 1
        continue
    count = 0

    print(snake[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dir = 0
            elif event.key == pygame.K_d:
                dir = 1
            elif event.key == pygame.K_s:
                dir = 2
            elif event.key == pygame.K_a:
                dir = 3

    if dir == 0:
        snake.insert(0, [snake[0][0] - 1, snake[0][1]])
    elif dir == 1:
        snake.insert(0, [snake[0][0], snake[0][1] + 1])
    elif dir == 2:
        snake.insert(0, [snake[0][0] + 1, snake[0][1]])
    elif dir == 3:
        snake.insert(0, [snake[0][0], snake[0][1] - 1])

    if gameOver(snake[0][0], snake[0][1]):
        running = False

    if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
        apple = [randrange(gameHeight), randrange(gameWidth)]
    else:
        snake.pop()

    screen.fill((0, 0, 0))
    for snakePart in snake:
        pygame.draw.rect(screen, (0, 255, 0),(snakePart[1] * sizeOfSquare, snakePart[0] * sizeOfSquare, sizeOfSquare, sizeOfSquare))

    pygame.draw.rect(screen, (255, 0, 0),(apple[1] * sizeOfSquare, apple[0] * sizeOfSquare, sizeOfSquare, sizeOfSquare))
    pygame.display.update()
