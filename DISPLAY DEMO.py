import pygame
import sys
from pygame.locals import *                                             # Initialize Pygame and set

pygame.init()                                                            # Initialize Pygame

display_window = pygame.display.set_mode((1000,750))                     # Set the display window size
pygame.display.set_caption('HARISH GAME WINDOW DEMO')                    # Set the window title the display window caption

while True: 
    for each_event in pygame.event.get():                                 # Event handling loop
        if each_event.type==QUIT:                                         # If the event is a quit event
            pygame.quit()
            sys.exit()

    pygame.display.update()    