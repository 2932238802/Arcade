import pygame
import sys

# --- 初始化 Pygame ---
pygame.init()

# --- 常量 ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


# 颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)
BUTTON_COLOR = (100, 150, 200)
BUTTON_HOVER_COLOR = (150, 200, 250)
TEXT_COLOR = WHITE

# 字体
try:
    # 尝试加载一个常用的中文字体，如果系统中没有，会回退到None（默认字体）
    # 你可以替换为你喜欢的字体文件路径，例如 "your_font.ttf"
    TITLE_FONT = pygame.font.Font("simhei.ttf", 72) # 黑体
    BUTTON_FONT = pygame.font.Font("simhei.ttf", 40)
    INSTRUCTION_FONT = pygame.font.Font("simhei.ttf", 24)
    
except pygame.error:
    print("警告：找不到 simhei.ttf 字体，将使用默认字体。中文可能无法正常显示。")
    TITLE_FONT = pygame.font.Font(None, 72)
    BUTTON_FONT = pygame.font.Font(None, 40)
    INSTRUCTION_FONT = pygame.font.Font(None, 24)


# --- 屏幕设置 ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("警察抓小偷 - 开始菜单")
clock = pygame.time.Clock()

# --- 游戏说明文本 ---
GAME_INSTRUCTIONS = [
    "欢迎来到《警察抓小偷》打字游戏！",
    "",
    "游戏目标：",
    "  作为警察，你需要通过快速准确地打字，",
    "  来追赶并抓捕前方的小偷。",
    "",
    "操作方式：",
    "  - 屏幕上会出现需要输入的文字。",
    "  - 每正确输入一个字，你会前进一小步。",
    "  - 连续正确输入可以积累连击，",
    "    达到一定连击数会触发“开车模式”，",
    "    大幅提升你的追赶速度！",
    "  - 如果输入错误，连击会中断。",
    "",
    "胜利条件：追上并抓住小偷。",
    "失败条件：让小偷领先你太远。",
    "",
    "祝你游戏愉快！",
    "(点击任意处或按Esc返回主菜单)"
]

# --- 按钮类 ---
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, font, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = font
        self.action = action
        self.is_hovered = False

    def draw(self, surface):
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, current_color, self.rect, border_radius=10)

        text_surface = self.font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_hovered: # 左键点击
                if self.action:
                    return self.action # 返回动作标识
        return None

# --- 创建按钮实例 ---
button_width = 280
button_height = 70
button_spacing = 30
start_y = SCREEN_HEIGHT // 2 - button_height # 调整按钮起始Y坐标

start_button = Button(
    "开始游戏",
    (SCREEN_WIDTH - button_width) // 2,
    start_y,
    button_width, button_height,
    BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_FONT,
    action="start_game"
)

instructions_button = Button(
    "游戏说明",
    (SCREEN_WIDTH - button_width) // 2,
    start_y + button_height + button_spacing,
    button_width, button_height,
    BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_FONT,
    action="show_instructions"
)

exit_button = Button(
    "退出游戏",
    (SCREEN_WIDTH - button_width) // 2,
    start_y + 2 * (button_height + button_spacing),
    button_width, button_height,
    BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_FONT,
    action="exit_game"
)

buttons = [start_button, instructions_button, exit_button]

# --- 游戏状态 ---
current_screen = "main_menu" # "main_menu", "instructions"

# --- 主循环 ---
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if current_screen == "main_menu":
            
            for button in buttons:
                action_taken = button.handle_event(event)
                if action_taken:
                    if action_taken == "start_game":
                        print("动作：开始游戏！")
                        # 在这里可以添加跳转到实际游戏循环的代码
                        # running = False # 结束菜单循环，准备进入游戏
                        # game_loop() # 假设你有一个game_loop函数
                        # 为了演示，我们仅打印信息并退出
                        running = False
                        action_result = "START"
                        
                    elif action_taken == "show_instructions":
                        print("动作：显示游戏说明")
                        current_screen = "instructions"
                        
                    elif action_taken == "exit_game":
                        print("动作：退出游戏")
                        running = False
                        action_result = "EXIT"
                        
        elif current_screen == "instructions":
            if event.type == pygame.MOUSEBUTTONDOWN or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                current_screen = "main_menu"

    # --- 绘制 ---
    screen.fill(LIGHT_BLUE) # 背景色

    if current_screen == "main_menu":
        # 绘制标题
        title_surface = TITLE_FONT.render("警察抓小偷", True, BLACK)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_surface, title_rect)

        # 绘制按钮
        for button in buttons:
            button.draw(screen)

    elif current_screen == "instructions":
        # 绘制游戏说明背景板 (可选)
        instruction_panel_rect = pygame.Rect(50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100)
        pygame.draw.rect(screen, GRAY, instruction_panel_rect, border_radius=15)
        pygame.draw.rect(screen, BLACK, instruction_panel_rect, width=3, border_radius=15) # 边框

        # 绘制说明文字
        line_y = instruction_panel_rect.top + 30
        for i, line in enumerate(GAME_INSTRUCTIONS):
            instruction_surface = INSTRUCTION_FONT.render(line, True, BLACK)
            instruction_rect = instruction_surface.get_rect(
                centerx=instruction_panel_rect.centerx, # 居中
                top=line_y + i * (INSTRUCTION_FONT.get_linesize() + 5) # 每行向下偏移
            )
            # 对于较长的行，可以考虑换行逻辑，但这里简化处理
            if instruction_rect.left < instruction_panel_rect.left + 20: # 确保文本在面板内
                 instruction_rect.left = instruction_panel_rect.left + 20

            screen.blit(instruction_surface, instruction_rect)

    pygame.display.flip() # 更新屏幕
    clock.tick(FPS)     # 控制帧率

if 'action_result' in locals():
    if action_result == "START": # type: ignore
        print("主菜单已选择开始游戏。接下来应启动游戏主逻辑。")
    elif action_result == "EXIT": # type: ignore
        print("主菜单已选择退出。")
else:
    print("通过窗口关闭退出。")

pygame.quit()
sys.exit()
