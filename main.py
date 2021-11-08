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
    
    def draw(self, screen):
        self.rect = pygame.Rect((16*self.x, 16*self.y),(self.width, self.height))
        pygame.draw.rect(screen, (255,0,0), self.rect, width=0)
        text = f"{self.x}, {self.y}\n{self.dx}, {self.dy}"
        text_surface = FONT.render(text, True, (0,0,0))
        screen.blit(text_surface, (1,1))

    def input(self, event):

        if self.landed:
            if event.key == K_w:
                self.dy -= max(2,maths.floor(maths.sqrt(abs(self.dx))))
                self.landed = False
            elif event.key == K_a:
                self.dx -= 1
            elif event.key == K_d:
                self.dx += 1
        else:
            self.dy += 1
        self.x += self.dx 
        self.y += self.dy

SCREENWIDTH = 640
SCREENHEIGHT = 480

def main():
    active = True
    turn = True
    player = Player(2,2)
    
    while active:
        if player.y >= 20:
            player.landed = True
            player.y = 20
            player.dy = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                active = False
            if turn and event.type == KEYDOWN:
                player.input(event)
        screen.fill((255,255,255))
        pygame.draw.rect(screen, (125,125,125),(0,22*16,640,32),width=0)
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    FONT =pygame.font.Font(None, 32)
    screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
    clock = pygame.time.Clock()
    main()
    pygame.quit()