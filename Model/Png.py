import pygame as g

class Png:
    
    @staticmethod
    def Load(path: str):
        png = g.image.load(path).convert()
        return png
    
    @staticmethod
    def Trans(background,width,height):
        png = g.transform.scale(background, (width, height))
        return png
        
        