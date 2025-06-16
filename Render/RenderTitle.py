

from Model import Title as t
from MyLog import MyLog
class RenderTitle:
    
    
    def __init__(self) -> None:
         
        # 初始化标题  
        self.title = t.Title()
        
        
    def Draw(self,screen):
        
        screen.blit(self.title.title_surface, self.title.title_rect)
        
        
        