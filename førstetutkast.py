import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movie Posters")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up box properties
poster_width = 200
poster_height = 300
button_width = 100
button_height = 40
vertical_spacing = 20
horizontal_spacing = 50
button_radius = 10  # Adjust the radius for rounded corners

# Load placeholder images
poster1_image = pygame.image.load("poster1.jpg")  # Replace with your image file
poster2_image = pygame.image.load("poster2.jpg")  # Replace with your image file

# Resize images to fit the box dimensions
poster1_image = pygame.transform.scale(poster1_image, (poster_width, poster_height))
poster2_image = pygame.transform.scale(poster2_image, (poster_width, poster_height))

# Calculate box positions
poster1_x = (width - 2 * poster_width - horizontal_spacing) // 3
poster1_y = height // 2 - poster_height // 2

poster2_x = 2 * (width - 2 * poster_width - horizontal_spacing) // 3 + poster_width + horizontal_spacing
poster2_y = height // 2 - poster_height // 2

button_higher_x = (width - button_width) // 2
button_higher_y = height // 2 - (button_height + vertical_spacing) // 2

button_lower_x = (width - button_width) // 2
button_lower_y = height // 2 + vertical_spacing // 2 + button_height + vertical_spacing

# Set up score
score = 0
font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 68)

# Set up game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for button clicks
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if (
                button_higher_x < mouse_x < button_higher_x + button_width
                and button_higher_y < mouse_y < button_higher_y + button_height
            ):
                print("Higher button clicked")
                # Add your code for the "Higher" button action here
                score += 1

            elif (
                button_lower_x < mouse_x < button_lower_x + button_width
                and button_lower_y < mouse_y < button_lower_y + button_height
            ):
                print("Lower button clicked")
                # Add your code for the "Lower" button action here
                score -= 1
    

    # Clear the screen
    screen.fill(black)

    # Draw movie posters with images
    screen.blit(poster1_image, (poster1_x, poster1_y))
    screen.blit(poster2_image, (poster2_x, poster2_y))

    # Draw rounded buttons
    pygame.draw.rect(screen, white, (button_higher_x, button_higher_y, button_width, button_height), border_radius=button_radius)
    pygame.draw.rect(screen, white, (button_lower_x, button_lower_y, button_width, button_height), border_radius=button_radius)

    # Add text to buttons
    text_higher = font.render("Higher", True, black)
    text_lower = font.render("Lower", True, black)

    # Center the text in the buttons
    text_higher_rect = text_higher.get_rect(center=(button_higher_x + button_width // 2, button_higher_y + button_height // 2))
    text_lower_rect = text_lower.get_rect(center=(button_lower_x + button_width // 2, button_lower_y + button_height // 2))

    screen.blit(text_higher, text_higher_rect.topleft)
    screen.blit(text_lower, text_lower_rect.topleft)

    # Draw the score
    score_text = score_font.render(f"Score: {score}", True, white)
    score_rect = score_text.get_rect(center=(width // 2, height - 50))
    screen.blit(score_text, score_rect.topleft)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
