import pygame,sys
from pygame.locals import *
from ghost import *

# bien mac dinh
WINDOWNHEIGHT = 540
WINDOWNWIDTH = 1200
FPS = 100

# khoi tao giao dien game
pygame.init()
screen = pygame.display.set_mode((WINDOWNWIDTH,WINDOWNHEIGHT))
clock = pygame.time.Clock()
up,down,left,right = False,False,False,False


# tao event cho ghost
ghost_flap = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_flap,50) 
# tao event cho bug
bug_flap = pygame.USEREVENT
pygame.time.set_timer(bug_flap,10) 

new_ghost = Ghost()
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
            new_ghost.ghost_animations()
        # animation bug
        if event.type == bug_flap:
            new_bug.bug_animations()
    new_ghost.ghost_move()
    new_bug.bug_move(up,down,left,right)
    new_bug.bug_rotate()
    new_background.draw_background(screen)
    screen.blit(new_bug.bug,new_bug.bug_rect)
    screen.blit(new_ghost.ghost,new_ghost.ghost_rect)
    pygame.display.update()
    clock.tick(FPS)