# Feed the Dragon Game 1
import pygame, random

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
lives_rect.topright = (WINDOW_WIDTH - 20, 10)

game_over_text = font.render("GAME OVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)


# Set up sounds for the game
coin_sound = pygame.mixer.Sound("./assets/coin_sound.wav")
miss_sound = pygame.mixer.Sound("./assets/miss_sound.wav")
miss_sound.set_volume(0.1)
pygame.mixer.music.load("./assets/ftd_background_music.wav")

# Set up images for the game
player_image = pygame.image.load("./assets/dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2

coin_image = pygame.image.load("./assets/coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

# Main Game Loop
pygame.mixer.music.play(-1)
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Move the player
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_UP] and player_rect.top > 64:
    player_rect.y -= PLAYER_VELOCITY
  if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
    player_rect.y += PLAYER_VELOCITY
    
  # Coin Movement
  if coin_rect.x < 0:
    miss_sound.play()
    player_lives -= 1
    coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
    coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
  else:
    coin_rect.x -= coin_velocity
    
  if player_rect.colliderect(coin_rect):
    score += 1
    coin_velocity += COIN_ACCELERATION
    coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
    coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    
  # Text Rendering 
  lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
  
  # Fill up display surface
  display_surface.fill(BLACK)
      
  # Blit (copy) HUD to the game surface
  display_surface.blit(score_text, score_rect)
  display_surface.blit(title_text, title_rect)
  display_surface.blit(lives_text, lives_rect)
  pygame.draw.line(display_surface, WHITE, (0, 64), (WINDOW_WIDTH, 64), 2)
      
  # Blit images to the display surface
  display_surface.blit(player_image, player_rect)
  display_surface.blit(coin_image, coin_rect)
  
  # update the game
  pygame.display.update()
  
  # Set the FPS and clock
  clock.tick(FPS)
  
# End the game
pygame.quit()