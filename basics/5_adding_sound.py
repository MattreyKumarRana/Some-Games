# Adding sounds in pygame
import pygame

# Initializing Pygame 
pygame.init()

# Create a display surface for the game
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Allowing Sounds')

# Allowing Sounds
sound1 = pygame.mixer.Sound('assets/sound_1.wav')
sound2 = pygame.mixer.Sound('assets/sound_2.wav')

sound1.play()
pygame.time.delay(2000)
sound2.play()

# Change sound volume to new set vol
pygame.time.delay(2000)
sound2.set_volume(0.2)
sound2.play()

# Setting up background music for the game
pygame.time.delay(2000)
pygame.mixer.music.load('assets/music.wav')
pygame.mixer.music.play(-1, 0.0)

# Main Game Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.update()


# Quit the game
pygame.quit()