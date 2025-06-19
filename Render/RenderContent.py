
from MyLog import MyLog
from Common import State,Font,Color,Appearance
from Factory import ContentFactoty,ScoreFactory

class RenderContent:
    
    def __init__(self) -> None:
        """
        这里的渲染逻辑
        就是文章的内容
        """
        
        self.player_speed = 0.0
        self.mock_current_cps = 0.0
        self.current_lane_index = 0.0
        self.right_num = 0.0
        
        self.content = ContentFactoty.ContentFactoty.GetContent()
        self.score = ScoreFactory.ScoreFactory.GetScore()
        self.choose_success = ContentFactoty.ContentFactoty.GetContent(
            content = ["文件准备就绪啦~"] ,
            start_centerx = Appearance.ARTICLE_CHOOSE_BUTTON_INFO_SUC_X,
            start_top_y =Appearance.ARTICLE_CHOOSE_BUTTON_INFO_SUC_Y
        )
        
        
    
    def Render(self,screen,state,player_speed=0.0,mock_current_cps=0.0,current_lane_index=0.0,right_num=0.0,is_ready=False):
        if state == State.GAME_STATE.GAME_INSTRUCTION:
            self.content.Draw(screen=screen)
        
        if state == State.GAME_STATE.GAME_RUNNING:
            self.score.Draw(player_speed,mock_current_cps,current_lane_index,right_num=right_num,screen=screen)
            
            self.player_speed = player_speed
            self.mock_current_cps = mock_current_cps
            self.current_lane_index = current_lane_index
            self.right_num = right_num

        if state == State.GAME_STATE.GAME_ARTICLE:
            if is_ready == True:
                self.choose_success.Draw(screen=screen)
                
        if state == State.GAME_STATE.GAME_REPORT:
            
            self.report = ContentFactoty.ContentFactoty.GetContent(
                content = [f"平均打字速度是 —— {self.right_num:.1f}"] ,
                start_centerx = Appearance.REPORT_START_X,
                start_top_y =Appearance.REPORT_START_Y)
            
            self.report.Draw(screen=screen)
    
    