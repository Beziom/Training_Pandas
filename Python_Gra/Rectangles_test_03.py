import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((920,613))

pygame.display.set_caption("Maciej's Game")

clock = pygame.time.Clock()

#Text objects
test_font = pygame.font.Font(None,50)

#Background object
sky_surface = pygame.image.load(r'D:\Repozytorium\Kody_Python\Python_Gra\Sky.png').convert() 
snow_surface = pygame.image.load(r'D:\Repozytorium\Kody_Python\Python_Gra\Snow.png').convert()
text_surface= test_font.render("AC Valhalla - Deluxe Budget Edition",False,"Black")

#Movable objects
viking_surface = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Viking.png").convert_alpha()
viking_x_pos = 600
viking_rect = viking_surface.get_rect(midbottom = (900,518)) # Settinf rectangle for Snail

player_surface = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Eivor.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100,518)) # Seettin up rectangle

# bg_music = pygame.mixer.Sound(r'D:\Repozytorium\Kody_Python\Python_Gra\Szaman.mp3')
# bg_music.play()

while True:
    """Avoiding closing the program"""    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 
    
    screen.blit(sky_surface,(0,0))
    screen.blit(snow_surface,(0,518))
    screen.blit(text_surface,(170,50))
    screen.blit(viking_surface,viking_rect)
    screen.blit(player_surface, player_rect) # Defining rectangle as a dimensions

    viking_rect.right -= 4
    if viking_rect.right <= 0: viking_rect.left = 900

    player_rect.left += 1
    if player_rect.left >= 900: player_rect.left = 100
    pygame.display.update()
    clock.tick(60)