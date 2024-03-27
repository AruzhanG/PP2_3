'''import pygame


pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Pygame Lab Project")

icon = pygame.image.load('diamond_icon.png')
pygame.display.set_icon(icon)
running = True

while running:
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
'''
import pygame
import sys
from pygame.locals import *
import math
import time


pygame.init()


WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")


mickey_image = pygame.image.load('mickeyclock.jpeg')
mickey_image = pygame.transform.scale(mickey_image, (400, 400))


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def draw_clock():
  
    window.fill((255, 255, 255))
    
   
    window.blit(mickey_image, (100, 100))
    
 
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min


    seconds_angle = math.radians(seconds * 6 - 90)
    seconds_x = 300 + 150 * math.cos(seconds_angle)
    seconds_y = 300 + 150 * math.sin(seconds_angle)
    pygame.draw.line(window, (255, 0, 0), (300, 300), (seconds_x, seconds_y), 2)


    minutes_angle = math.radians(minutes * 6 - 90)
    minutes_x = 300 + 150 * math.cos(minutes_angle)
    minutes_y = 300 + 150 * math.sin(minutes_angle)
    pygame.draw.line(window, (0, 0, 255), (300, 300), (minutes_x, minutes_y), 4)

    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    draw_clock()

   
    clock.tick(30)
