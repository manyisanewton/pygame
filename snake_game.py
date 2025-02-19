import pygame  # Library/framework for making games
import random  #the method is helping  with random food placement

pygame.init()

#  game window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Newton's Snake Game")

# Load sounds
pygame.mixer.init()
eat_sound = pygame.mixer.Sound("/home/newton/FUN PROJECTS/pygame/sounds/eat.wav")
game_over_sound = pygame.mixer.Sound("/home/newton/FUN PROJECTS/pygame/sounds/game_over.wav")

# Load background music
pygame.mixer.music.load("/home/newton/FUN PROJECTS/pygame/sounds/backgroundmusic.mp3")
pygame.mixer.music.play(-1)  # Play music in a loop

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake settings
snake_size = 20  
snake_x = WIDTH // 2  
snake_y = HEIGHT // 2  
snake_speed = 10  
velocity_x = 0  
velocity_y = 0  

# Snake body creation settings
snake_body = [(snake_x, snake_y)]  
snake_length = 3  

# Food  creation
food_size = 20  
food_x = random.randint(0, (WIDTH - food_size) // 20) * 20  
food_y = random.randint(0, (HEIGHT - food_size) // 20) * 20  

# Score  intialization
score = 0  
font = pygame.font.Font(None, 36)  

# Game loop variables
running = True  
paused = False  
clock = pygame.time.Clock()  
game_over = False  

while running:
    screen.fill(BLACK)  # the background color is black
    
    # Check'S if the game is over
    if game_over:
        game_over_sound.play()
        pygame.time.delay(700)
        pygame.mixer.music.stop()
        
        # Display'S the  game over message
        text = font.render(f"Game Over! Final Score: {score} | Press R to Restart", True, WHITE)
        screen.blit(text, (WIDTH // 10, HEIGHT // 2))
        pygame.display.update()
        
        # Wait for user to restart or quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
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
                pygame.mixer.music.play(-1)  
        continue
    
    # Handling  user's input
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
        pause_text = font.render("Game Paused - Press P to Resume", True, WHITE)
        screen.blit(pause_text, (WIDTH // 4, HEIGHT // 2))
        pygame.display.update()
        continue
    
    # Moving  the snake
    snake_x += velocity_x
    snake_y += velocity_y
    
    # Check for collisions
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        game_over = True
    
    # what if the snake eats the food
    if pygame.Rect(snake_x, snake_y, snake_size, snake_size).colliderect(pygame.Rect(food_x, food_y, food_size, food_size)):
        eat_sound.play()
        food_x = random.randint(0, (WIDTH - food_size) // 20) * 20
        food_y = random.randint(0, (HEIGHT - food_size) // 20) * 20
        snake_length += 1  
        score += 10  
        snake_speed += 0.5  
    
    # Updating the snake's body
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        snake_body.pop(0)
    
    if (snake_x, snake_y) in snake_body[:-1]:  
        game_over = True
    
    # Draw the food and snake
    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size), border_radius=10)
    for i, segment in enumerate(snake_body):
        color = (0, 255 - (i * 5), 0)  
        pygame.draw.rect(screen, color, (segment[0], segment[1], snake_size, snake_size), border_radius=5)
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(10 + score // 10)  

pygame.quit()







