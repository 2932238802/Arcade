from Common import Color,Font,Appearance

import MyLog
import MyLog.MyLog

class Score:
    
    def Draw(self,player_speed,mock_current_cps,current_lane_index,right_num,screen):
        speed_text_surf = Font.SCORE_FONT.render(f"{Font.SCORE_SPEED_CONTENT} {player_speed:.0f}(游戏速度)", True, Color.SCORE_COLOR)
        cps_text_surf = Font.SCORE_FONT.render(f"{Font.SCORE_CPS_CONTENT} {mock_current_cps:.1f}(速度加成)", True, Color.SCORE_COLOR)
        right_num_surf = Font.SCORE_FONT.render(f"{Font.SCORE_IRGHTNUM_CONTENT} {right_num:0.0f}(正确次数/分钟)", True, Color.SCORE_COLOR)
        lane_text_surf = Font.SCORE_FONT.render(f"{Font.SCORE_LANE_CONTENT} {current_lane_index}(道路位置)", True, Color.SCORE_COLOR)
        instruction =Font.SCORE_FONT.render(f"{Font.SCORE_INSTRUCTION_CONTENT}", True, Color.SCORE_COLOR) 
        
        screen.blit(speed_text_surf, (Font.SCORE_SPEED_X, Font.SCORE_SPEED_Y))
        screen.blit(cps_text_surf, (Font.SCORE_CPS_X, Font.SCORE_CPS_Y))
        screen.blit(right_num_surf, (Font.SCORE_RIGHTNUM_X, Font.SCORE_RIGHTNUM_Y))
        screen.blit(lane_text_surf, (Font.SCORE_LANE_X, Font.SCORE_LANE_Y))
        screen.blit(instruction, (Font.SCORE_INSTRUCTION_X, Font.SCORE_INSTRUCTION_Y))
        
class ScoreFactory():
    
    @staticmethod
    def GetScore():
        return Score()
    
    
