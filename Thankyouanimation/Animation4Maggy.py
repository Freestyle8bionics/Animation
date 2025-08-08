import pygame
import os
import imageio
import subprocess
import numpy as np
 
# Initialize pygame
pygame.init()
 
# Set window size
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("\u0002Thank You Maggy\u0021")
 
# Create directory for frames if it doesn't exist
if not os.path.exists('frames'):
    os.makedirs('frames')
 
DEFAULT_IMAGE_SIZE = (200, 200)
 
# Load both sets of dog images (using different sets for variety)
images1 = [pygame.image.load(r"photos/IMG_1686.JPG")] * 1  # First dog
images2 = [pygame.image.load(r"photos/IMG_1687.JPG")] * 1  # Second dog
images3 = [pygame.image.load(r"photos/IMG_1688.JPG")] * 1
images4 = [pygame.image.load(r"photos/IMG_1689.JPG")] * 1
images5 = [pygame.image.load(r"photos/IMG_1690.JPG")] * 1
images6 = [pygame.image.load(r"photos/IMG_1691.JPG")] * 1
images7 = [pygame.image.load(r"photos/IMG_1692.JPG")] * 1
 
# Rotate and scale all images
images1 = [pygame.transform.scale(pygame.transform.rotate(img, 0), DEFAULT_IMAGE_SIZE) for img in images1]
images2 = [pygame.transform.scale(pygame.transform.rotate(img, 0), DEFAULT_IMAGE_SIZE) for img in images2]
images3 = [pygame.transform.scale(pygame.transform.rotate(img, 0), DEFAULT_IMAGE_SIZE) for img in images3]
images4 = [pygame.transform.scale(pygame.transform.rotate(img, 0), DEFAULT_IMAGE_SIZE) for img in images4]
images5 = [pygame.transform.scale(pygame.transform.rotate(img, 0), DEFAULT_IMAGE_SIZE) for img in images5]
images6 = [pygame.transform.scale(pygame.transform.rotate(img, 0), DEFAULT_IMAGE_SIZE) for img in images6]
images7 = [pygame.transform.scale(pygame.transform.rotate(img, 0), DEFAULT_IMAGE_SIZE) for img in images7]
 
# Combine images into one sequence and repeat them 3 times
image_sequences = [images1, images2, images3, images4, images5, images6, images7]
 
# Repeat each sequence 3 times
image_sequences = [seq * 3 for seq in image_sequences]
 
# Flatten the list of all images
all_images = [image for seq in image_sequences for image in seq]
 
# Initialize frame variables
current_frame = 0
running = True
clock = pygame.time.Clock()
 
# Initial dog position
images_x = (width - DEFAULT_IMAGE_SIZE[0]) // 2
images_y = (height - DEFAULT_IMAGE_SIZE[1]) // 2
 
walking_speed = 5
walking_direction = 1  # 1 for right, -1 for left
 
# Initialize font
font = pygame.font.Font(None, 36)
 
# Frame storage for GIF and video
frames = []
 
# Main animation loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Update animation frame
    current_frame = (current_frame + 1) % len(all_images)
 
    # Draw the background and dog
    screen.fill((255, 255, 255))  # White background
 
    # Update dog's position
    images_x += walking_speed * walking_direction
 
    # Make the dog bounce off the edges of the screen
    if images_x < 0 or images_x > width - DEFAULT_IMAGE_SIZE[0]:
        walking_direction *= -1
 
    # Draw the current dog image
    screen.blit(all_images[current_frame], (images_x, images_y))
 
    # Render and display the text
    text = font.render("\u0002Thank you for Everything Maggy\u0021", True, (24, 0, 41))
    screen.blit(text, (width // 2 - text.get_width() // 2, 10))
 
    # Capture frame for GIF/Video
    frame = pygame.surfarray.array3d(screen)  # Converts surface to 3D numpy array
    frames.append(frame)
 
    pygame.display.flip()
    clock.tick(30)  # 30 frames per second
 
# Quit pygame
pygame.quit()
 
# Save the animation as a GIF
imageio.mimsave('Thankyou.gif', frames, duration=0.033)  # duration in seconds per frame
 
# Convert the GIF to a video using ffmpeg (Optional)
subprocess.run(['ffmpeg', '-i', 'Thankyou.gif', 'Thankyou_Animation.mp4'])
 
 
 