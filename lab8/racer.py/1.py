import pygame
import sys
from pygame.locals import *
import random
import time
from random import randint 

pygame.init()

#displays default settings and colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DOLL=0
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
DOLL=0


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        size = (30, 30)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


    
    def move(self):
        global DOLL
        self.rect.move_ip(0,5)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    

    def coll(self):
        self.rect.move_ip(0,5)
        self.rect.top = 0
        self.rect.center = (500, 700)
    


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (160, 520))
    

        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(7, 0)
    
                   
#initializing the sprites       
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
#sprites group
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
coins = pygame.sprite.Group()
coins.add(C1)
 
#new user event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#the main game Loop
while True:
       
    #cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(background , WHITE,(9, 10, 50, 45),) 
    pygame.draw.rect(background , WHITE,(345, 10, 50, 45),)  

    
    #fonts
    f2 = pygame.font.SysFont(None, 25)
    text2 = f2.render('score', False, BLACK)
    background.blit(text2, (10, 10))

    f1 = pygame.font.SysFont(None, 25)
    text2 = f2.render('coins', False, BLACK)
    background.blit(text2, (347, 10))

#display
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (23,22))
    scores1 = font_small.render(str(DOLL), True, BLACK)
    DISPLAYSURF.blit(scores1, (360,22))
 
    #moving everything
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(P1, coins):
        DOLL+=1
        C1.coll()
 
    #collision between a player and an enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()
    

             
    pygame.display.update()
    pygame.time.Clock().tick(60)