import tkinter as tk
from tkinter import filedialog
import os
import pygame as g
from Factory import ArticleFactory 
from Common import Color, Font, State

class RenderArticle:
    def __init__(self) -> None:
        self.article_processor = ArticleFactory.ArticleFactory.GetArticle()
        self.font_main = Font.ARTICLE_FONT
        self.font_typed = Font.ARTICLE_FONT_TYPED 
        
        self.segments = []
        self.segment_index = 0
        self.char_index = 0
        
        self.is_ready = False
        self.is_finished = False

    def LoadAndProcess(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            title="请选择打字练习文件 (.txt)",
            filetypes=[("文本文档", "*.txt")]
        )

        if not file_path:
            print("用户取消了选择")
            self.is_ready = False
            return False

        if not file_path.lower().endswith(".txt"):
            print(f"错误：请选择一个 .txt 文件您选择了: {file_path}")
            self.is_ready = False
            return False

        file_name = os.path.basename(file_path)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_text_content = f.read()

            if not raw_text_content.strip():
                print(f"错误: TXT文件 '{file_name}' 为空或不包含有效文本")
                self.is_ready = False
                return False

            # 获得分割好的 文章数组
            typing_segments = self.article_processor.SmartSplitText(raw_text_content)

            if not typing_segments:
                print(f"错误: 未能从TXT文件 '{file_name}' 中分割出有效的打字片段")
                self.is_ready = False
                return False
                
            # 所有检查都通过了，现在更新状态
            self.segments = typing_segments
            self.segment_index = 0
            self.char_index = 0
            self.is_ready = True
            self.is_finished = False
            print(f"文件 '{file_name}' 内容已成功分割成 {len(self.segments)} 个片段")
            
            return True

        except Exception as e:
            print(f"加载或处理文件 {file_path} 时发生未知错误: {e}")
            self.is_ready = False
            return False

    # 获得当前的
    def GetCurrentTargetChar(self):
        if self.is_finished or not self.is_ready:
            return None
        
        current_segment = self.segments[self.segment_index]
        if self.char_index < len(current_segment):
            return current_segment[self.char_index]
        return None

    def AdvanceChar(self):
        # 前进一个
        # 字符
        self.char_index += 1
        
        if self.char_index >= len(self.segments[self.segment_index]):
            return self.AdvanceSegment()
        
        return True

    def AdvanceSegment(self):
        self.segment_index += 1
        self.char_index = 0
        
        if self.segment_index >= len(self.segments):
            self.is_finished = True
            print("恭喜！所有文章片段都已完成！")
            self.segment_index = 0
            self.char_index = 0
            return False
        
        print(f"进入下一片段: {self.segments[self.segment_index]}")
        return True

    def Render(self, screen):
        
        if not self.is_ready or self.is_finished:
            return

        current_segment = self.segments[self.segment_index]
        
        typed_text = current_segment[:self.char_index]
        untyped_text = current_segment[self.char_index:]

        surface_typed = self.font_main.render(typed_text, True, Color.TEXT_COLOR_TYPED)
        surface_untyped = self.font_main.render(untyped_text, True, Color.TEXT_COLOR_UNTYPED)

        screen_rect = screen.get_rect()
        total_width = surface_typed.get_width() + surface_untyped.get_width()
        
        start_x = screen_rect.centerx - total_width / 2
        
        rect_typed = surface_typed.get_rect(topleft=(start_x, 650))
        rect_untyped = surface_untyped.get_rect(topleft=(rect_typed.right, 650))
        
        screen.blit(surface_typed, rect_typed)
        screen.blit(surface_untyped, rect_untyped)

        
    def Reset(self):
        if self.is_ready: 
            self.segment_index = 0
            self.char_index = 0
            self.is_finished = False
        else:
            pass