import pygame
from pygame.locals import *


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 32
        self.dx = 0
        self.dy = 0
        self.rect = pygame.Rect((16*self.x, 16*self.y),(self.width, self.height))
    
    def draw(self, screen):
        self.rect = pygame.Rect((16*self.x, 16*self.y),(self.width, self.height))
        pygame.draw.rect(screen, (255,0,0), self.rect, width=0)
        text = f"{self.dx}, {self.dy}"
        text_surface = FONT.render(text, True, (0,0,0))
        screen.blit(text_surface, (1,1))

    def input(self, event):
        if event.key == K_w:
            self.dy -= 1
        elif event.key == K_x:
            self.dy += 1
        elif event.key == K_a:
            self.dx -= 1
        elif event.key == K_d:
            self.dx += 1

        self.x += self.dx 
        self.y += self.dy

SCREENWIDTH = 640
SCREENHEIGHT = 480

def main():
    active = True
    turn = True
    player = Player(2,2)
    while active:
        for event in pygame.event.get():
            if event.type == QUIT:
                active = False
            if turn and event.type == KEYDOWN:
                player.input(event)
        screen.fill((255,255,255))
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    FONT =pygame.font.Font(None, 32)
    screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
    clock = pygame.time.Clock()
    main()
    pygame.quit()