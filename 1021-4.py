import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# --- 視窗設定 ---
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍🐍 雙人貪食蛇遊戲")

# --- 顏色設定 ---
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 128, 255)
WHITE = (255, 255, 255)
GRAY = (60, 60, 60)

# --- 字型設定（Windows 中文字體） ---
try:
    font = pygame.font.SysFont("Microsoft JhengHei", 24)
except:
    font = pygame.font.SysFont("SimHei", 24)

# --- 初始資料 ---
snake1 = [(100, 100), (80, 100), (60, 100)]
snake2 = [(400, 300), (420, 300), (440, 300)]
dir1 = "RIGHT"
dir2 = "LEFT"
score1 = 0
score2 = 0
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
clock = pygame.time.Clock()

# --- 顯示分數 ---
def show_score():
    text1 = font.render(f"玩家1分數：{score1}", True, GREEN)
    text2 = font.render(f"玩家2分數：{score2}", True, BLUE)
    screen.blit(text1, (10, 10))
    screen.blit(text2, (WIDTH - 200, 10))

# --- 結束畫面 ---
def game_over(winner_text):
    over = font.render(winner_text, True, RED)
    tip = font.render("按任意鍵重新開始", True, WHITE)
    screen.blit(over, (WIDTH//2 - 100, HEIGHT//2 - 40))
    screen.blit(tip, (WIDTH//2 - 120, HEIGHT//2 + 10))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
    restart_game()

# --- 重新開始 ---
def restart_game():
    global snake1, snake2, dir1, dir2, score1, score2, food
    snake1 = [(100, 100), (80, 100), (60, 100)]
    snake2 = [(400, 300), (420, 300), (440, 300)]
    dir1 = "RIGHT"
    dir2 = "LEFT"
    score1 = 0
    score2 = 0
    food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))

# --- 主迴圈 ---
running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 玩家1（↑↓←→）
            if event.key == pygame.K_UP and dir1 != "DOWN":
                dir1 = "UP"
            elif event.key == pygame.K_DOWN and dir1 != "UP":
                dir1 = "DOWN"
            elif event.key == pygame.K_LEFT and dir1 != "RIGHT":
                dir1 = "LEFT"
            elif event.key == pygame.K_RIGHT and dir1 != "LEFT":
                dir1 = "RIGHT"
            # 玩家2（WASD）
            elif event.key == pygame.K_w and dir2 != "DOWN":
                dir2 = "UP"
            elif event.key == pygame.K_s and dir2 != "UP":
                dir2 = "DOWN"
            elif event.key == pygame.K_a and dir2 != "RIGHT":
                dir2 = "LEFT"
            elif event.key == pygame.K_d and dir2 != "LEFT":
                dir2 = "RIGHT"

    # --- 移動蛇1 ---
    x1, y1 = snake1[0]
    if dir1 == "UP":
        y1 -= CELL_SIZE
    elif dir1 == "DOWN":
        y1 += CELL_SIZE
    elif dir1 == "LEFT":
        x1 -= CELL_SIZE
    elif dir1 == "RIGHT":
        x1 += CELL_SIZE
    new_head1 = (x1, y1)
    snake1.insert(0, new_head1)

    # --- 移動蛇2 ---
    x2, y2 = snake2[0]
    if dir2 == "UP":
        y2 -= CELL_SIZE
    elif dir2 == "DOWN":
        y2 += CELL_SIZE
    elif dir2 == "LEFT":
        x2 -= CELL_SIZE
    elif dir2 == "RIGHT":
        x2 += CELL_SIZE
    new_head2 = (x2, y2)
    snake2.insert(0, new_head2)

    # --- 吃到食物 ---
    if new_head1 == food:
        score1 += 10
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
    else:
        snake1.pop()

    if new_head2 == food:
        score2 += 10
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
    else:
        snake2.pop()

    # --- 撞牆或撞自己 / 撞對方 ---
    if (x1 < 0 or x1 >= WIDTH or y1 < 0 or y1 >= HEIGHT or
        len(snake1) != len(set(snake1)) or new_head1 in snake2):
        game_over("💥 玩家2獲勝！")
    if (x2 < 0 or x2 >= WIDTH or y2 < 0 or y2 >= HEIGHT or
        len(snake2) != len(set(snake2)) or new_head2 in snake1):
        game_over("💥 玩家1獲勝！")

    # --- 繪圖 ---
    screen.fill(GRAY)
    for seg in snake1:
        pygame.draw.rect(screen, GREEN, (*seg, CELL_SIZE, CELL_SIZE))
    for seg in snake2:
        pygame.draw.rect(screen, BLUE, (*seg, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    show_score()
    pygame.display.flip()

pygame.quit()
