
import pygame
import Common.Color 
import Common.Player
from Common import Appearance

class Player:
    def __init__(self) -> None:
        
        self.size = Appearance.TILE_SIZE * Common.Player.PLAYER_SIZE_FACTOR
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.color = Common.Color.PLAYER_COLOR 
        
        # 这个是速度
        self.velocity = 0
        
        # 这个是固定的位置
        self.x_position = Appearance.SCREEN_WIDTH * Common.Player.PLAYER_POSITION_X_RATIO
        
        # 这个是赛道的位置
        self.current_lane_index = 1 
        
        # 这个是加速度
        self.acceleration = 0
        
        # 最小要停止的速度
        self.min_speed_to_stop = Common.Player.MIN_SPEED_TO_STOP
    
        # 道路的位置
        self.lane_y_centers = [(r + 0.5) * Appearance.TILE_SIZE for r in Appearance.LANE_ROW_INDICES]
        
        # 矩形的位置
        self.rect.centerx = int(self.x_position)
        self.rect.centery = int(self.lane_y_centers[self.current_lane_index])

        self.logical_world_distance_covered = 0.0 

    def Draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def Update(self, dt, typing_cps):
        if typing_cps > 0:
            self.acceleration = Common.Player.TYPING_ACCELERATION_FACTOR * typing_cps
        else:
            self.acceleration = 0.0
        
        self.velocity += self.acceleration * dt
        
        # 速度缓慢下降
        if self.acceleration == 0 and self.velocity != 0:
            self.velocity *= (Common.Player.DRAG_FACTOR ** dt) 
            
            # 太小直接没了
            if abs(self.velocity) < self.min_speed_to_stop:
                self.velocity = 0.0
        
        #太大就限制
        if abs(self.velocity) > Common.Player.MAX_LOGICAL_SPEED:
            self.velocity = Common.Player.MAX_LOGICAL_SPEED
        
        self.logical_world_distance_covered += self.velocity * dt

    def SwitchLane(self, direction: int):
        self.current_lane_index += direction
        self.current_lane_index = max(0, min(self.current_lane_index, len(self.lane_y_centers) - 1))
        self.rect.centery = int(self.lane_y_centers[self.current_lane_index])

    def GetCurrentSpeed(self):
        return self.velocity

    def GetLane(self):
        return self.current_lane_index
    
    def Reset(self):
        
        self.velocity = 0
        self.acceleration = 0
        
        self.current_lane_index = 1 
    
class PlayerFactory:
    @staticmethod
    def GetPlayer():
        return Player()
