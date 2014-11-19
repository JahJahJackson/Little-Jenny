import pygame
import sys
from pygame.locals import *
from random import randint

class Player (pygame.sprite.Sprite) :
    '''the class that the main character and controls. Jumping etc. 
        They dont move the world moves around them'''

    def __init__(self, start_x, start_y, width, height) :
    
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale (
            pygame.image.load(player_image), (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.speed_y = 0
        self.base = pygame.Rect (start_x, start_y+ height, width,2)
    

    def move_y(self):
        '''this is the y-axis movment for the sprite in the current speed'''
        self.rect.y = self.rect.y + 1
        collided_y = world.collided_get_y(self.base)
        if self.speed_y <= 0 or collided_y <0:
            self.rect.y = self.rect.y + self.speed_y
            self.speed_y = self.speed_y + gravity
        if collided_y > 0 and self.speed_y > 0:
            self.rect.y = collided_y
        self.base.y = self.rect.y + self.rect.height

    def jump (self, speed) :
        '''the player jumps only if its feet are on the ground'''
        pass

class World():
    '''The platforms and goals. The world moves side to side instead of the player.'''

    def __init__(self,level, block_size,
            color_platform, color_goals):
        self.platforms = []
        self.goals = []
        self.posn_y = 0
        self.color = color_platform
        self.color_goals = color_goals
        self.block_size = block_size
    
        for line in level:
            self.posn_x = 0
            for block in line:
                if block == "-":
                    self.platforms.append(pygame.Rect(
                        self.posn_x, self.posn_y,
                        block_size,block_size))
                if block == "G":
                    self.goals.append(pygame.Rect (
                        self.posn_x, self.posn_y,
                        block_size, block_size))
                self.posn_x = self.posn_x + block_size
            self.posn_y = self.posn_y + block_size
    

    def move(self, dist) :
        '''move the world dist pixels right, a negatives moves left'''
        pass

    def collided_get_y (self, player_rect):
        '''Get the y value of the platform the sprite is on'''
        pass

    def at_goal (self, player_rect):
        '''True is sprite is in contact with the goal. False if not'''
        pass
    
    def update (self, screen):
        '''draw all rectangles on the screen'''
        for block in self.platforms:
            pygame.draw.rect(screen, self.color, block, 0)
        for block in self.goals:
            pygame.draw.rect(screen, self.color_goals, block, 0)

    def collided_get_y(self,player_rect):
        '''Get the y value of the  platform the player is on'''
        return_y = -1
        for block in self.platforms:
            return_y = block.y - block.height + 1
        return return_y
            
class Doom() :
    '''this class holds all the things that can kill the sprite'''

    def __init__ (self, fireball_num, pit_depth, color) :
        pass
    
    def move(self, dist):
        '''move errthang right dist pixles (negative means left)'''
        pass

    def update (self, screen):
        '''move fireballs down, and draw errthang on the screen'''
        pass

    def collided (self, player_rect) :
        '''check and see if the sprite is in contact with the doom'''
        pass

class Blade (pygame.sprite.Sprite) :
    '''This class holds the fireballs that fall from the sky'''

    def __init__ (self):
        pass

    def reset (self):
        '''re-generate the blades a random distance along
        the screen and gives them random speed'''
    
    def move_x (self, dist):
        '''moves to right (negative to left)'''
        pass

    def move_y (self):
        '''moves the blades down the screen at a random speed. 
        Regenerates after passing the bottom'''
    

    def update(self, screen, color):
        '''draws blades onto the screen'''
        pass

#options
screen_x = 600
screen_y = 400
game_name = "Little Jenny's dungeon"
player_spawn_x = 50
player_spawn_y = 200
player_image = "tinyjenny.png"
gravity = 1

level=[
 "                             ",
 "                             ",
 "                             ",
 "                             ",
 "                             ",
 "                             ",
 "                             ",
 "          ---               G",
 "     -- --   ---       ------",
 " -- -           -------      ",]
platform_color = (100, 100, 100)
goal_color = (0, 0, 255)
#initialise pygame.mixer


#initialise pygame
pygame.init()
window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption(game_name)
screen = pygame.display.get_surface()

#load level
#initialise variables
clock = pygame.time.Clock()
finished = False
player = Player(player_spawn_x, player_spawn_y, 20,30)
player_plain = pygame.sprite.RenderPlain(player)
world = World(level, 30, platform_color,goal_color)

#setup the background 
while not finished :
    pass
    #blank screen
    screen.fill ((0,0,0))
    #check events
    for event in pygame.event.get():
        if event.type == QUIT:
                finished = True
    # check which keys are held

    #move the player with gravity
    player.move_y()
    #render the frame
    player_plain.draw(screen)
    world.update(screen)
    #update the display
    pygame.display.update()

    #check if the player is dead
    #check if the player has completed the level
    #set the speed
    clock.tick(20)














