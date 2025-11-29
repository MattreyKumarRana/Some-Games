# Mouse Movement in Pygame
import pygame

# Initialize the pygame
pygame.init()

# Create display surface for the game
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mouse Movement!")

# Load in the images
dragon_image = pygame.image.load("./assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

# Main Game Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x = event.pos[0]
      mouse_y = event.pos[1]
      dragon_rect.centerx = mouse_x
      dragon_rect.centery = mouse_y
      
    if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
      mouse_x = event.pos[0]
      mouse_y = event.pos[1]
      dragon_rect.centerx = mouse_x
      dragon_rect.centery = mouse_y
  
  # Fill up the old images 
  display_surface.fill((0,0,0)) 
    
  # Blit (copy) the image on the display surface
  display_surface.blit(dragon_image, dragon_rect)
    
  # Update the Game
  pygame.display.update()
  
# End the game
pygame.quit()