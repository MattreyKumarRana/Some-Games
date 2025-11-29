# Drawing on surface

import pygame

# Initialize the game
pygame.init()

# Create the game surface
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

# Defining the colors of the surface
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

# background color
display_surface.fill(BLUE)

# making drawing shapes
pygame.draw.line(display_surface, RED, (0,0), (100, 100), 5)

pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 195, 0)

pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 200, 200))

# Game Loop
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  pygame.display.update()

    
# End the game
pygame.quit()
