import pygame

#Initialize Pygame and screen dimensiom
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

# Load and scale images directly
background_image = pygame.transform.scale(
    pygame.image.load('images.jpg').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

bluebells_image = pygame.transform.scale(
    pygame.image.load('images (1).jpg').convert_alpha(), (200,200))
bluebells_rect = bluebells_image.get_rect(center=(SCREEN_WIDTH // 2,
    SCREEN_HEIGHT // 2 - 50))

# Initialize font, render text and set text position
text = pygame.font.Font(None, 36).render('Bluebells are a native woodland flower and are found in the UK and Europe.', True, pygame.Color('blue'))
textrect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 +110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(bluebells_image, bluebells_rect)
        display_surface.blit(text,textrect)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if__name__=='__main__':
game_loop()