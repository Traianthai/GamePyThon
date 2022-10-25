import pygame,math

WINDOWHEIGHT = 540
WINDOWWIDTH = 1200
class Ghost:
    def __init__(self,speed):
        self.ghost_size = 7
        self.ghost_list = []
        for i in range(0,10):
            ghost = pygame.transform.scale(pygame.image.load(f'dog/ghost/png/skeleton-animation_0{i}.png'),(11*self.ghost_size,15*self.ghost_size)).convert_alpha()
            self.ghost_list.append(ghost)
        for i in range(10,30):
            ghost = pygame.transform.scale(pygame.image.load(f'dog/ghost/png/skeleton-animation_{i}.png'),(11*self.ghost_size,15*self.ghost_size)).convert_alpha()
            self.ghost_list.append(ghost)

        self.ghost_index = 0
        self.ghost = self.ghost_list[0]
        self.ghost_rect = self.ghost.get_rect(topleft = (WINDOWWIDTH-100,150))
        self.ghost_speed = speed
        self.move = 0

    def ghost_animations(self):
        if self.ghost_index < 29:
                self.ghost_index += 1
        else:
                self.ghost_index = 0
        self.ghost = self.ghost_list[self.ghost_index]
        self.ghost_rect = self.ghost.get_rect(center = (self.ghost_rect.centerx,self.ghost_rect.centery))
    def ghost_move(self): # chua fix dc
        self.move += self.ghost_speed
        a = int(math.sin(self.move*math.pi/360)*2)
        b = self.move%5
        self.ghost_rect.centerx -= int(b)
        if self.ghost_rect.centery <= 70 and a > 0:
            return
        self.ghost_rect.centery -= a

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
        self.bug_rect = self.bug.get_rect(topleft = (50,50))
        self.bug_movement = 0
        self.speed = 10

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
            if bug_rect.centery < WINDOWHEIGHT - 150: bug_rect.centery += self.speed
        if left:
            if bug_rect.centerx > 55: bug_rect.centerx -= self.speed
        if right:
            if bug_rect.centerx < WINDOWWIDTH - 65: bug_rect.centerx += self.speed
    def check_collision(self,ghost): 
            if self.bug_rect.colliderect(ghost):
                print("vac cham")
 

class Background():
    def __init__(self):
        self.scroll = 0
        self.background_list = []
        for i in range(1,6):
            background = pygame.transform.scale(pygame.image.load(f'dog/backgroundLayers/layer-{i}.png'),(1700,WINDOWHEIGHT)).convert_alpha()
            self.background_list.append(background)
        self.background_width = self.background_list[1].get_width()

        
    def draw_background(self,screen):
        self.scroll -= 1
        if self.scroll <= -self.background_width:
            self.scroll = 0
        for i in self.background_list:
            screen.blit(i,(self.scroll ,0))
            screen.blit(i,(self.background_width + self.scroll ,0))