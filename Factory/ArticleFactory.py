import re
import tkinter as tk
from tkinter import filedialog
import os

class Article:
    
    def __init__(self) -> None:
        pass

    def SmartSplitText(self, text, max_length=25):

        if not text or not text.strip():
            return []
        text = re.sub(r'[ \t\r\f\v]+', ' ', text)
        text = re.sub(r'\n+', '\n', text).strip()

        primary_delimiters = r'([.\n!?])'
        sentences = []
        parts = re.split(primary_delimiters, text)
        for i in range(0, len(parts), 2):
            sentence = parts[i]
            if i + 1 < len(parts):
                sentence += parts[i+1]
            if sentence.strip():
                sentences.append(sentence.strip())

        final_segments = []
        for sentence in sentences:
            if len(sentence) <= max_length:
                final_segments.append(sentence)
                continue

            secondary_delimiters = r'([,;:])'
            clauses = []
            parts = re.split(secondary_delimiters, sentence)
            for i in range(0, len(parts), 2):
                clause = parts[i]
                if i + 1 < len(parts):
                    clause += parts[i+1]
                if clause.strip():
                    clauses.append(clause.strip())
            for clause in clauses:
                if len(clause) <= max_length:
                    final_segments.append(clause)
                    continue
                words = clause.split(' ')
                current_segment = ""
                for word in words:
                    if not word: continue
                    if len(current_segment) + len(word) + 1 > max_length:
                        if current_segment:
                            final_segments.append(current_segment)
                        current_segment = word
                    else:
                        if current_segment:
                            current_segment += " " + word
                        else:
                            current_segment = word
                
                if current_segment:
                    final_segments.append(current_segment)

        return [s for s in final_segments if s]
    
class ArticleFactory():
    
    @staticmethod
    def GetArticle():
        return Article()