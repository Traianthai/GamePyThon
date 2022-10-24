
import random

from tkinter.tix import WINDOW
import pygame,sys
from pygame.locals import *
import math
def bug_rotate(bug1):
    new_bug = pygame.transform.rotozoom(bug,bug_movement*1.5,1)
    return new_bug
def bug_animations():
    new_bug = bug = bug_list[bug_index]
    new_bug_rect = new_bug.get_rect(center = (bug_rect.centerx,bug_rect.centery))
    return new_bug,new_bug_rect
def bug_move(up,down,left,right):
    if up:
        if bug_rect.centery > 55: bug_rect.centery -= speed 
    if down:
        if bug_rect.centery < WINDOWNHEIGHT - 150: bug_rect.centery += speed
    if left:
        if bug_rect.centerx > 55: bug_rect.centerx -= speed
    if right:
        if bug_rect.centerx < WINDOWNWIDTH - 65: bug_rect.centerx += speed

def ghost_animations():
    new_ghost = ghost_list[ghost_index]
    new_ghost_rect = new_ghost.get_rect(center = (ghost_rect.centerx,ghost_rect.centery))
    return new_ghost,new_ghost_rect

def ghost_move():
    ghost_rect.centerx -= 1
    a = int(math.sin(ghost_speed*math.pi/360)*3)
    if ghost_rect.centery <= 70 and a > 0:
        return
    ghost_rect.centery -= a


def draw_background():
    for i in background_list:
        screen.blit(i,(scroll ,0))
        screen.blit(i,(background_width + scroll ,0))

# bien mac dinh
WINDOWNHEIGHT = 540
WINDOWNWIDTH = 1200
FPS = 100

# khoi tao giao dien game
pygame.init()
screen = pygame.display.set_mode((WINDOWNWIDTH,WINDOWNHEIGHT))
clock = pygame.time.Clock()
#tao bug
bug_size = 10
bug_list = []
for i in range (0,15):
    if i >= 10:
        bug_animation = pygame.transform.scale(pygame.image.load(f"bug_png/skeleton-animation_{i}.png"),(bug_size*11,bug_size*9)).convert_alpha()
    else:
        bug_animation = pygame.transform.scale(pygame.image.load(f"bug_png/skeleton-animation_0{i}.png"),(bug_size*11,bug_size*9)).convert_alpha()
    bug_list.append(bug_animation)

bug_index = 0
bug = bug_list[bug_index]
bug_rect = bug.get_rect(topleft = (50,50))
bug_movement = 0

# tao event cho bug
bug_flap = pygame.USEREVENT
pygame.time.set_timer(bug_flap,10) 
# bien di chuyen 
up,down,left,right = False,False,False,False
scroll = 0
speed = 10
#tao background
background_list = []
for i in range(1,6):
    background = pygame.transform.scale(pygame.image.load(f'backgroundLayers/layer-{i}.png'),(1700,WINDOWNHEIGHT)).convert_alpha()
    background_list.append(background)
background_width = background_list[1].get_width()
# tao ghost
ghost_size = 10
ghost_list = []
for i in range(0,10):
    ghost = pygame.transform.scale(pygame.image.load(f'ghost/png/skeleton-animation_0{1}.png'),(11*ghost_size,15*ghost_size)).convert_alpha()
    ghost_list.append(ghost)
for i in range(10,30):
    ghost = pygame.transform.scale(pygame.image.load(f'ghost/png/skeleton-animation_{i}.png'),(11*ghost_size,15*ghost_size)).convert_alpha()
    ghost_list.append(ghost)

ghost_index = 0
ghost = ghost_list[ghost_index]
ghost_rect = ghost.get_rect(topleft = (WINDOWNWIDTH-100,150))



# tao event cho ghost
ghost_flap = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_flap,50) 

# run
ghost_speed = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
        if event.type == KEYDOWN:
            if event.key == K_UP:
                up = True
                bug_movement = 10
            if event.key == K_DOWN:
                down = True
                bug_movement = -10
            if event.key == K_LEFT:
                left = True
            if event.key == K_RIGHT:
                right = True
        if event.type == KEYUP:
            bug_movement = 0
            up,down,left,right = False,False,False,False
        # vo canh 
        if event.type == bug_flap:
            if bug_index < 14:
                bug_index += 1
            else:
                bug_index = 0
            bug,bug_rect = bug_animations()  
        # animation ghost
        if event.type == ghost_flap:
            if ghost_index < 29:
                ghost_index += 1
            else:
                ghost_index = 0
            ghost,ghost_rect = ghost_animations()  
        
        # di chuyen background
    scroll -= 1
    if scroll <= -background_width:
        scroll = 0
    ghost_speed += 1
    bug_move(up,down,left,right)
    ghost_move()
    draw_background()
    rotated_bug = bug_rotate(bug)
    screen.blit(rotated_bug,bug_rect)
    screen.blit(ghost,ghost_rect)
    pygame.display.update()
    clock.tick(FPS)
