# Collision Detection in Python
import pygame, random

# Initialize the pygame 
pygame.init()

# Create a display surface for the game
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection!")

# Set up FPS and clock for the game
FPS = 60
clock = pygame.time.Clock()

# Allowing Sounds
sound1 = pygame.mixer.Sound('assets/sound_1.wav')


# Loading Images
dragon_image = pygame.image.load("./assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)

coin_image = pygame.image.load("./assets/coin.png")
coin_rect = coin_image.get_rect()
coin_rect.centerx = WINDOW_WIDTH // 2
coin_rect.centery = WINDOW_HEIGHT // 2

# Set up Velocity
VELOCITY = 5

# Main Game Loop for the game
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_LEFT] and dragon_rect.left > 0:
    dragon_rect.x -= VELOCITY
  if keys[pygame.K_RIGHT] and dragon_rect.right < WINDOW_WIDTH:
    dragon_rect.x += VELOCITY
  if keys[pygame.K_UP] and dragon_rect.top > 0:
    dragon_rect.y -= VELOCITY
  if keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
    dragon_rect.y += VELOCITY
    
  # Fill up per update
  display_surface.fill((0,0,0))

  
  # Rect for the images
  pygame.draw.rect(display_surface, (0, 255, 0), dragon_rect, 1)
  pygame.draw.rect(display_surface, (255, 255, 0), coin_rect, 1) 
  
  # Check for the collisions
  if dragon_rect.colliderect(coin_rect):
    coin_rect.x = random.randint(0, WINDOW_WIDTH - 32) 
    coin_rect.y = random.randint(0, WINDOW_HEIGHT - 32) 
    sound1.play()
    
  
  # Blit (copy) the image to the display surface
  display_surface.blit(dragon_image, dragon_rect)
  display_surface.blit(coin_image, coin_rect)
  
  # Update the game
  pygame.display.update()
  
  # clock tick for the FPS
  clock.tick(FPS)
  
# End the Game
pygame.quit()