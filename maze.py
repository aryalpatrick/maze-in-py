import pygame
import sys

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Maze data
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


CELL_SIZE = 40
player_col = 1
player_row = 1
destination_col = len(maze[0]) - 2
destination_row = len(maze) - 2

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[row][col] == 0:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(screen, GREEN, (destination_col * CELL_SIZE, destination_row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_player():
    pygame.draw.circle(screen, RED, (player_col * CELL_SIZE + CELL_SIZE // 2, player_row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if maze[player_row - 1][player_col] == 0:
                    player_row -= 1
            elif event.key == pygame.K_DOWN:
                if maze[player_row + 1][player_col] == 0:
                    player_row += 1
            elif event.key == pygame.K_LEFT:
                if maze[player_row][player_col - 1] == 0:
                    player_col -= 1
            elif event.key == pygame.K_RIGHT:
                if maze[player_row][player_col + 1] == 0:
                    player_col += 1

    screen.fill(WHITE)
    draw_maze()
    draw_player()

    if player_row == destination_row and player_col == destination_col:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render("Congratulations! You reached the destination!", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    pygame.display.update()
