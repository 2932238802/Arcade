from Common import Font,Color,Appearance

class Title:
    def __init__(self) -> None:
        self.title_surface = \
            Font.TITLE_FONT.render(Appearance.TITLE_NAME, True, Color.GRAY)
            
            # 设置标题
        self.title_rect = \
            self.title_surface.get_rect \
                (center=(Appearance.SCREEN_WIDTH // 2, 
                         Appearance.SCREEN_HEIGHT // 4))