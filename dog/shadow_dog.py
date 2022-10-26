import pygame

WINDOWHEIGHT = 540
WINDOWWIDTH = 1200
class Dog:
    def __init__(self):
        self.size = 0.2
        self.list = []
        for i in range (0,10):
            list_tmp = []
            for j in range (0,12):
                try:
                    animation = pygame.transform.scale(pygame.image.load(f"dog\dog_png\dog{i}\dog{i}{j}.png"),(self.size*523,self.size*573)).convert_alpha()
                    list_tmp.append(animation)
                except FileNotFoundError:
                    pass
            self.list.append(list_tmp)

        self.index_x = 0
        self.index_y = 0
        tmp = self.list[self.index_y]
        self.dog = tmp[self.index_x]
        self.rect = self.dog.get_rect(topleft = (200,300))
        self.movement = 0
        self.speed = 10
    def update(self):
        if self.rect.centery < WINDOWHEIGHT - 150: self.rect.centery += self.speed
        else: self.index_y = 3
        tmp = self.list[self.index_y]
        if self.index_x < len(tmp)-1:
            self.index_x += 1
        else:
            self.index_x = 0
        tmp = self.list[self.index_y]
        self.dog = tmp[self.index_x]
        self.rect = self.dog.get_rect(center = (self.rect.centerx,self.rect.centery))
        # self.dog = pygame.transform.rotozoom(self.dog,self.movement*1.5,1)
    def move(self,up,down,left,right):
        if up:
            if self.rect.centery > 55: self.rect.centery -= self.speed*2
        if down:
            if self.rect.centery < WINDOWHEIGHT - 150: self.rect.centery += self.speed
        if left:
            if self.rect.centerx > 55: self.rect.centerx -= self.speed*1.2
        if right:
            if self.rect.centerx < WINDOWWIDTH - 65: self.rect.centerx += self.speed*1.2
    def check_collision(self,ghost): 
        if self.rect.colliderect(ghost):
            return True
        return False