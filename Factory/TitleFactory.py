from Common import Font,Color,Appearance


class Title:
    def __init__(self,title,color,font,centerx,centery) -> None:
        
        # title_surface 标题的位置和内容
        self.title_surface = \
            font.render(title, True, color)
            # 设置标题
            
        self.pos_size_rect = \
            self.title_surface.get_rect(center=(centerx, centery))
                
    def Draw(self,screen):
        """
        绘制标题
        """
        screen.blit(self.title_surface, self.pos_size_rect)

class TitleFactory:
    @staticmethod
    def GetTitle(title = Font.TITLE_NAME,color=Color.INDEX_TITLE_COLOR,font=Font.TITLE_FONT,centerx=Appearance.SCREEN_WIDTH // 2,centery=Appearance.SCREEN_HEIGHT // 5):
        return Title(title,color,font,centerx,centery)
    
                
                
