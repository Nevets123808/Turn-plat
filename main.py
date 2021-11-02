import pygame
from pygame.locals import *



SCREENWIDTH = 640
SCREENHEIGHT = 480


active = True

def main():
    while active:
        for event in pygame.event.get():
            if event.type == quit():
                active = False

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
    clock = pygame.time.Clock()
    main()
    pygame.quit()