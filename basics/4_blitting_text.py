# Blitting Text in Pygame

import pygame

# Initialize pygame
pygame.init()

# Create display surface for the game
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Text!")

# Setting up colors for the fonts
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

# Use fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('assets/AttackGraffiti.ttf', 32)

# Define Text
system_text = system_font.render("Dragons Rule", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

custom_text = custom_font.render("Feed the Dragon", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 75)

# Main Game Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  display_surface.blit(system_text, system_text_rect)
  display_surface.blit(custom_text, custom_text_rect)
  pygame.display.update()
  
# Quit the game
pygame.quit()