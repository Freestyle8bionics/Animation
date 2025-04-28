import pygame
import os
import Animation.py
import subprocess
# from moviepy.editor import *
# from moviepy.editor import ImageSequenceClip

# Initialise pygame
pygame.init()

# Set window size
size = width,height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Border Collie Animation")

# Save the current frame as an image
num_frames = Animation:4

# Create directory for frames if it doesn't exist
if not os.path.exists('frames'):
    os.makedirs('frames')

# Generate and save frames
for i in range(num_frames):
    # Add your drawing code here
    pygame.image.save(screen, f"frames/frame{i}.png")

DEFAULT_IMAGE_SIZE = (200, 200)

# Load images (replace with your dog images)
dog_images2 = [pygame.image.load("reference/IMG_0409.jpeg"), pygame.image.load("reference/IMG_0409.jpeg"), pygame.image.load("reference/IMG_0409.jpeg"), pygame.image.load("reference/IMG_0409.jpeg")] #example images
current_frame = 1

# Rotate the images to the default rotation
dog_images2 = [pygame.transform.rotate(image, 270) for image in dog_images2]

images = [pygame.transform.scale(image, DEFAULT_IMAGE_SIZE) for image in dog_images2]

running = True
clock = pygame.time.Clock()

dog_x = (width - DEFAULT_IMAGE_SIZE[0]) // 2
dog_y = (height - DEFAULT_IMAGE_SIZE[1]) // 2

walking_speed = 5
walking_direction = 1 # 1 for right, -1 for left

# Initialize font
font = pygame.font.Font(None, 36)

# Initialize the video recording
pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
screen = pygame.display.get_surface()

# Initialize the video recording
# I have a linux system so I'm saving the files in a specific location
# You might need to change the format if your system doesn't work with it


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation frame
    current_frame = (current_frame + 1) % len(images)

    # Draw the background and dog
    screen.fill((255, 255, 255))  # White background

    # Update dog's position
    dog_x += walking_speed * walking_direction

    # Make the dog bounce off the edges of the screen
    if dog_x < 0 or dog_x > width - DEFAULT_IMAGE_SIZE[0]:
        walking_direction *= -1

    # Don't flip the image
    screen.blit(images[current_frame], (dog_x, dog_y))

    # Render and display the text
    text = font.render("Happy Birthday Annabelle and Isaac!", True, (24, 0, 41))
    screen.blit(text, (width // 2 - text.get_width() // 2, 10)) 

    

    pygame.display.flip()
    clock.tick(30) # 30 frames per second

pygame.quit()