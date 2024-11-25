import pygame
import random

# Start the game
pygame.init()

size = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Breaker")
floor = pygame.Rect(250, 550, 100, 10)
ball = pygame.Rect(350, 250, 10, 10)
score = 0
lives = 3
move = [1, 1] 
continueGame = True

GREEN = (28, 252, 106)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (252, 3, 152)
ORANGE = (252, 170, 28)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

bricks = []
colors = [ORANGE, YELLOW]
for row in range(5):
    for col in range(8):
        brick_color = random.choice(colors)
        bricks.append((pygame.Rect(1 + col * 100, 60 + row * 40, 98, 38), brick_color))

def draw_bricks(bricks):
    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)

while continueGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueGame = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, floor)
    font = pygame.font.Font(None, 34)
    text = font.render("CURRENT SCORE: " + str(score), 1, WHITE)
    screen.blit(text, (180, 10))
    text_lives = font.render("LIVES: " + str(lives), 1, WHITE)
    screen.blit(text_lives, (480, 10))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and floor.x < 500:
        floor.x += 3
    if keys[pygame.K_LEFT] and floor.x > 0:
        floor.x -= 3

    ball.x += move[0]
    ball.y += move[1]

    if ball.x > 590 or ball.x < 0:
        move[0] = -move[0]
    if ball.y <= 3:
        move[1] = -move[1]
    if floor.collidepoint(ball.x, ball.y):
        move[1] = -move[1]

    if ball.y >= 590:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over!", 1, RED)
        screen.blit(text, (150, 300))
        font = pygame.font.Font(None, 50)
        text = font.render("YOUR FINAL SCORE: " + str(score), 1, GREEN)
        screen.blit(text, (100, 350))
        pygame.display.flip()
        pygame.time.wait(5000)
        break

    pygame.draw.rect(screen, WHITE, ball)

    for brick, color in bricks:
        if brick.collidepoint(ball.x, ball.y):
            bricks.remove((brick, color))
            move[1] = -move[1]
            score += 1

    if score == len(bricks): 
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON", 1, GREEN)
        screen.blit(text, (150, 350))
        pygame.display.flip()
        pygame.time.wait(3000)
        break

    draw_bricks(bricks)
    pygame.time.wait(1)
    pygame.display.flip()

# End the game
pygame.quit()