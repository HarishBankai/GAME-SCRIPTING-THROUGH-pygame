# import pygame and sys modules, which are necessary for game development
import pygame
import sys

# Initialize Pygame library 
pygame.init()

display_window =  pygame.display.set_mode((1000,700))    
pygame.display.set_caption("DISPLAY DEMO")

# Infinite loop to keep the program running until user quits
while True:
    
    # Get all events that happened since last frame 
    for each_event in pygame.event.get(): 
        
        # Check if event type is QUIT (if user clicked on close button)
        if each_event.type==pygame.QUIT: 
            
            # If the event was a quit event, quit Pygame and then exit Python program using sys.exit()
            pygame.quit()
            sys.exit()
    
    # Update the display to show any changes made in the game since last update

    pygame.display.update() 
