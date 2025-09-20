import pygame

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
            quit()
            
        #rectangle drawing
        pygame.draw.rect(display_window,(255,0,0),(50,75,100,75))
        pygame.Rect(50,60,100,75)

    # Update the display with the new drawings
    pygame.display.flip() 