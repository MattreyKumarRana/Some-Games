# Movement Restriction and Alernate KeyMapping in Pygame
import pygame

# Initialize Pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Movement Restriction!")

# Load in images for the game
dragon_image = pygame.image.load("./assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH // 2
dragon_rect.centery = WINDOW_HEIGHT // 2

# Set up Constants for the game
VELOCITY = 10

# Set up FPS and clock for the game
FPS = 60
clock = pygame.time.Clock()

# Main Game Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # get keys pressed
  keys = pygame.key.get_pressed()
  
  if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
    dragon_rect.x -= VELOCITY
  if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
    dragon_rect.x += VELOCITY
  if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
    dragon_rect.y -= VELOCITY
  if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HEIGHT:
    dragon_rect.y += VELOCITY 
    
    
  # Fill up 
  display_surface.fill((0,0,0))
  
  # Blit (copy) image to the display surface
  display_surface.blit(dragon_image, dragon_rect)
  
  # Update Game
  pygame.display.update()
  
  # Add a clock delay
  clock.tick(FPS)
  
# End the game
pygame.quit()