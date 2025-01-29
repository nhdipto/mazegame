import pygame
import sys
import time
import random

pygame.init()

#Screen
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
PLAYER_SIZE = 32
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

#Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Levels
LEVELS = [
    [   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    [   [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]
]

player1_jpg = pygame.image.load('player1.jpg')
player2_jpg = pygame.image.load('player2.jpg')

player1_jpg = pygame.transform.scale(player1_jpg, (PLAYER_SIZE, PLAYER_SIZE))
player2_jpg = pygame.transform.scale(player2_jpg, (PLAYER_SIZE, PLAYER_SIZE))

current_level = 0
MAZE = LEVELS[current_level]

player_x, player_y = 1, 1
goal_x, goal_y = 18, 9

def draw_maze():
    for row in range(len(MAZE)):
        for col in range(len(MAZE[row])):
            if MAZE[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
def show_popup(message):
    font = pygame.font.Font(None, 74)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)


def reset_level():
    global player_x, player_y, goal_x, goal_y
    if current_level == 0:
        player_x, player_y = 1, 1
        goal_x, goal_y = 18, 9
    elif current_level == 1:
        player_x, player_y = 1, 1
        goal_x, goal_y = 18, 9


def next_level():
    global current_level, MAZE, player_x, player_y, goal_x, goal_y, enemies
    current_level += 1
    if current_level < len(LEVELS):
        MAZE = LEVELS[current_level]
        enemies = place_enemies(3,MAZE)
        reset_level()
    else:
        show_popup("You Win!")
        pygame.quit()
        sys.exit()

def character_selection():    
    selected_character = 1
    font = pygame.font.Font(None, 36)

    while True:
        screen.fill(WHITE)
        char1_rect = pygame.Rect(WIDTH // 4 - PLAYER_SIZE // 2, HEIGHT // 2 - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
        char2_rect = pygame.Rect(3 * WIDTH // 4 - PLAYER_SIZE // 2, HEIGHT // 2 - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
        
        screen.blit(player1_jpg, char1_rect.topleft)
        screen.blit(player2_jpg, char2_rect.topleft)
        
        if selected_character == 1:
            pygame.draw.rect(screen, RED, char1_rect, 3)
        else:
            pygame.draw.rect(screen, RED, char2_rect, 3)
        
        text = font.render("Press LEFT/RIGHT to select, ENTER to confirm", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_character = 1
                elif event.key == pygame.K_RIGHT:
                    selected_character = 2
                elif event.key == pygame.K_RETURN:
                    return selected_character

enemies = [(5, 5), (10, 5), (15, 5)]
enemy_speed = 0.2


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move_enemy(enemy_pos):
    x, y = enemy_pos
    random_dir = random.choice(directions)
    new_x = x + random_dir[0]
    new_y = y + random_dir[1]
    
    if 0 <= new_x < COLS and 0 <= new_y < ROWS and MAZE[new_y][new_x] == 0:
        return (new_x, new_y)
    return enemy_pos

level_enemy_positions = {
    0: [(5, 5), (10, 5), (15, 5)],
    1: [(2, 2), (7, 7), (14, 4)],
}



def check_collision():
    player_rect = pygame.Rect(player_x * CELL_SIZE, player_y * CELL_SIZE, PLAYER_SIZE, PLAYER_SIZE)
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0] * CELL_SIZE, enemy[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if player_rect.colliderect(enemy_rect):
            show_popup("Game Over")
            pygame.quit()
            sys.exit()


def valid_enemy_position(x, y, maze):
    if maze[y][x] == 0:
        return True
    return False

def place_enemies(num_enemies, maze):
    enemy_positions = []
    while len(enemy_positions) < num_enemies:
        x = random.randint(0, len(maze[0]) - 1)
        y = random.randint(0, len(maze) - 1)
        
        if valid_enemy_position(x, y, maze) and (x, y) not in enemy_positions:
            enemy_positions.append((x, y))
    
    return enemy_positions



def game_loop(selected_character):
    global player_x, player_y, start_time
    start_time = time.time()
    
    while True:
        screen.fill(WHITE)
        draw_maze()
        if selected_character == 1:
            screen.blit(player1_jpg, (player_x * CELL_SIZE, player_y * CELL_SIZE))
        else:
            screen.blit(player2_jpg, (player_x * CELL_SIZE, player_y * CELL_SIZE))
        
        pygame.draw.rect(screen, GREEN, (goal_x * CELL_SIZE, goal_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        for enemy in enemies:
            pygame.draw.rect(screen, RED, (enemy[0] * CELL_SIZE, enemy[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        
        for i in range(len(enemies)):
            enemies[i] = move_enemy(enemies[i])
        pygame.display.flip()
        check_collision()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                new_x, new_y = player_x, player_y
                if event.key == pygame.K_UP:
                    new_y -= 1
                elif event.key == pygame.K_DOWN:
                    new_y += 1
                elif event.key == pygame.K_LEFT:
                    new_x -= 1
                elif event.key == pygame.K_RIGHT:
                    new_x += 1
                if MAZE[new_y][new_x] == 0:
                    player_x, player_y = new_x, new_y
                if (player_x, player_y) == (goal_x, goal_y):
                    if current_level == 0:
                        show_popup("Level Completed!")
                    next_level()

        pygame.time.delay(100)
selected_character = character_selection()
game_loop(selected_character)
