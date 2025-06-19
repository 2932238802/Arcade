

from Factory import TitleFactory
from MyLog import MyLog
from Common import State,Font,Color,Appearance
class RenderTitle:
    
    def __init__(self) -> None:
        self.game_start_tile = TitleFactory.TitleFactory.GetTitle(Font.TITLE_NAME_MAX)
        self.instruction_title = TitleFactory.TitleFactory.GetTitle(
            title=Font.INSTURCTION_TITLE,
            color=Color.INSTRUCTION_TITLE_COLOR,
            font = Font.INSTRUCTION_TITLE_FONT,
            centerx = Appearance.SCREEN_WIDTH // 2,
            centery = Font.INSTRUCTION_TITLE_Y
        )
    
    def Render(self,screen,state):
        # 绘制标题
        # TODO: 到时候要根据状态进行渲染 ok了
        # 
        if state == State.GAME_STATE.GAME_INDEX:
            self.game_start_tile.Draw(screen)
            
        elif state == State.GAME_STATE.GAME_INSTRUCTION:
            self.instruction_title.Draw(screen)

        