import pygame  # this is a Library for making games ,it is only used in python 
import random  # Helps with random numbers ,
#Python’s random module uses a mathematical algorithm called a pseudo-random number generator (PRNG). 
# (like food placement) in our case the pring starts on the initial position of the food and calculates the next position of the food
import cv2  # Used for displaying video as background there is a command in the readme on how to insatall it
import numpy as np  # Helps with handling images from OpenCV and videos

# Initialize Pygame (this starts the game engine) it shows that the game has started to be executed
pygame.init()

# now we are setting the window on which the game will be played 
WIDTH, HEIGHT = 800, 600  # this is the screen size of the window we will use (in px form)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # pygame Creates the game window for us to use 
pygame.display.set_caption("Newton's_Snake Game")  # this is the window title for the game

# now lets Load video as background remember that the background video is displayed by the help of cv2 player
video_path = "/home/newton/pygame/sounds/backgroundgradientvideo.mp4"
cap = cv2.VideoCapture(video_path)  # Loading the video file into the game 

# now Loading the  sounds  that we will use in the game 
pygame.mixer.init()  
eat_sound = pygame.mixer.Sound("/home/newton/pygame/sounds/eat.wav")  # Sound when snake eats the food
game_over_sound = pygame.mixer.Sound("/home/newton/pygame/sounds/game_over.wav")  # Sound when game ends this happens when the snake hits a wall or it body

# Loading  background music to give the player moral 
pygame.mixer.music.load("/home/newton/pygame/sounds/backgroundmusic.mp3")
pygame.mixer.music.play(-1)  # Play music in a loop this means that the music will not end unless the player ends the game

# Colors e will use in the game  (RGB values)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Snake settings
snake_size = 20  # Size of each snake block 
snake_x = WIDTH // 2  # Start position X (middle of the screen)
snake_y = HEIGHT // 2  # Start position Y (middle of the screen)
snake_speed = 10  # How fast the snake moves initial speed 
velocity_x = 0  # Movement direction X  prevents snake from moving in two directions at the same time that is to x direction and y direction
velocity_y = 0  # Movement direction Y prevents snake from moving in two directions at the same time that is to x direction and y direction

# Snake body settings initial snake length
snake_body = [(snake_x, snake_y)]  # List to store snake parts (head and body)
snake_length = 3  # Start with three  segment

# Food settings 
food_size = 20  # Size of the food
food_x = random.randint(0, (WIDTH - food_size) // 20) * 20  # Random X position calculated by the random module 
food_y = random.randint(0, (HEIGHT - food_size) // 20) * 20  # Random Y position  calculated by the random module  PRING

# Score
score = 0  # Keep track of the player's score  initial score 
font = pygame.font.Font(None, 36)  # Font for displaying text on the screen 

# Game loop variables
running = True  # Keeps  the game running 
paused = False  # Pause state of the game 
clock = pygame.time.Clock()  # Helps control game speed thats is as the snake eats the food the speed increases
game_over = False  # Track if the game has ended if the game is not over the game will continue running

while running:
    # Read a frame from the background video
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart the video when it ends loop the video to avoid the white background
        continue
    
    # Resize and convert the video frame for display in Pygame so that it fits the window size
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert colors
    frame = np.rot90(frame)  # Rotate for correct orientation
    frame = pygame.surfarray.make_surface(frame)  # Convert to Pygame format
    screen.blit(frame, (0, 0))  # Draw video as background
    
    # Check if the game is over
    if game_over:
        game_over_sound.play()  # plays the game over sound
        pygame.time.delay(10000)  # Wait 10 seconds before the window closes the game over message is displayed
        pygame.mixer.music.stop()  # stops the game over sound playback
        
        # Display game over message
        text = font.render(f"Game Over! Final Score: {score} | Press R to Restart", True, BLACK)
        screen.blit(text, (WIDTH // 10, HEIGHT // 2))
        pygame.display.update()
        
        # Wait for user to restart or quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:  # Restart game
                snake_x = WIDTH // 2
                snake_y = HEIGHT // 2
                velocity_x = 0
                velocity_y = 0
                snake_body = [(snake_x, snake_y)]
                snake_length = 1
                food_x = random.randint(0, (WIDTH - food_size) // 20) * 20
                food_y = random.randint(0, (HEIGHT - food_size) // 20) * 20
                score = 0
                snake_speed = 10
                game_over = False
                pygame.mixer.music.play(-1)  # Restart background music
        continue
    
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pause or unpause game
                paused = not paused
            if not paused:
                if event.key == pygame.K_LEFT and velocity_x == 0:
                    velocity_x = -snake_speed
                    velocity_y = 0
                if event.key == pygame.K_RIGHT and velocity_x == 0:
                    velocity_x = snake_speed
                    velocity_y = 0
                if event.key == pygame.K_UP and velocity_y == 0:
                    velocity_x = 0
                    velocity_y = -snake_speed
                if event.key == pygame.K_DOWN and velocity_y == 0:
                    velocity_x = 0
                    velocity_y = snake_speed
    
    if paused:
        pause_text = font.render("Game Paused - Press P to Resume", True, BLACK)
        screen.blit(pause_text, (WIDTH // 4, HEIGHT // 2))
        pygame.display.update()
        continue
    
    # Move the snake
    snake_x += velocity_x
    snake_y += velocity_y
    
    # Check for collisions
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        game_over = True
    
    # Check if the snake eats the food
    if pygame.Rect(snake_x, snake_y, snake_size, snake_size).colliderect(pygame.Rect(food_x, food_y, food_size, food_size)):
        eat_sound.play()  # Play eating sound
        food_x = random.randint(0, (WIDTH - food_size) // 20) * 20
        food_y = random.randint(0, (HEIGHT - food_size) // 20) * 20
        snake_length += 1  # Grow the snake
        score += 10  # Increase score
        snake_speed += 1  # Make the game harder
    
    # Update the snake body
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        snake_body.pop(0)
    
    if (snake_x, snake_y) in snake_body[:-1]:  # Check if the snake bites itself
        game_over = True
    
    # Draw the food and snake
    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size), border_radius=5)
    for i, segment in enumerate(snake_body):
        color = (0, 255 - (i * 5), 0)  # Gradient effect on snake
        pygame.draw.rect(screen, color, (segment[0], segment[1], snake_size, snake_size), border_radius=5)
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(10 + score // 10)  # Control speed

cap.release()
pygame.quit()
