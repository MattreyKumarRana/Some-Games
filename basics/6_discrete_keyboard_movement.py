# Adding Discrete Keyboard Movement in Pygame
import pygame

# Initialize pygame
pygame.init()

# Create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Movement!")

# Set the game values
VELOCITY = 10

# Load in images for the game
dragon_image = pygame.image.load("./assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH // 2
dragon_rect.bottom = WINDOW_HEIGHT

# Main Game Loop
running = True
while running:
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        dragon_rect.x -= VELOCITY
      if event.key == pygame.K_RIGHT:
        dragon_rect.x += VELOCITY
      if event.key == pygame.K_UP:
        dragon_rect.y -= VELOCITY
      if event.key == pygame.K_DOWN:
        dragon_rect.y += VELOCITY
        
  # Fill up old images in the screen
  display_surface.fill((0,0,0)) 
      
  # Blit (copy) the image in display surface
  display_surface.blit(dragon_image, dragon_rect) 
      
  # Update the game
  pygame.display.update()
    
# End the game
pygame.quit()