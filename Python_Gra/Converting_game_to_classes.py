import pygame
from sys import exit
import random

class Player(pygame.sprite.Sprite): # Creating spirit class to start everything (spirit have 2 main actions (draw sprites and update sprites))
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Eivor.png").convert_alpha()
        player_walk_2 = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Eivor_movement.png").convert_alpha() 
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Eivor_jump.png").convert_alpha() 
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound(r'D:\Repozytorium\Kody_Python\Python_Gra\[YT2mp3.info] - Mariusz Pudzianowski - POLSKA GÓRĄ (320kbps).mp3')
        # (r'D:\Repozytorium\Kody_Python\Python_Gra\[YT2mp3.info] - Mariusz Pudzianowski - POLSKA GÓRĄ (320kbps).mp3')
        # (r'D:\Repozytorium\Kody_Python\Python_Gra\Polska_Gurom.mp3') 
    def player_input(self):
        keys = pygame.key.get_pressed() # All keys that have been pressed for players
        if keys[pygame.K_SPACE] and self.rect.bottom >= 518:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 518:
            self.rect.bottom = 518

    def animation_state(self):
        if self.rect.bottom < 518:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self): # update method to run all methods written in class
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstackle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type =="fly":
            fly_frame_1 = pygame.transform.rotozoom(pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Fly.png").convert_alpha(),0,0.2)
            fly_frame_2 = pygame.transform.rotozoom(pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Fly_movement.png").convert_alpha(),0,0.2)
            self.frames = [fly_frame_1,fly_frame_2]
            y_pos = 350
        else:
            viking_frame_1 = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Viking.png").convert_alpha() #uploading an image - use covert for
            viking_frame_2 = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Viking_movement.png").convert_alpha() #uploading an image - use covert for
            self.frames = [viking_frame_1, viking_frame_2]
            y_pos = 518
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900,1100),y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def collisions(player,obstackles):
    if obstackles:
        for obstackle_rect in obstackles:
            if player.colliderect(obstackle_rect): return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstackle_group,False): #colliding True will be killed False not
        obstackle_group.empty()
        return False
    else:
        return True    

def obstackle_movement(obstackle_list):
    if obstackle_list: #if there is nothing in list it will not work but for everyminions spawn it will
        for obstackle_rect in obstackle_list: #Animation
            obstackle_rect.x -= 5 # Animationf for obstackles -5
            if obstackle_rect.bottom == 518: # Spawning both vikings and planes
                screen.blit(viking_surface,obstackle_rect)
            else:
                screen.blit(fly_surface,obstackle_rect)


        obstackle_list = [obstackle for obstackle in obstackle_list if obstackle.x>-100] #Deleting an object which will go through left wall

        return obstackle_list
    else: return [] # To avoid error for empty list at start of the game

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time # /1000 o have 1 number and integer to dont gave float
    score_surf = test_font.render(f' Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (460,100))
    screen.blit(score_surf, score_rect)
    return current_time # Returning actual current time

def player_animation():
    #play walking animation if player is on floor
    #display jump surface when player not on the floor
    global player_surface, player_index

    if player_rect.bottom < 518:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]

#Initing the game (major variables)
pygame.init() #First stem required to init the game
screen = pygame.display.set_mode((920,613)) #Setting up a display and it's dimension
pygame.display.set_caption("Maciej's Game") #Title on the game's Bbar
clock = pygame.time.Clock() #Initiating the framerate
game_active = False # Variable which means is game is running or we back to menu
start_time = 0 # Variable for setting up start time
score = 0

player = pygame.sprite.GroupSingle() # Creating a group to start with drawing objects
player.add(Player()) # Addong Player object class to group

obstackle_group = pygame.sprite.Group()

#Text objects
test_font = pygame.font.Font(None,50) # setting up the font for different text rendering

#Background object
sky_surface = pygame.image.load(r'D:\Repozytorium\Kody_Python\Python_Gra\Sky.png').convert() #uploading an image - use covert for better 
snow_surface = pygame.image.load(r'D:\Repozytorium\Kody_Python\Python_Gra\Snow.png').convert() #use convert to better apply on screen

#Text objects
text_surface= test_font.render("AC Valhalla - Deluxe Budget Edition",False,"Black") #Creating a title text in game loop
text_rect = text_surface.get_rect(center = (460,50)) #Rect
game_message = test_font.render("Press Space to enter the gane",True,"Black") #Creating a title text in game loop
game_message_rect = game_message.get_rect(center = (460,550)) #Rect

#Viking frames creation
viking_frame_1 = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Viking.png").convert_alpha() #uploading an image - use covert for
viking_frame_2 = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Viking_movement.png").convert_alpha() #uploading an image - use covert for
viking_frames = [viking_frame_1, viking_frame_2]
viking_frame_index = 0
viking_surface = viking_frames[viking_frame_index]

#Flu frames creation
fly_image = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Fly.png").convert_alpha()
fly_image_2 = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Fly_movement.png").convert_alpha()
fly_frame_1 = pygame.transform.rotozoom(fly_image,0,0.2)
fly_frame_2 = pygame.transform.rotozoom(fly_image_2,0,0.2)
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

#Movable object - game
player_walk_1 = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Eivor.png").convert_alpha() #uploading an image - use covert for better 
player_walk_2 = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Eivor_movement.png").convert_alpha() #uploading an image - use covert for better 
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Eivor_jump.png").convert_alpha() #uploading an image - use covert for better 
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (100,518)) #Rect

#Viking + FLy list
obstackle_rect_list = []

#Score Screen - player
player_surface_score = pygame.image.load(r"D:\Repozytorium\Kody_Python\Python_Gra\Eivor.png").convert_alpha() # 1 Importing image
player_surface_score_scaled = pygame.transform.rotozoom(player_surface_score, 0, 3)# 2. Overrite to scale 
player_rect_score = player_surface_score_scaled.get_rect(center = (460,307))# 3. Creating rctangle 

#Animation variables
player_gravity = 0 

#Timer
obstackle_timer = pygame.USEREVENT + 1 # +1 to avoid conflict to each event
pygame.time.set_timer(obstackle_timer, 1500) # If printed in gameloop then every 900 milisecont print will appear

viking_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(viking_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

#Game Loop - describe all thinks that will be displayed and ongoing in the game 
while True:
    """Loop for the whole game"""    
    for event in pygame.event.get(): #Every event will be desrbides separatly in pygame.event.get

        #Game close
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 

        #Game_active when is True and all actions can by done by player
        if game_active:

        #Mouse Jump
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 518: 
                        player_gravity = -25
                        
        #Keyboard Jump
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 518:
                if event.key == pygame.K_SPACE: 
                    player_gravity = -25

        else: #Stetement when game is no active (when You fall)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)# setting time to zero when game restart (current time - start_time)
        
        if game_active:

            if event.type == obstackle_timer: #Viking and fly will spawn
                obstackle_group.add(Obstackle(random.choice(["fly", "viking"])))

            if event.type == viking_animation_timer:
                if viking_frame_index ==0:
                    viking_frame_index =1
                else:
                    viking_frame_index =0
                viking_surface = viking_frames[viking_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index ==0:
                    fly_frame_index =1
                else:
                    fly_frame_index =0
                fly_surface = fly_frames[fly_frame_index]
        

    if game_active: # Statement that game is running (TRUE) - ACTUAL GAME PART

        #Diplaying objects (other than players)
        screen.blit(sky_surface,(0,0))
        screen.blit(snow_surface,(0,518))
        screen.blit(text_surface, text_rect)

        #Score displaying on active game
        score = display_score() #basic score is 0

        #Viking movement
        obstackle_rect_list = obstackle_movement(obstackle_rect_list)
        #Drawing Player
        player.draw(screen)
        player.update()
        obstackle_group.draw(screen)
        obstackle_group.update()

        game_active = collision_sprite()

    else: #END Game part
        score_message = test_font.render(f"Your score: {score}", False, (64,64,64))
        score_message_rect = score_message.get_rect(center = (460,550))
        obstackle_rect_list.clear() # Removing list to clear all monestrs after failing the game
        player_rect.midbottom=(100,518) # setting players position for respawning
        player_gravity = 0 # setting players position for respawning
        screen.fill((160,82,65)) #Bacground for score 
        screen.blit(text_surface,text_rect)
        screen.blit(player_surface_score_scaled,player_rect_score)

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60)
