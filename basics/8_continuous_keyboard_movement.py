# Continuous Keyboard Movement in Pygame
import pygame

# Initialize the pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Continuous Keyboard Movement")

# Load in images for the game
dragon_image = pygame.image.load("./assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH // 2
dragon_rect.centery = WINDOW_HEIGHT // 2  

# Settin up clock and FPS for the game
FPS = 60
clock = pygame.time.Clock()

# Set up constant variables
VELOCITY = 10

# Main Game Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # Get a list of keys
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_LEFT]:
    dragon_rect.x -= VELOCITY
  if keys[pygame.K_RIGHT]:
    dragon_rect.x += VELOCITY
  if keys[pygame.K_UP]:
    dragon_rect.y -= VELOCITY
  if keys[pygame.K_DOWN]:
    dragon_rect.y += VELOCITY 
    
  # Fill up 
  display_surface.fill((0,0,0))
  
  # Blit (copy) the image in display surface
  display_surface.blit(dragon_image, dragon_rect)
  
  # Update the game
  pygame.display.update()
  
  # Adding the clock delay to the game
  clock.tick(FPS)
  
# End the game
pygame.quit()