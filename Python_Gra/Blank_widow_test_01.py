#https://www.youtube.com/watch?v=AY9MnQ4x3zk
import pygame
from sys import exit

pygame.init() #Starts pygame - engine of the car

screen = pygame.display.set_mode((920,700)) #Creating diplay surface (black)

pygame.display.set_caption("Maciej's Game") # Title of our Game

clock = pygame.time.Clock() #Creating clock object
test_font = pygame.font.Font(None,50) #default and size of font

#Considering specific colors *uncomment*
#test_surface = pygame.Surface((300,600)) #Black surface if no action is taken
#test_surface.fill("Red")

sky_surface = pygame.image.load(r'D:\Repozytorium\Kody_Python\Python_Gra\Sky.png')#Uploading Sky as a surface
snow_surface = pygame.image.load(r'D:\Repozytorium\Kody_Python\Python_Gra\Snow.png')
text_surface= test_font.render("My game",False,"Black")

while True:
    """Avoiding closing the program"""    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Synonymous of x button to close the game
            pygame.quit() #Opposite of pygame.init()
            exit() #exiting Loop while
    
    screen.blit(sky_surface,(0,0))#block image transfer (one surface )
    screen.blit(snow_surface,(0,518))#block image transfer (one surface )
    screen.blit(text_surface,(390,50))
    pygame.display.update() #Is an update of created surface ,,screen = pygame.display.set_mode((1920,1080))""
    clock.tick(60) #This Loop should not play faster than 60 fps (maximum framerate)