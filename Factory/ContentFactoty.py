from Common import Font,Color,Appearance


class Content:
    def __init__(self,content,color,font,start_centerx,start_top_y,line_spacing) -> None:
        
        self.surfaces_and_rects = []
        self.font = font
        self.color = color
        self.line_spacing = line_spacing
        
        current_y = start_top_y
        for line_text in content:
            text_surface = self.font.render(line_text, True, self.color)
            text_rect = text_surface.get_rect()
            text_rect.centerx = start_centerx
            text_rect.top = current_y
            self.surfaces_and_rects.append((text_surface, text_rect))
            current_y += self.font.get_linesize() + self.line_spacing
                
    def Draw(self, screen):
        for surface, rect in self.surfaces_and_rects:
            screen.blit(surface, rect)

class ContentFactoty:
    @staticmethod
    def GetContent(content = Font.INSTRUCTION_CONTENT,color=Color.INSTRUCTION_COLOR,font=Font.INSTRUCTION_CONTENT_FONT,start_centerx=Appearance.SCREEN_WIDTH // 2,start_top_y=Font.INSTRUCTION_CONTENT_Y, line_spacing = Font.INSTRUCTION_FONT_LINESPACING):
        return Content(content,color,font,start_centerx,start_top_y,line_spacing)
    
                
                
