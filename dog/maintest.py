import pygame,sys
from pygame.locals import *
from ghost import *


# bien mac dinh
WINDOWHEIGHT = 540
WINDOWWIDTH = 1200
num_of_enemy = 100
FPS = 100

# khoi tao giao dien game
pygame.init()
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
clock = pygame.time.Clock()
up,down,left,right = False,False,False,False

# tao enemy
enemy_list = []
for i in range (0,num_of_enemy): 
    enemy_list.append(Enemy2(0.5))

boom_list = []
spawboom = pygame.USEREVENT
pygame.time.set_timer(spawboom,90)
check_boom = 0

# tao nhan vat
new_bug = Bug()

#tao background
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
        if event.type == spawboom:
            for i in boom_list:
                i.update()
    new_bug.bug_animations()
    new_bug.bug_move(up,down,left,right)
    
    for i in enemy_list:
        i.update()
        if new_bug.check_collision(i.rect): 
            boom_list.append(Boom(i.rect.centerx,i.rect.centery))
            enemy_list.remove(i)

# draw
    new_background.draw_background()
    for i in new_background.background_list:
            screen.blit(i,(new_background.scroll ,0))
            screen.blit(i,(new_background.background_width + new_background.scroll ,0))
            
    screen.blit(new_bug.bug,new_bug.bug_rect)

    for i in boom_list:
        screen.blit(i.boom,i.rect)
        if i.index == 4:
            boom_list.remove(i)

    for i in enemy_list:
        screen.blit(i.enemy,i.rect)


    pygame.display.update()
    clock.tick(FPS)