import pygame
import Common.Appearance as CA
import Common.Color as CC

from MyLog import MyLog

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, font, action):
        """_summary_ 按钮初始化
        Args:
            text : 按钮内容
            x : 起始位置 x
            y : 起始位置 y
            width : 宽度 
            height : 高度
            
            color : 颜色
            hover_color : 
            font : _description_
            action : _description_. Defaults to None.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = font
        self.action:str|None = action
        self.is_hovered = False

    def Draw(self, screen):
        """绘画

        Args:
            screen : 会话
        """
        current_color = self.hover_color if self.is_hovered else self.color
        
        # 
        # surface: Surface,         对应的图像和屏幕
        # color: ColorValue,        颜色
        # rect: RectValue,          位置和大小
        # width: int = 0,           变宽厚度
        # border_radius: int = -1   边缘厚度
        pygame.draw.rect(screen, current_color, self.rect, border_radius=CA.GAME_START_BUTTON_BORDER_RADIUS)

        # True antialias (抗锯齿) 参数
        text_screen = self.font.render(self.text, True, CC.TEXT_COLOR)
        
        # MyLog.MyLog(self.text);
        
        text_rect = text_screen.get_rect(center=self.rect.center)
        
        screen.blit(text_screen, text_rect)

    def HandleEvent(self, event):
        """
        处理关于按钮的事件
        """
        if event.type == pygame.MOUSEMOTION:
            # 检测悬停
            self.is_hovered = self.rect.collidepoint(event.pos)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # event.button == 1  是不是鼠标点击
            if event.button == 1 and self.is_hovered: 
                if self.action:
                    return self.action 
        return None
    
class ButtonFactory:
    @staticmethod
    def GetButton(text_out, x, y, width, height, color_out, hover_color_out, font_out, action_out=None):
        return Button(text_out, x, y, width, height, color_out, hover_color_out, font_out, action_out)
