import pygame as g
from Common import Appearance as CA, Color, State, Font as CF
from Render import RenderButton, RenderTitle, RenderPng, RenderContent, RenderPlayer, RenderArticle
from MyLog import MyLog

class GameSystem:
    
    def __init__(self) -> None:
        self.title = CF.TITLE_NAME
        self.width = CA.SCREEN_WIDTH
        self.height = CA.SCREEN_HEIGHT
        self.screen = g.display.set_mode((CA.SCREEN_WIDTH, CA.SCREEN_HEIGHT))
        g.display.set_caption(CF.TITLE_NAME)
        self.clock = g.time.Clock()
        self.fps = CA.FPS
        
        self.state = State.GAME_STATE.GAME_INDEX
        self.previous_state = None  
        
        self.start_time = 0.0
        self.cur_time = 0.0
        self.is_timestart = False
    
        self.rb = RenderButton.RenderButton()
        self.rt = RenderTitle.RenderTitle()
        self.rp = RenderPng.RenderPng()
        self.rc = RenderContent.RenderContent()
        self.rpl = RenderPlayer.RenderPlayer()
        self.ra = RenderArticle.RenderArticle() 
        
        self.game_data = None
        
    def Run(self):
      
        while self.state != State.GAME_STATE.GAME_EXIT_FORMAL and self.state is not None:
            
            if self.state != self.previous_state:
                self.__OnStateEnter(self.state, self.previous_state)
                self.previous_state = self.state

            # 获取帧间隔时间
            dt = self.clock.tick(self.fps) / 1000.0
            
            for event in g.event.get():
                if event.type == g.QUIT:
                    self.state = State.GAME_STATE.GAME_EXIT_FORMAL
                    continue
                
                self.__HandleEvent(event)
            
            self.__UpdateState(dt)
                
            self.__Render(dt)
            
        # 游戏结束，清理资源
        self.__Quit()
        
    def __OnStateEnter(self, new_state, old_state):
   
        if new_state == State.GAME_STATE.GAME_RUNNING:
            self.ra.Reset()
            self.rpl.StartTyping(self.ra)
            self.is_timestart = True
            self.start_time = g.time.get_ticks()
            
        elif new_state == State.GAME_STATE.GAME_REPORT:
            self.is_timestart = False
            
        elif new_state == State.GAME_STATE.GAME_INDEX:
            self.ra.Reset()
            self.rpl.Reset()

    def __HandleEvent(self, event):
        """
        根据当前状态，分发事件给对应的处理器。
        只处理离散的、一次性的事件。
        """
        if self.state == State.GAME_STATE.GAME_RUNNING:
            self.state = self.rpl.HandleEvent(event, self.state)
            return
        
        if self.state == State.GAME_STATE.GAME_REPORT:
            MyLog.MyLog("in reposrtstate")
            self.state = self.rb.HandleEvent(event, self.state)
            return 

        if self.state in [State.GAME_STATE.GAME_INDEX, State.GAME_STATE.GAME_INSTRUCTION, State.GAME_STATE.GAME_ARTICLE]:
            self.state = self.rb.HandleEvent(event, self.state)
            return

    def __UpdateState(self, dt):
        if self.state == State.GAME_STATE.GAME_RUNNING:
            self.rpl.UpdateState(dt)
    
    def __Render(self, dt):
        self.cur_time = g.time.get_ticks()
        
        if self.state in [State.GAME_STATE.GAME_INDEX, State.GAME_STATE.GAME_INSTRUCTION, State.GAME_STATE.GAME_ARTICLE, State.GAME_STATE.GAME_REPORT]:
            self.screen.fill(Color.BACKGROUND_COLOR)
            self.rb.Render(self.screen, self.state)
            self.rt.Render(self.screen, self.state)
            self.rc.Render(self.screen, self.state, is_ready=self.ra.is_ready)
        elif self.state == State.GAME_STATE.GAME_RUNNING:
            player_speed, mock_current_cps, current_lane_index, right_num = self.rpl.GetInfo()
            scroll_dx_this_frame = -player_speed * dt
            
            elapsed_seconds = (self.cur_time - self.start_time) / 1000.0 if self.is_timestart else 0
            cpm = (right_num / elapsed_seconds) * 60 if elapsed_seconds > 0 else 0
            
            self.rp.Render(self.screen, scroll_dx_this_frame, self.state)
            self.rc.Render(self.screen, self.state, player_speed, mock_current_cps, current_lane_index, cpm)
            self.rpl.Render(self.screen, self.state)
            self.ra.Render(self.screen)
            self.rb.Render(self.screen, self.state)
        
        if self.state == State.GAME_STATE.GAME_ARTICLE_CHOOSING:
            if self.ra.LoadAndProcess():
                self.state = State.GAME_STATE.GAME_ARTICLE
            else:
                self.state = State.GAME_STATE.GAME_ARTICLE
            
        g.display.flip()
    
    def __Quit(self):
        """
        清理并退出游戏 (保留)
        """
        g.quit()

