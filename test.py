import pygame
import random

# --- 初始化 Pygame ---
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lane Runner Demo")
clock = pygame.time.Clock()
FPS = 60

# --- 颜色 ---
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN_PLAYER = (0, 200, 0)
GRASS_GREEN = (50, 150, 50)
EARTH_BROWN = (139, 119, 74) # 土地颜色，之前叫 EARTH_BROWN，改个名
ROAD_GREY = (80, 80, 80)   # 道路颜色
DEBUG_RED = (255,0,0)

# --- 游戏参数 ---
TILE_SIZE = 40 # 每个背景方块的大小
NUM_ROWS = SCREEN_HEIGHT // TILE_SIZE
NUM_COLS = SCREEN_WIDTH // TILE_SIZE + 2 # 多两列用于平滑滚动

# 道路定义 (基于行索引, 0-indexed from top)
# 假设屏幕高600, TILE_SIZE 40, 则有15行 (0-14)
# 我们选中间的三行作为道路
ROAD_START_ROW = NUM_ROWS // 2 - 1
LANE_ROW_INDICES = [ROAD_START_ROW, ROAD_START_ROW + 1, ROAD_START_ROW + 2]

# --- 玩家类 ---
class Player:
    def __init__(self, screen_x_ratio=0.25): # Y位置由道路决定
        self.screen_fixed_x = SCREEN_WIDTH * screen_x_ratio
        
        self.logical_forward_velocity = 0.0
        self.logical_forward_acceleration = 0.0
        self.typing_acceleration_factor = 100.0
        self.max_logical_forward_speed = 500.0 
        self.drag_factor = 0.90
        self.min_speed_to_stop = 1.0

        self.size = TILE_SIZE * 0.8 # 玩家大小略小于一个瓷砖
        self.color = GREEN_PLAYER

        # 道路相关
        self.lane_y_centers = [(r + 0.5) * TILE_SIZE for r in LANE_ROW_INDICES]
        self.current_lane_index = 1 # 默认在中间道路 (索引1)
        self.screen_pos_y = self.lane_y_centers[self.current_lane_index]
        
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = (self.screen_fixed_x, self.screen_pos_y)

    def update_logical_speed(self, dt, typing_cps):
        # (与之前版本相同)
        if typing_cps > 0:
            self.logical_forward_acceleration = self.typing_acceleration_factor * typing_cps
        else:
            self.logical_forward_acceleration = 0.0
        self.logical_forward_velocity += self.logical_forward_acceleration * dt
        if self.logical_forward_acceleration == 0 and self.logical_forward_velocity != 0:
            self.logical_forward_velocity *= (self.drag_factor ** dt)
            if abs(self.logical_forward_velocity) < self.min_speed_to_stop:
                self.logical_forward_velocity = 0.0
        if abs(self.logical_forward_velocity) > self.max_logical_forward_speed:
            self.logical_forward_velocity = self.max_logical_forward_speed * \
                                            (1 if self.logical_forward_velocity > 0 else -1)

    def switch_lane(self, direction): # direction: -1 for up, 1 for down
        self.current_lane_index += direction
        self.current_lane_index = max(0, min(self.current_lane_index, len(self.lane_y_centers) - 1))
        self.screen_pos_y = self.lane_y_centers[self.current_lane_index]
        self.rect.centery = self.screen_pos_y
            
    def get_current_forward_speed(self):
        return self.logical_forward_velocity

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# --- 背景列类 ---
class BackgroundColumn:
    def __init__(self, col_index, initial_x_offset=0):
        self.col_index_in_grid = col_index # 这个列在概念上的网格中的索引
        self.x = col_index * TILE_SIZE + initial_x_offset
        self.tiles_color = [] # 存储这一列中每个瓷砖的颜色
        self.generate_tiles()

    def generate_tiles(self):
        self.tiles_color = []
        for r in range(NUM_ROWS):
            if r in LANE_ROW_INDICES:
                self.tiles_color.append(ROAD_GREY)
            else:
                self.tiles_color.append(random.choice([GRASS_GREEN, EARTH_BROWN]))
    
    def update_x(self, dx): # dx是这一帧x方向的位移
        self.x += dx # 注意：背景向左移动，所以dx通常是负的
        
        # 如果这列完全移出屏幕左侧
        if self.x + TILE_SIZE < 0:
            self.x += NUM_COLS * TILE_SIZE # 将其移动到整个可见网格的最右侧
            self.generate_tiles() # 重新生成瓷砖内容，使其看起来像是新的一列

    def draw(self, surface):
        for r, color in enumerate(self.tiles_color):
            pygame.draw.rect(surface, color, (round(self.x), r * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            # pygame.draw.rect(surface, BLACK, (round(self.x), r * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1) # 可选：绘制网格线


# --- 游戏对象和变量 ---
player = Player(screen_x_ratio=0.25)

background_columns = []
for i in range(NUM_COLS):
    background_columns.append(BackgroundColumn(col_index=i))

# --- 模拟打字速度 ---
mock_current_cps = 0.0 

# --- 游戏主循环 ---
running = True
world_x_offset = 0.0 # 用一个总的偏移量来控制所有列的精确位置

while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mock_current_cps += 2.5
            if event.key == pygame.K_BACKSPACE:
                mock_current_cps = max(0, mock_current_cps - 4.0)
            
            if event.key == pygame.K_UP:
                player.switch_lane(-10)
            if event.key == pygame.K_DOWN:
                player.switch_lane(10)
    
    if mock_current_cps > 0:
        mock_current_cps = max(0, mock_current_cps - 4.0 * dt)

    # --- 更新游戏状态 ---
    player.update_logical_speed(dt, mock_current_cps)
    player_speed = player.get_current_forward_speed()

    # 更新背景列的位置
    # 背景向左移动的距离是 player_speed * dt
    scroll_dx_this_frame = -player_speed * dt 
    
    for col in background_columns:
        col.update_x(scroll_dx_this_frame)

    # --- 渲染 ---
    screen.fill(BLACK) # 如果有缝隙，用黑色填充

    # 绘制背景列
    for col in background_columns:
        col.draw(screen)
            
    player.draw(screen) # 玩家在最前景

    font = pygame.font.SysFont(None, 30)
    speed_text_surf = font.render(f"Speed: {player_speed:.0f}", True, WHITE)
    cps_text_surf = font.render(f"CPS: {mock_current_cps:.1f}", True, WHITE)
    lane_text_surf = font.render(f"Lane: {player.current_lane_index}", True, WHITE)
    screen.blit(speed_text_surf, (10, 10))
    screen.blit(cps_text_surf, (10, 40))
    screen.blit(lane_text_surf, (10, 70))

    pygame.display.flip()

pygame.quit()
