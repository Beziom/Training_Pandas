import pygame
from sys import exit

#init
pygame.init()
screen = pygame.display.set_mode((920,613))
pygame.display.set_caption("Maciej's Game")
clock = pygame.time.Clock()

#Text objects
test_font = pygame.font.Font(None,50)

#Background object
sky_surface = pygame.image.load(r'D:\Repozytorium\Kody_Python\Python_Gra\Sky.png').convert() 
snow_surface = pygame.image.load(r'D:\Repozytorium\Kody_Python\Python_Gra\Snow.png').convert()

#Text objects
text_surface= test_font.render("AC Valhalla - Deluxe Budget Edition",False,"Black")
text_rect = text_surface.get_rect(center = (460,50))
score_surface= test_font.render("Score",False,(64,64,64)) 
score_rect = score_surface.get_rect(center = (460,100))

#Movable objects
viking_surface = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Viking.png").convert_alpha()
viking_rect = viking_surface.get_rect(midbottom = (900,518))

player_surface = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Eivor.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100,518))

#Animation variables
player_gravity = 0 

#Game Loop
while True:
    """Loop for the whole game"""    
    for event in pygame.event.get():

        #Game close
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 

        #Mouse jump
        if event.type == pygame.MOUSEBUTTONDOWN: #Mouse Motion poruszanie się Mouse button down to jż klikanie
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 518: # and player_rect.bottom >= 518 - jump if touches the floor
                    player_gravity = -20
                    
        #Keyboard - jump
        if event.type == pygame.KEYDOWN and player_rect.bottom >= 518:
            if event.key == pygame.K_SPACE: 
                player_gravity = -20
    
    #Diplaying objects (other than players)
    screen.blit(sky_surface,(0,0))
    screen.blit(snow_surface,(0,518))
    screen.blit(text_surface, text_rect)
    pygame.draw.rect(screen,"#c0e8ec", score_rect)
    pygame.draw.rect(screen,"#c0e8ec", score_rect,10)
    screen.blit(score_surface, score_rect)
    screen.blit(viking_surface,viking_rect)

    #Viking Animation
    viking_rect.right -= 4
    if viking_rect.right <= 0: viking_rect.left = 900

    # Gravity before drawing player
    player_gravity += 1 #every fram player gravity is increasing by one
    player_rect.y += player_gravity
    if player_rect.bottom >= 518: #creating floor 
        player_rect.bottom = 518
    screen.blit(player_surface, player_rect)
    
    #Coollision
    mouse_pos = pygame.mouse.get_pos() 
    if player_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())
    
    #Game settings
    pygame.display.update()
    clock.tick(60)

# bg_music = pygame.mixer.Sound(r'D:\Repozytorium\Kody_Python\Python_Gra\Szaman.mp3')
# bg_music.play()