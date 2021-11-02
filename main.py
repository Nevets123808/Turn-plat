import pygame
from pygame.locals import *



SCREENWIDTH = 640
SCREENHEIGHT = 480

def main():
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == QUIT:
                active = False

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
    clock = pygame.time.Clock()
    main()
    pygame.quit()