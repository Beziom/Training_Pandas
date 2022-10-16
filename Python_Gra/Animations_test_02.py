import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((920,613))

pygame.display.set_caption("Maciej's Game")

clock = pygame.time.Clock()

#Text objects
test_font = pygame.font.Font(None,50)

#Background object
sky_surface = pygame.image.load(r'D:\Repozytorium\Kody_Python\Python_Gra\Sky.png').convert() #convert for faster animatin
snow_surface = pygame.image.load(r'D:\Repozytorium\Kody_Python\Python_Gra\Snow.png').convert()
text_surface= test_font.render("AC Valhalla - Deluxe Budget Edition",False,"Black")

#Movable objects
viking_surface = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Viking.png").convert_alpha()
viking_x_pos = 600

while True:
    """Avoiding closing the program"""    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 
    
    screen.blit(sky_surface,(0,0))
    screen.blit(snow_surface,(0,518))
    screen.blit(text_surface,(170,50))

    viking_x_pos -= 4 #Animation that viking is moving
    if viking_x_pos < -72: viking_x_pos = 900 # repating animation
    screen.blit(viking_surface,(viking_x_pos,482))

    pygame.display.update()
    clock.tick(60)