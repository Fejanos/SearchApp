import pygame               # Grafikus könyvtár

CELL_SIZE = 60              # Minden cella 60x60 px
# Különböző RGB színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (170, 170, 170)
BLUE = (50, 50, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)


# =========================================== Menü metódus ===========================================
def show_menu():
    pygame.init()  # pygame indítása
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Válassz algoritmust")

    font = pygame.font.SysFont(None, 36)
    dfs_rect = pygame.Rect(50, 80, 120, 50)
    bfs_rect = pygame.Rect(230, 80, 120, 50)

    clicked_dfs = False
    clicked_bfs = False

    while True:
        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # DFS gomb logika
        if dfs_rect.collidepoint(mouse_pos):
            dfs_color = RED if mouse_click[0] else GREEN
            if mouse_click[0]:
                clicked_dfs = True
        else:
            dfs_color = WHITE

        # BFS gomb logika
        if bfs_rect.collidepoint(mouse_pos):
            bfs_color = RED if mouse_click[0] else GREEN
            if mouse_click[0]:
                clicked_bfs = True
        else:
            bfs_color = WHITE

        # Gombok és szövegek kirajzolása
        pygame.draw.rect(screen, dfs_color, dfs_rect)
        pygame.draw.rect(screen, bfs_color, bfs_rect)

        dfs_text = font.render("DFS", True, BLACK)
        bfs_text = font.render("BFS", True, BLACK)

        screen.blit(dfs_text, (dfs_rect.x + 35, dfs_rect.y + 10))
        screen.blit(bfs_text, (bfs_rect.x + 35, bfs_rect.y + 10))

        title = font.render("Melyik algoritmust szeretnéd?", True, WHITE)
        screen.blit(title, (30, 20))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if clicked_dfs:
            pygame.time.wait(200)
            pygame.quit()
            return "dfs"
        elif clicked_bfs:
            pygame.time.wait(200)
            pygame.quit()
            return "bfs"
# =========================================== Menü metódus VÉGE ===========================================



# =========================================== Vizuális keresés metódus ===========================================
def visualize_stepwise(maze, visited, path, start, goal):
    rows, cols = len(maze), len(maze[0])
    pygame.init()
    screen = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE))
    pygame.display.set_caption("Keresés lépésenként")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    index = 0
    running = True

    while running:
        screen.fill(WHITE)

        for y in range(rows):
            for x in range(cols):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pos = (y, x)

                # szín logika
                if maze[y][x] == '#':
                    color = BLACK
                elif pos == start:
                    color = GREEN
                elif pos == goal:
                    color = RED
                elif index < len(visited) and pos == visited[index]:
                    color = ORANGE
                elif pos in visited[:index]:
                    color = GRAY
                else:
                    color = WHITE

                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (50, 50, 50), rect, 1)

                # kezdő/cél betűk
                if pos == start:
                    text = font.render("A", True, BLACK)
                    screen.blit(text, (x * CELL_SIZE + 12, y * CELL_SIZE + 10))
                elif pos == goal:
                    text = font.render("B", True, WHITE)
                    screen.blit(text, (x * CELL_SIZE + 12, y * CELL_SIZE + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and index < len(visited) - 1:
                    index += 1
                elif event.key == pygame.K_LEFT and index > 0:
                    index -= 1

        clock.tick(30)

    pygame.quit()

# =========================================== Vizuális keresés metódus vége ===========================================
