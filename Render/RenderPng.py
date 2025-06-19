
from Factory import PngFactory as PF
from Common import Appearance,Color,State
import random,pygame


class BackgroundColumn:
    def __init__(self, col_index, initial_x_offset=0):
        
        # 这个列在概念上的网格中的索引
        self.col_index_in_grid = col_index
        self.x = col_index * Appearance.TILE_SIZE + initial_x_offset
        
        # 存储这一列中每个瓷砖的颜色
        self.tiles_color = [] 
        self.GenerateTiles()

    def GenerateTiles(self):
        self.tiles_color = []
        for r in range(Appearance.NUM_ROWS):
            if r in Appearance.LANE_ROW_INDICES:
                self.tiles_color.append(Color.ROAD_COLOR)
            else:
                self.tiles_color.append(random.choice([Color.GLASS_COLOR, Color.EARTH_COLOR]))
                
    def UpdateX(self, dx):
        self.x += dx 
        
        if self.x + Appearance.TILE_SIZE < 0:
            self.x += Appearance.NUM_COLS_BUFFERED * Appearance.TILE_SIZE
            self.GenerateTiles()

    def Draw(self, surface):
        for r, color in enumerate(self.tiles_color):
            pygame.draw.rect(surface, color, (round(self.x), r * Appearance.TILE_SIZE, Appearance.TILE_SIZE, Appearance.TILE_SIZE))


class RenderPng:
    def __init__(self) -> None:
        self.background_columns = []
        for i in range(Appearance.NUM_COLS_BUFFERED):
            self.background_columns.append(BackgroundColumn(col_index=i))
    
    def RenderPng(self,screen,path):
        
        background = PF.PngFactory.Load(path)
        
        # TODO: 之后这个背景颜色要修x改
        screen.blit(background,
                    (0, 0),
                    (0, 0, Appearance.SCREEN_WIDTH, 
                    Appearance.SCREEN_HEIGHT))
        
    def RenderColorbg(self,screen,state):
        if state == State.GAME_STATE.GAME_RUNNING:
            screen.fill(Color.VERY_PALE_MINT)
 
    def Render(self,screen,scroll_dx_this_frame,state):
        
        if state == State.GAME_STATE.GAME_RUNNING:
            # 更新所有的位置
            for col in self.background_columns:
                col.UpdateX(scroll_dx_this_frame)

            # 如果有缝隙，用黑色填充
            screen.fill(Color.BLACK) 

            # 绘制背景列
            for col in self.background_columns:
                col.Draw(screen)