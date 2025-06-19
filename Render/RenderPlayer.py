from Factory import PlayerFactory
from Common import State, Appearance as AP,Player               # 假设将常量放在 Appearance 中
import pygame
from MyLog import MyLog

class RenderPlayer:
    def __init__(self) -> None:
        self.player = PlayerFactory.PlayerFactory.GetPlayer()   # 通过工厂获取玩家对象
        self.article_handler = None                             # 文章处理器  在游戏开始时被设置
        self.typing_cps = 0                                     # 打字速度  会随时间衰减
        self.right_num = 0                                      # 记录打字的正确的个数           
        
    def Reset(self):
        self.typing_cps = 0
        self.right_num = 0
        print("RenderPlayer 状态已重置 ")
        
    def Render(self, screen, state):
        if state == State.GAME_STATE.GAME_RUNNING:
            self.player.Draw(screen)

    def StartTyping(self, article_handler):
        self.article_handler = article_handler
        self.Reset() 
        print("RenderPlayer 已准备就绪 开始接收输入 ")

    def HandleEvent(self, event, state):
        """
        处理 Pygame 事件  主要是键盘输入 
        """ 
        
        
        if state != State.GAME_STATE.GAME_RUNNING or self.article_handler is None:
            MyLog.MyLog("Player")
            return state
        

        MyLog.MyLog("Player")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player.SwitchLane(-1)                  # 向上切换赛道
                return State.GAME_STATE.GAME_RUNNING
            elif event.key == pygame.K_DOWN:
                self.player.SwitchLane(1)                   # 向下切换赛道
                return State.GAME_STATE.GAME_RUNNING
            elif event.key == pygame.K_ESCAPE:
                return State.GAME_STATE.GAME_INDEX          # 按下ESC返回主菜单

            if not event.unicode:
                return State.GAME_STATE.GAME_RUNNING

            target_char = self.article_handler.GetCurrentTargetChar()
            
            if target_char:
                if event.unicode == target_char:
                    
                    self.typing_cps += Player.CPS_BOOST_ON_CORRECT
                    self.right_num += 1
                    
                    # 答对了就前进一格
                    self.article_handler.AdvanceChar()
                    
                    if self.article_handler.is_finished:
                        print("文章完成！已自动重置  请继续")
                        return State.GAME_STATE.GAME_REPORT
                        # self.article_handler.GenerateReport()
                else:
                    pass

        return State.GAME_STATE.GAME_RUNNING

    def UpdateState(self, dt):
        if self.typing_cps > 0:
            # 衰减比率
            decay_amount = Player.CPS_DECAY_RATE * dt
            self.typing_cps = max(0, self.typing_cps - decay_amount)
            
        # 更新对应的状态信息
        self.player.Update(dt, self.typing_cps)

    def GetInfo(self):
        return self.player.GetCurrentSpeed(), self.typing_cps, self.player.GetLane(),self.right_num
    
    
    
    
    




