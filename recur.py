import pygame
import random

# Initialize pygame
pygame.init()

# Define screen dimensions and create a window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Find Waldo!")


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load background image
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Load Waldo image
waldo_image = pygame.image.load('waldo.png')

# Initial size of Waldo
max_waldo_width, max_waldo_height = 100, 100  # Set initial size for Waldo
waldo_image = pygame.transform.scale(waldo_image, (max_waldo_width, max_waldo_height))

waldo_width, waldo_height = waldo_image.get_size()

# Set the percentage by which Waldo shrinks after each score
shrink_factor = 0.9  # Waldo will shrink by 10% each time

# Set font for score display
font = pygame.font.SysFont(None, 36)

# Function to display the score
def display_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (screen_width - 150, 10))

# Function to generate random position for Waldo
def random_waldo_position():
    x = random.randint(0, screen_width - waldo_width)
    y = random.randint(0, screen_height - waldo_height)
    return x, y

# Game variables
score = 0
waldo_position = random_waldo_position()

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw the background
    screen.blit(background_image, (0, 0))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if waldo_position[0] <= mouse_x <= waldo_position[0] + waldo_width and waldo_position[1] <= mouse_y <= waldo_position[1] + waldo_height:
                score += 1
                # Move Waldo to a new random location
                waldo_position = random_waldo_position()

                # Shrink Waldo by 10% after each score
                waldo_width = int(waldo_width * shrink_factor)
                waldo_height = int(waldo_height * shrink_factor)

                # Prevent Waldo from shrinking too much
                if waldo_width < 20:
                    waldo_width = 20
                if waldo_height < 20:
                    waldo_height = 20

                # Resize the Waldo image
                waldo_image = pygame.transform.scale(waldo_image, (waldo_width, waldo_height))

    # Draw Waldo
    screen.blit(waldo_image, waldo_position)
    
    # Display the score
    display_score(score)
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
