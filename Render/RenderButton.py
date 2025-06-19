
from Factory import ButtonFactory
from Common import Appearance,Color,Font,State
from MyLog import MyLog

import pygame

# 开始位置
START_Y = Appearance.SCREEN_HEIGHT // 2 - Appearance.BUTTON_BEGIN_HEIGHT

class RenderButton:
    
    def __init__(self) -> None:
        self.__start_button = ButtonFactory.ButtonFactory.GetButton(
                Font.TITILE_GAMESTRAT_1,
                (Appearance.SCREEN_WIDTH - Appearance.BUTTON_BEGIN_WIDTH) // 2,
                START_Y,
                Appearance.BUTTON_BEGIN_WIDTH, Appearance.BUTTON_BEGIN_HEIGHT,
                Color.BUTTON_BEGIN_COLOR, Color.BUTTON_BEGIN_HOVER_COLOR, Font.BUTTON_BEGIN_FONT,
                action_out="StartGame"
            )

        self.__instructions_button = ButtonFactory.ButtonFactory.GetButton(
            Font.TITILE_GAMESTRAT_2,
            (Appearance.SCREEN_WIDTH  - Appearance.BUTTON_BEGIN_WIDTH) // 2,
            START_Y + Appearance.BUTTON_BEGIN_HEIGHT + Appearance.BUTTON_BEGIN_SPACING,
            Appearance.BUTTON_BEGIN_WIDTH, Appearance.BUTTON_BEGIN_HEIGHT,
            Color.BUTTON_BEGIN_COLOR, Color.BUTTON_BEGIN_HOVER_COLOR, Font.BUTTON_BEGIN_FONT,
            action_out="ShowInstructions"
        )

        self.__exit_button = ButtonFactory.ButtonFactory.GetButton(
            Font.TITILE_GAMESTRAT_3,
            (Appearance.SCREEN_WIDTH  - Appearance.BUTTON_BEGIN_WIDTH) // 2,
            START_Y + 2 * (Appearance.BUTTON_BEGIN_HEIGHT + Appearance.BUTTON_BEGIN_SPACING),
            Appearance.BUTTON_BEGIN_WIDTH, Appearance.BUTTON_BEGIN_HEIGHT,
            Color.BUTTON_BEGIN_COLOR, Color.BUTTON_BEGIN_HOVER_COLOR,Font.BUTTON_BEGIN_FONT,
            action_out="ExitGame"
        )
        
        self.__return_index_button = ButtonFactory.ButtonFactory.GetButton(
            text_out = Font.INSTURCTION_BUTTON_CONTENT, 
            x = Appearance.INSTRUCTION_X,
            y = Appearance.INSTRUCTION_Y,
            width = Appearance.INSTRUCTION_RETURN_WIDTH, 
            height = Appearance.INSTRUCTION_RETURN_HEIGHT,
            color_out= Color.INSTRUCTION_RETURN_COLOR, 
            hover_color_out =Color.INSTRUCTION_RETURN_HOVER_COLOR,
            font_out= Font.INSTRUCTION_BUTTON_CONTENT_FONT,
            action_out="ReturnIndex"
        )
        
        self.__article_choose_button = ButtonFactory.ButtonFactory.GetButton(
            text_out = Font.ARTICLE_CHOOSE_BUTTON_CONTENT, 
            x = Appearance.ARTICLE_CHOOSE_BUTTON_X,
            y = Appearance.ARTICLE_CHOOSE_BUTTON_Y,
            width = Appearance.ARTICLE_CHOOSE_BUTTON_WIDTH, 
            height = Appearance.ARTICLE_CHOOSE_BUTTON_HEIGHT,
            color_out = Color.ARTICLE_CHOOSE_BUTTON_COLOR, 
            hover_color_out = Color.ARTICLE_CHOOSE_BUTTON_COLOR_HOVER,
            font_out= Font.ARTICLE_CHOOSE_BUTTON_FONT,
            action_out="ChooseArticle"
        )
        
        self.__article_choose_over_button = ButtonFactory.ButtonFactory.GetButton(
            text_out = Font.ARTICLE_CHOOSEOVER_START_CONTENT, 
            x = Appearance.ARTICLE_CHOOSEOVER_START_X,
            y = Appearance.ARTICLE_CHOOSEOVER_START_Y,
            width = Appearance.ARTICLE_CHOOSEOVER_START_WIDTH, 
            height = Appearance.ARTICLE_CHOOSEOVER_START_HEIGHT,
            color_out = Color.ARTICLE_CHOOSEOVER_START__COLOR, 
            hover_color_out = Color.ARTICLE_CHOOSEOVER_START__COLOR_HOVER,
            font_out= Font.ARTICLE_CHOOSEOVER_START_FONT,
            action_out="GameStart"
        )
        
        # 重开
        self.__rebegin_button = ButtonFactory.ButtonFactory.GetButton(
            text_out = Font.REBUGIN_BUTTON_CONTENT, 
            x = Appearance.REBUGIN_BUTTON_START_X,
            y = Appearance.REBUGIN_BUTTON_START_Y,
            width = Appearance.REBUGIN_BUTTON_START_WIDTH, 
            height = Appearance.REBUGIN_BUTTON_START_HEIGHT,
            color_out = Color.REBUGIN_BUTTON_COLOR, 
            hover_color_out = Color.REBUGIN_BUTTON_COLOR_HOVER,
            font_out= Font.REBUGIN_BUTTON_FONT,
            action_out="GameReStart"
        )
        
        self.game_index_buttons = [self.__start_button,self.__instructions_button,self.__exit_button]
        self.article_buttons = [self.__article_choose_over_button,self.__article_choose_button]
        self.generate_report = [self.__return_index_button,self.__rebegin_button]
        
        
    def Render(self,screen,state):
        # MyLog.MyLog(f"[debug] Render 进入 state:{state}")
            
        # MyLog.MyLog("[debug] Render 渲染按钮")
        
        if state == State.GAME_STATE.GAME_INDEX:
            for button in self.game_index_buttons:
                button.Draw(screen)
        
        if state in [State.GAME_STATE.GAME_INSTRUCTION  ,  State.GAME_STATE.GAME_ARTICLE] :
            self.__return_index_button.Draw(screen)
            
        if state == State.GAME_STATE.GAME_ARTICLE:
            for button in self.article_buttons:
                button.Draw(screen)
        
        if state == State.GAME_STATE.GAME_REPORT:
            for button in  self.generate_report:
                button.Draw(screen)
            
    def HandleEvent(self,event,state):
        
        # 其实要根据游戏状态进行处理
        # TODO: 这里要根据游戏状态
        # state 就是外部游戏状态
        
        if state == State.GAME_STATE.GAME_INDEX:
            for button in self.game_index_buttons:
                action = button.HandleEvent(event)
                
                if action == "ExitGame":
                    return State.GAME_STATE.GAME_EXIT_FORMAL
                
                if action == "ShowInstructions":
                    
                    # 渲染Instruction
                    # MyLog.MyLog("[debug] action == `ShowInstructions`")
                    return State.GAME_STATE.GAME_INSTRUCTION
                
                if action == "StartGame":
                    
                    return State.GAME_STATE.GAME_ARTICLE
                    
            return State.GAME_STATE.GAME_INDEX
        
                
        if state == State.GAME_STATE.GAME_INSTRUCTION:
            action = self.__return_index_button.HandleEvent(event)
            if action == "ReturnIndex":
                return State.GAME_STATE.GAME_INDEX
            return State.GAME_STATE.GAME_INSTRUCTION
        
        if state == State.GAME_STATE.GAME_ARTICLE:
        
            action = self.__article_choose_button.HandleEvent(event)
            # MyLog.MyLog(f"action = {action}")

            if action == "ChooseArticle":
                # MyLog.MyLog(f"action = {action}")
                return State.GAME_STATE.GAME_ARTICLE_CHOOSING
            
            if self.__article_choose_over_button.HandleEvent(event) == "GameStart":
                
                return State.GAME_STATE.GAME_RUNNING
            
            if self.__return_index_button.HandleEvent(event) == "ReturnIndex":
                return State.GAME_STATE.GAME_INDEX
            
            return State.GAME_STATE.GAME_ARTICLE
        
        if state == State.GAME_STATE.GAME_REPORT:
            
            for button in self.generate_report:
                action = button.HandleEvent(event)
                if action == "ReturnIndex":
                    return State.GAME_STATE.GAME_INDEX
                if action == "GameReStart":
                    return State.GAME_STATE.GAME_RUNNING
            return State.GAME_STATE.GAME_REPORT