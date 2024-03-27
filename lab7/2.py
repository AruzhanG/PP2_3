import pygame
import os

pygame.init()

window_width = 800
window_height = 600
game_display = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

current_song_index = 0
songs = [ '3D.mp3']
pygame.mixer.music.load(os.path.normpath(songs[current_song_index]))
pygame.mixer.music.play()

play = True
x = 0
font = pygame.font.SysFont('Arial', 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        play = not play
        if play:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
    
    if pressed[pygame.K_LEFT]: 
        current_song_index = (current_song_index - 1) % len(songs)
        pygame.mixer.music.load(songs[current_song_index])
        pygame.mixer.music.play()
        play = True
        x = 0
        
            
    if pressed[pygame.K_RIGHT]: 
        current_song_index = (current_song_index + 1) % len(songs)
        pygame.mixer.music.load(songs[current_song_index])
        pygame.mixer.music.play()
        play = True
        x = 0
        
        

    game_display.fill((255, 255, 255))    
    text = font.render(songs[current_song_index][:-4], True, (0, 0, 0))  
    game_display.blit(text, (400 - text.get_width() // 2, 370))  
    
    pygame.draw.rect(game_display, (225, 225, 225), (290, 342, 275, 11))
    if play:
        x += 0.1
        if x > 275:
            x = 0
    pygame.draw.rect(game_display, (100, 150, 200), (290, 342, x, 11))
    
    
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()

