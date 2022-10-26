
import random
import pygame,math

WINDOWHEIGHT = 540
WINDOWWIDTH = 1200
class Enemy1:
    def __init__(self,size,scroll):
        self.size = size
        self.frame = 0
        self.scroll = scroll
        speed = random.randint(-2,2) +3
        self.flapspeed = speed
        self.list = []
        for i in range(0,6):
            enemy = pygame.transform.scale(pygame.image.load(f'dog/enemies/enemy1/enemy1.{i}.png'),(int(293*self.size),int(155*self.size))).convert_alpha()
            self.list.append(enemy)
        
        self.index = 0
        self.enemy = self.list[0]
        y = random.randint(13,WINDOWHEIGHT-200)
        x = random.randint(WINDOWWIDTH*1,WINDOWWIDTH*5)
        self.rect = self.enemy.get_rect(topleft = (x,y))

    def update(self):
        self.frame += 1
        if self.frame % self.flapspeed == 0:
            if self.index < 5:
                self.index += 1
            else:
                self.index = 0
        self.enemy = self.list[self.index]
        speed = random.randint(-2,2)
       
        self.rect.centerx += -(2+self.scroll)
        self.rect.centery += speed
        self.rect = self.enemy.get_rect(center = (self.rect.centerx,self.rect.centery))

class Enemy2:
    def __init__(self,size,scroll):
        self.size = size
        self.frame = 0
        self.scroll = scroll
        self.speed = random.randint(1,4)
        self.flapspeed = random.randint(1,4)
        self.list = []
        for i in range(0,6):
            enemy = pygame.transform.scale(pygame.image.load(f'dog/enemies/enemy2/enemy2.{i}.png'),(int(266*self.size),int(188*self.size))).convert_alpha()
            self.list.append(enemy)
        
        self.index = 0
        self.enemy = self.list[0]
        y = random.randint(13,WINDOWHEIGHT-200)
        x = random.randint(0,WINDOWWIDTH*5)
        self.rect = self.enemy.get_rect(topleft = (x,y))
        self.anpha = float(random.randint(1,3))

    def update(self):
        self.frame += 1
        self.anpha += self.speed
        if self.frame % self.flapspeed == 0:
            if self.index < 5:
                self.index += 1
            else:
                self.index = 0
        self.enemy = self.list[self.index]
        self.rect.centerx -= self.speed+self.scroll
        
        if self.rect.centerx < -100: 
            self.rect.centerx = WINDOWWIDTH +100
        # if self.rect.centery < WINDOWHEIGHT-100: 
        self.rect.centery -= int(math.cos(self.anpha*math.pi/360)*3)
        self.rect = self.enemy.get_rect(center = (self.rect.centerx,self.rect.centery))

class Bug:
    def __init__(self):
        self.bug_size = 9
        self.bug_list = []
        for i in range (0,15):
            if i >= 10:
                bug_animation = pygame.transform.scale(pygame.image.load(f"dog/bug_png/skeleton-animation_{i}.png"),(self.bug_size*11,self.bug_size*9)).convert_alpha()
            else:
                bug_animation = pygame.transform.scale(pygame.image.load(f"dog/bug_png/skeleton-animation_0{i}.png"),(self.bug_size*11,self.bug_size*9)).convert_alpha()
            self.bug_list.append(bug_animation)

        self.bug_index = 0
        self.bug = self.bug_list[self.bug_index]
        self.bug_rect = self.bug.get_rect(topleft = (150,340))
        self.bug_movement = 0
        self.speed = 6

    def bug_animations(self):
        if self.bug_index < 14:
                self.bug_index += 1
        else:
            self.bug_index = 0
        self.bug = self.bug_list[self.bug_index]
        self.bug_rect = self.bug.get_rect(center = (self.bug_rect.centerx,self.bug_rect.centery))
        self.bug = pygame.transform.rotozoom(self.bug,self.bug_movement*1.5,1)
    def bug_move(self,up,down,left,right):
        bug_rect = self.bug_rect
        if up:
            if bug_rect.centery > 55: bug_rect.centery -= self.speed 
        if down:
            if bug_rect.centery < WINDOWHEIGHT - 140: bug_rect.centery += self.speed
        if left:
            if bug_rect.centerx > 55: bug_rect.centerx -= self.speed
        if right:
            if bug_rect.centerx < WINDOWWIDTH - 65: bug_rect.centerx += self.speed
    def check_collision(self,ghost): 
        if self.bug_rect.colliderect(ghost):
            return True
        return False
 
class Background:
    def __init__(self):
        self.speed = 0
        self.scroll = 0
        self.background_list = []
        for i in range(1,6):
            background = pygame.transform.scale(pygame.image.load(f'dog/backgroundLayers/layer-{i}.png'),(1700,WINDOWHEIGHT)).convert_alpha()
            self.background_list.append(background)
        self.background_width = self.background_list[1].get_width()

        
    def draw_background(self):
        self.scroll -= self.speed
        if self.scroll <= -self.background_width:
            self.scroll = 0

class Boom:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 0.5
        self.list = []
        for i in range (0,5):
            animation = pygame.transform.scale(pygame.image.load(f"dog/enemies/boom/boom{i}.png"),(self.size*179,self.size*200)).convert_alpha()
            self.list.append(animation)
        self.check_boom = 0
        self.index = 0
        self.boom = self.list[self.index]
        self.rect = self.boom.get_rect(center = (self.x,self.y))
    def setx_y(self,x,y):
        self.x = 200
        self.y = 200

    def update(self):
        if self.index < 4:
            self.index += 1
        self.boom = self.list[self.index]
        
