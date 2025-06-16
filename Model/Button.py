import pygame
import Common.Appearance as CA
import Common.Color as CC

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, font, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = font
        self.action = action
        self.is_hovered = False

    def Draw(self, surface):
        
        current_color = self.hover_color if self.is_hovered else self.color
        
        pygame.draw.rect(surface, current_color, self.rect, border_radius=CA.GAME_START_BUTTON_BORDER_RADIUS)

        text_surface = self.font.render(self.text, True, CC.TEXT_COLOR)
        
        text_rect = text_surface.get_rect(center=self.rect.center)
        
        surface.blit(text_surface, text_rect)

    def HandleEvent(self, event):
        
        if event.type == pygame.MOUSEMOTION:
            
            self.is_hovered = self.rect.collidepoint(event.pos)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1 and self.is_hovered: 
                
                if self.action:
                    
                    return self.action 
            
        return None