# Import necessary libraries
import pygame

# Initialize required modules
pygame.init()

# Setup window geometry
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Pygame Window")
clock = pygame.time.Clock()

# Create a loop to run till the game is quit by the user
done = False

while not done:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw a background and update the screen
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()