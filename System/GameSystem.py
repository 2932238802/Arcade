
import pygame as g
from Common import Appearance as CA
from Common import Color

from Render import RenderGameStartButton,RenderTitle,RenderPng

class GameSystem:
    def __init__(self) -> None:
        
        # 设置窗口
        self.title = CA.TITLE_NAME
        self.width = CA.SCREEN_WIDTH
        self.height = CA.SCREEN_HEIGHT
        
        # 设置一下屏幕和标题
        self.screen = g.display.set_mode((CA.SCREEN_WIDTH, CA.SCREEN_HEIGHT))
        g.display.set_caption(CA.TITLE_NAME)
        
        # 设置时钟控制帧率
        self.clock = g.time.Clock()
        self.fps = CA.FPS
        self.running = False
    
    
        # 渲染开始按钮
        
        self.rgsb = RenderGameStartButton.RenderGameStartButton()
        self.rt= RenderTitle.RenderTitle()
        self.rp = RenderPng.RenderPng()
        
    def Run(self):
        """游戏主循环"""
        self.running = True
        while self.running:
            # 处理事件
            for event in g.event.get():
                if event.type == g.QUIT:
                    self.running = False
            
            # # 更新游戏逻辑
            self.__Update()
            
            # # 渲染画面
            # # 控制帧率
            self.__Render()
            self.clock.tick(self.fps)
        
        # 游戏结束，清理资源
        self.__Quit()
        
    def __Update(self):
        """
        
        更新游戏状态
        
        """
        pass
    
    def __Render(self):
        """
        TODO: 统一来渲染游戏界面
        渲染游戏画面
        
        """
        # 渲染开始游戏按钮
        
        self.screen.fill(Color.WHITE)
        # self.rp.RenderBackground(self.screen)
        self.rgsb.Draw(self.screen)
        self.rt.Draw(self.screen)
        g.display.flip()
    
    def __Quit(self):
        """
        
        清理并退出游戏
        
        """
        g.quit()