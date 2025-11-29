# Displaying sureface in pygame
import pygame

# Initializing pygame
pygame.init()


# creating a display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

pygame.display.set_caption("Hello World")
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True

while running:
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.QUIT:
      running = False


# End the game
pygame.quit()
