
from Model import Button as btn
from Common import Appearance,Color,Font

START_Y = Appearance.SCREEN_HEIGHT // 2 - Appearance.BUTTON_BEGIN_HEIGHT

class RenderGameStartButton():
    

    
    def __init__(self) -> None:
        
        """
        渲染 按钮
        """
        
        
        start_button = btn.Button(
            "开始游戏",
            (Appearance.SCREEN_WIDTH - Appearance.BUTTON_BEGIN_WIDTH) // 2,
            START_Y,
            Appearance.BUTTON_BEGIN_WIDTH, Appearance.BUTTON_BEGIN_HEIGHT,
            Color.BUTTON_BEGIN_COLOR, Color.BUTTON_BEGIN_HOVER_COLOR, Font.BUTTON_BEGIN_FONT,
            action="StartGame"
        )

        instructions_button = btn.Button(
            "游戏说明",
            (Appearance.SCREEN_WIDTH  - Appearance.BUTTON_BEGIN_WIDTH) // 2,
            START_Y + Appearance.BUTTON_BEGIN_HEIGHT + Appearance.BUTTON_BEGIN_SPACING,
            Appearance.BUTTON_BEGIN_WIDTH, Appearance.BUTTON_BEGIN_HEIGHT,
            Color.BUTTON_BEGIN_COLOR, Color.BUTTON_BEGIN_HOVER_COLOR, Font.BUTTON_BEGIN_FONT,
            action="ShowInstructions"
        )

        exit_button = btn.Button(
            "退出游戏",
            (Appearance.SCREEN_WIDTH  - Appearance.BUTTON_BEGIN_WIDTH) // 2,
            START_Y + 2 * (Appearance.BUTTON_BEGIN_HEIGHT + Appearance.BUTTON_BEGIN_SPACING),
            Appearance.BUTTON_BEGIN_WIDTH, Appearance.BUTTON_BEGIN_HEIGHT,
            Color.BUTTON_BEGIN_COLOR, Color.BUTTON_BEGIN_HOVER_COLOR,Font.BUTTON_BEGIN_FONT,
            action="ExitGame"
        )
        
        self.buttons = [start_button,instructions_button,exit_button]
    
    # 需要窗口
    def Draw(self,screen):
        for button in self.buttons:
            button.Draw(screen)         # type: ignore
    
    
    