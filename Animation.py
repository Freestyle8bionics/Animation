import pygame
import os
import imageio
# Initialize pygame
pygame.init()

# Set window size
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Border Collie Animation")

# Create directory for frames if it doesn't exist
if not os.path.exists('frames'):
    os.makedirs('frames')

DEFAULT_IMAGE_SIZE = (200, 200)

# Load both sets of dog images
dog_images1 = [pygame.image.load("reference/IMG_2068.jpeg")] * 1  # First dog
dog_images2 = [pygame.image.load("reference/IMG_0409.jpeg")] * 1  # Second dog
dog_images3 = [pygame.image.load("reference/IMG_4094.png")] * 1
dog_images4 = [pygame.image.load("reference/IMG_0140.jpeg")] * 1
dog_images5 = [pygame.image.load("reference/IMG_0138.jpeg")] * 1

# Rotate and scale all images
dog_images1 = [pygame.transform.scale(pygame.transform.rotate(img, 270), DEFAULT_IMAGE_SIZE) for img in dog_images1]
dog_images2 = [pygame.transform.scale(pygame.transform.rotate(img, 270), DEFAULT_IMAGE_SIZE) for img in dog_images2]
dog_images3 = [pygame.transform.scale(pygame.transform.rotate(img, 0), DEFAULT_IMAGE_SIZE) for img in dog_images3]
dog_images4 = [pygame.transform.scale(pygame.transform.rotate(img, 270), DEFAULT_IMAGE_SIZE) for img in dog_images4]
dog_images5 = [pygame.transform.scale(pygame.transform.rotate(img, 270), DEFAULT_IMAGE_SIZE) for img in dog_images5]

# Combine images into one sequence
all_images = dog_images1 + dog_images2 + dog_images3 + dog_images4 + dog_images5
current_frame = 0

running = True
clock = pygame.time.Clock()

dog_x = (width - DEFAULT_IMAGE_SIZE[0]) // 2
dog_y = (height - DEFAULT_IMAGE_SIZE[1]) // 2

walking_speed = 5
walking_direction = 1  # 1 for right, -1 for left

# Initialize font
font = pygame.font.Font(None, 36)

frame_count = 0

frames = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation frame
    current_frame = (current_frame + 1) % len(all_images)

    # Draw the background and dog
    screen.fill((255, 255, 255))  # White background

    # Update dog's position
    dog_x += walking_speed * walking_direction

    # Make the dog bounce off the edges of the screen
    if dog_x < 0 or dog_x > width - DEFAULT_IMAGE_SIZE[0]:
        walking_direction *= -1

    # Draw the current dog image
    screen.blit(all_images[current_frame], (dog_x, dog_y))

    # Render and display the text
    text = font.render("Happy Birthday Annabelle and Isaac!", True, (24, 0, 41))
    screen.blit(text, (width // 2 - text.get_width() // 2, 10))

    # Save frame
    pygame.image.save(screen, f"frames/frame{frame_count}.png")
    frames.append(imageio.imread(f"frames/frame{frame_count}.png"))
    frame_count += 1

    pygame.display.flip()
    clock.tick(1)  # 30 frames per second

pygame.quit()

imageio.mimsave('Patch.gif', frames, duration=0.033)