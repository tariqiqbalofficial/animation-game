import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumping Castle Action")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height
player_speed = 5
player_jump = False
player_jump_height = 10
player_jump_count = 10

# Obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    player_x -= (keys[pygame.K_LEFT] or keys[pygame.K_a]) * player_speed
    player_x += (keys[pygame.K_RIGHT] or keys[pygame.K_d]) * player_speed
    player_jump = keys[pygame.K_SPACE] and not player_jump

    # Player jump
    if player_jump:
        if player_jump_count >= -player_jump_height:
            player_y -= (player_jump_count * abs(player_jump_count)) * 0.5
            player_jump_count -= 1
        else:
            player_jump_count = player_jump_height
            player_jump = False

    # Create obstacles
    if random.randint(1, obstacle_frequency) == 1:
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacle_y = -obstacle_height
        obstacles.append([obstacle_x, obstacle_y])

    # Move obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

    # Remove off-screen obstacles
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < screen_height]

    # Check for collisions
    for obstacle in obstacles:
        if (player_x < obstacle[0] + obstacle_width and
            player_x + player_width > obstacle[0] and
            player_y < obstacle[1] + obstacle_height and
            player_y + player_height > obstacle[1]):
            running = False

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [player_x, player_y, player_width, player_height])
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, [obstacle[0], obstacle[1], obstacle_width, obstacle_height])
    pygame.display.flip()

    # Frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
