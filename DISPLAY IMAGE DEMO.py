import pygame

# Initialize Pygame library 
pygame.init()

# RGB for white color
white = (255,255,255)   

# Create display window of size 1000x700
display_window =  pygame.display.set_mode((1000,700))    
pygame.display.set_caption("DISPLAY IMAGE")                  # Set window title

image = pygame.image.load(R"path_to_your_image\image.png")  # Load image from specified path 

while True:
    display_window.fill(white)                              # Fill display window with white color
    display_window.blit(image,(230,230))                    # Draw image at (230,230)
    
    # Get all events that happened since last frame 
    for each_event in pygame.event.get(): 
        
        # Check if event type is QUIT (if user clicked on close button)
        if each_event.type==pygame.QUIT: 
            
            # If the event was a quit event, quit Pygame and then exit Python program using sys.exit()
            pygame.quit()
            quit()
            
    # Update the display with the new drawings
    pygame.display.update() 