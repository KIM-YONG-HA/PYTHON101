import pygame
import random

# 초기 설정
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0),    # Z
]

# 테트로미노 모양
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
]

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# 그리드 초기화
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# 테트로미노 클래스
class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def collides(self, dx, dy):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    nx, ny = self.x + j + dx, self.y + i + dy
                    if nx < 0 or nx >= GRID_WIDTH or ny >= GRID_HEIGHT or (ny >= 0 and grid[ny][nx]):
                        return True
        return False

    def freeze(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    grid[self.y + i][self.x + j] = self.color

    def drop_to_bottom(self):
        while not self.collides(0, 1):
            self.y += 1
        self.freeze()

# 블록 삭제
def clear_rows():
    global grid
    grid = [row for row in grid if any(cell == 0 for cell in row)]
    while len(grid) < GRID_HEIGHT:
        grid.insert(0, [0 for _ in range(GRID_WIDTH)])

# 게임 실행
def main():
    clock = pygame.time.Clock()
    tetromino = Tetromino()
    running = True
    fall_time = 0
    fall_speed = 500  # 밀리초

    while running:
        screen.fill(BLACK)
        fall_time += clock.get_rawtime()
        clock.tick()

        # 블록 이동
        if fall_time >= fall_speed:
            fall_time = 0
            if not tetromino.collides(0, 1):
                tetromino.y += 1
            else:
                tetromino.freeze()
                clear_rows()
                tetromino = Tetromino()
                if tetromino.collides(0, 0):  # 새로운 블록 생성 시 충돌 -> 게임 종료
                    running = False

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not tetromino.collides(-1, 0):
                    tetromino.x -= 1
                elif event.key == pygame.K_RIGHT and not tetromino.collides(1, 0):
                    tetromino.x += 1
                elif event.key == pygame.K_DOWN and not tetromino.collides(0, 1):
                    tetromino.y += 1
                elif event.key == pygame.K_UP:
                    tetromino.rotate()
                    if tetromino.collides(0, 0):  # 회전 후 충돌 시 원상 복구
                        tetromino.rotate()
                        tetromino.rotate()
                        tetromino.rotate()
                elif event.key == pygame.K_SPACE:  # 스페이스 키로 즉시 바닥으로 이동
                    tetromino.drop_to_bottom()
                    clear_rows()
                    tetromino = Tetromino()
                    if tetromino.collides(0, 0):  # 새로운 블록 생성 시 충돌 -> 게임 종료
                        running = False

        # 그리드 및 테트로미노 렌더링
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        for i, row in enumerate(tetromino.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen,
                        tetromino.color,
                        ((tetromino.x + j) * BLOCK_SIZE, (tetromino.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    )

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
