
from Model import Png
from Common import Appearance


class RenderPng:
    
    @staticmethod
    def RenderBackground(screen):
        
        background = Png.Png.Load(Appearance.START_PNG_PATH)
        
        screen.blit(background,
                    (0, 0),
                    (0, 0, Appearance.SCREEN_WIDTH, 
                    Appearance.SCREEN_HEIGHT))
        
        
        
        
    