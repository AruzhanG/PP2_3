import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed = 20


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - ball_speed, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + ball_speed, HEIGHT - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - ball_speed, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + ball_speed, WIDTH - ball_radius)


    screen.fill(WHITE)

  
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

  
    pygame.time.Clock().tick(30)


pygame.quit()
sys.exit()
