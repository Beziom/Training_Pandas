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
viking_x_pos = 600
viking_rect = viking_surface.get_rect(midbottom = (900,518))
player_surface = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Eivor.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100,518))

# bg_music = pygame.mixer.Sound(r'D:\Repozytorium\Kody_Python\Python_Gra\Szaman.mp3')
# bg_music.play()

#Game Loop
while True:
    """Loop for the whole game"""    
    for event in pygame.event.get():

        #Game close
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 

        #Keyboard
        if event.type == pygame.KEYDOWN: # when key is pressed then another event is done
            if event.key == pygame.K_SPACE: # Wehn space then Jump
                print("Jump")
        if event.type == pygame.KEYUP :
                print("Key Up")
    
    #Diplaying objects
    screen.blit(sky_surface,(0,0))
    screen.blit(snow_surface,(0,518))
    screen.blit(text_surface, text_rect)
    pygame.draw.rect(screen,"#c0e8ec", score_rect)
    pygame.draw.rect(screen,"#c0e8ec", score_rect,10)
    screen.blit(score_surface, score_rect)
    screen.blit(viking_surface,viking_rect)
    screen.blit(player_surface, player_rect)

    #Viking Animation
    viking_rect.right -= 4
    if viking_rect.right <= 0: viking_rect.left = 900

    #Player Animation
    player_rect.left += 1
    if player_rect.left >= 900: player_rect.left = 100

    #Coollision
    mouse_pos = pygame.mouse.get_pos() 
    if player_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())

    #Keyboard
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("Jump")


    pygame.display.update()
    clock.tick(60)

    #Rectangles (in Loop)
    # pygame.draw.line(screen,"Gold", (0,0),pygame.mouse.get_pos(),2) drawing a line
    # pygame.draw.ellipse(screen,"Gold", pygame.Rect(50,200,100,100)) #Drawing object

    # Collisions(in Loop)
    # if player_rect.colliderect(viking_rect):
    # print("Collision") #It returns 0 or 1

    #in Loop For
    #if event.type == pygame.MOUSEBUTTONDOWN: #try with position MOUSEMOTION and event.pos to check position of 
        # print("Mouse Down")
        # if event.type == pygame.MOUSEMOTION:
        # if player_rect.collidepoint(event.pos): print("Collision") # Printing collision for mouse and image
