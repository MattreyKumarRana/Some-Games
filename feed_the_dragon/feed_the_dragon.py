# Feed the Dragon Game 1
import pygame

# Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the dragon!")

# Set FPS and clock for the game
FPS = 60
clock = pygame.time.Clock()

# Set up constants for the game
PLAYER_VELOCITY = 5
PLAYER_STARTING_LIVES = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

# Set up colors for the game
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up text and fonts for the game
font = pygame.font.Font('assets/AttackGraffiti.ttf', 32)
score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed the Dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

# Main Game Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Blit (copy) to the game surface
  display_surface.blit(score_text, score_rect)
  display_surface.blit(title_text, title_rect)
  display_surface.blit(lives_text, lives_rect)
      
  # update the game
  pygame.display.update()
  
# End the game
pygame.quit()