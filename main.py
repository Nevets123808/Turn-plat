import pygame
from pygame.locals import *
import math as maths


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 32
        self.dx = 0
        self.dy = 0
        self.rect = pygame.Rect((16*self.x, 16*self.y),(self.width, self.height))
        self.landed = False
        self.double = True
    
    def draw(self, screen):
        self.rect = pygame.Rect((16*self.x, 16*self.y),(self.width, self.height))
        pygame.draw.rect(screen, (255,0,0), self.rect, width=0)
        text = f"{self.x}, {self.y}\n{self.dx}, {self.dy}"
        text_surface = FONT.render(text, True, (0,0,0))
        screen.blit(text_surface, (1,1))

    def input(self, event):
        if self.landed or self.double:
            if self.landed:
                if event.key == K_w:
                    self.dy -= max(2,maths.floor(maths.sqrt(abs(self.dx))))
                    self.landed = False
                elif event.key == K_a:
                    if self.dx > 1:
                        self.dx -= 1
                    self.dx -= 1
                elif event.key == K_d:
                    if self.dx < -1:
                        self.dx += 1
                    self.dx += 1
            elif self.double:
                if event.key == K_w:
                    self.dy -= 2
                    self.double = False
                elif event.key == K_q:
                    self.dy -= 1
                    if self.dx > 1:
                        self.dx -= 1
                    self.dx -= 1
                    self.double = False
                elif event.key == K_e:
                    self.dy -= 1
                    if self.dx < -1:
                        self.dx += 1
                    self.dx += 1
                    self.double = False
                else:
                    self.dy += 1
                    self.x += self.dx 
                    self.y += self.dy
        else:
            self.dy += 1
        self.x += self.dx 
        self.y += self.dy
    def land(self):
        self.landed = True
        self.double = True
        self.dy = 0


class Platform:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x*16,(y+1)*16,w*16,h*16)
    
    def draw(self,screen):
        pygame.draw.rect(screen, (100,100,100), self.rect, width = 0)

    def check(self,player):
        if  player.dy > 0 and self.y - 1 <= player.y < self.y + self.h and self.x <= player.x < self.x + self.w:
            player.land()
            player.y = self.y - 1

SCREENWIDTH = 640
SCREENHEIGHT = 480

def main():
    active = True
    turn = True
    player = Player(2,20)
    plat = Platform(10,18,3,1)
    while active:
        plat.check(player)
        if player.y >= 20:
            player.land()
            player.y = 20


        for event in pygame.event.get():
            if event.type == QUIT:
                active = False
            if turn and event.type == KEYDOWN:
                player.input(event)
        screen.fill((255,255,255))
        pygame.draw.rect(screen, (125,125,125),(0,22*16,640,32),width=0)
        plat.draw(screen)
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    FONT =pygame.font.Font(None, 32)
    screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
    clock = pygame.time.Clock()
    main()
    pygame.quit()