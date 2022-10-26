import pygame,sys
from pygame.locals import *
from ghost import *
from shadow_dog import *

# bien mac dinh
WINDOWHEIGHT = 540
WINDOWWIDTH = 1200
num_of_enemy = 30
FPS = 100

# khoi tao giao dien game
pygame.init()
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
clock = pygame.time.Clock()
up,down,left,right = False,False,False,False
game_active = 1
# tao enemy
enemy_list = []
for i in range (0,num_of_enemy//2): 
    enemy_list.append(Enemy2(0.5,1))
    enemy_list.append(Enemy1(0.5,1))

boom_list = []
spawboom = pygame.USEREVENT+1
pygame.time.set_timer(spawboom,90)
check_boom = 0

# tao nhan vat
# new_bug = Bug()
new_dog = Dog()
spawdog = pygame.USEREVENT
pygame.time.set_timer(spawdog,30)
#tao background
new_background = Background()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()  
        if game_active == 1:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    up = True
                    new_dog.movement = 10
                    new_dog.index_y = 1
                    
                if event.key == K_DOWN:
                    down = True
                    new_dog.movement = -10
                    new_dog.index_y = 2

                if event.key == K_LEFT:
                    left = True
                if event.key == K_RIGHT:
                    right = True
            if event.type == KEYUP:
                new_dog.movement = 0
                if new_dog.rect.centery < WINDOWHEIGHT-150:
                    new_dog.index_y = 2
                else:
                    new_dog.index_y = 3
                up,down,left,right = False,False,False,False
            new_dog.move(up,down,left,right)
        else: new_dog.move(False,False,True,False)
        if event.type == spawboom:
            for i in boom_list:
                i.update()
        if event.type == spawdog:
            new_dog.update()
            
    if new_dog.rect.centerx > 0:
        new_background.speed = 0
    if new_dog.rect.centerx > 260: 
        new_background.speed = 2
    if new_dog.rect.centerx > 660: 
        new_background.speed = 5
    for i in enemy_list:
        i.scroll = new_background.speed
    print(new_dog.rect.centerx,new_background.speed)
    for i in enemy_list:
        i.update()
        if new_dog.check_collision(i.rect): 
            boom_list.append(Boom(i.rect.centerx,i.rect.centery))
            enemy_list.remove(i)

# draw
    new_background.draw_background()
    for i in new_background.background_list:
            screen.blit(i,(new_background.scroll ,0))
            screen.blit(i,(new_background.background_width + new_background.scroll ,0))
            
    screen.blit(new_dog.dog,new_dog.rect)

    for i in boom_list:
        screen.blit(i.boom,i.rect)
        if i.index == 4:
            boom_list.remove(i)

    for i in enemy_list:
        screen.blit(i.enemy,i.rect)
    if len(enemy_list) == 0:
        game_active = 0 
        new_background.scroll = 0

    pygame.display.update()
    clock.tick(FPS)