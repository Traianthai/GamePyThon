import pygame,sys
from pygame.locals import *
from ghost import *

# bien mac dinh
WINDOWHEIGHT = 540
WINDOWWIDTH = 1200
NUMOFENEMY = 10
FPS = 100

# khoi tao giao dien game
pygame.init()
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
clock = pygame.time.Clock()
up,down,left,right = False,False,False,False


# tao event cho ghost
ghost_flap = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_flap,50) 
# tao event cho bug
bug_flap = pygame.USEREVENT
pygame.time.set_timer(bug_flap,10) 
# tao enemy
ghost_list = []
for i in range (0,NUMOFENEMY): ghost_list.append(Ghost(i+1))
new_bug = Bug()
new_background = Background()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
        if event.type == KEYDOWN:
            if event.key == K_UP:
                up = True
                new_bug.bug_movement = 10
            if event.key == K_DOWN:
                down = True
                new_bug.bug_movement = -10
            if event.key == K_LEFT:
                left = True
            if event.key == K_RIGHT:
                right = True
        if event.type == KEYUP:
            new_bug.bug_movement = 0
            up,down,left,right = False,False,False,False
        # animation ghost
        if event.type == ghost_flap:
            for i in range (0,NUMOFENEMY):
                ghost_list[i].ghost_animations()
        # animation bug
        if event.type == bug_flap:
            new_bug.bug_animations()
    for i in range (0,NUMOFENEMY):
        ghost_list[i].ghost_move()
        new_bug.check_collision(ghost_list[i].ghost_rect)

    new_bug.bug_move(up,down,left,right)
    new_background.draw_background(screen)
    screen.blit(new_bug.bug,new_bug.bug_rect)
    for i in range (0,NUMOFENEMY):
        screen.blit(ghost_list[i].ghost,ghost_list[i].ghost_rect)
    pygame.display.update()
    clock.tick(FPS)