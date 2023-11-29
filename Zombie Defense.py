# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:57:55 2023

@author: pclee
"""

import pygame, simpleGE
    
pygame.init()

class archer(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Archer.png")
        self.setSize(50, 50)
        self.y = (185)
        self.x = (150)
        
    def checkEvents(self):
        super().checkEvents()
        if self.scene.isKeyPressed(pygame.K_b):
            self.scene.currentArrow += 1
            if self.scene.currentArrow >= self.scene.NUM_ARROWS:
                self.scene.currentArrow = 0
            self.scene.arrows[self.scene.currentArrow].fire()
    
    def setPosition (self, position):
        (self.x, self.y) = position
        self.rect.center = self.x, self.y
    
class arrow(simpleGE.SuperSprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.imageMaster = pygame.Surface((5, 5))
        self.setImage("arrow.png")
        self.setBoundAction(self.HIDE)
        self.hide()

    def fire(self):
        self.show()
        self.setPosition(self.parent.rect.center)
        self.setMoveAngle(self.parent.rotation)
        self.setSpeed(20)
        
class Crosshair(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cross_normal.png")
        self.setSize(10, 10)

    def checkEvents(self):
        (mx, my) = pygame.mouse.get_pos()
        self.x = mx
        self.y = my

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Arrow keys to aim")
        self.archer = archer(self)
        self.NUM_ARROW = 100
        self.currentArrow = 0       
        self.arrow = []
        for i in range(self.NUM_ARROW):
            self.arrow.append(arrow(self, self.archer))
                                
        self.sprites = [self.archer, self.arrow]
        self.background = pygame.image.load("forest_background.png")
        self.background = pygame.transform.scale(self.background, (640,480))

    def doEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.currentArrow += 1
                if self.currentArrow >= self.NUM_ARROWS:
                    self.currentBullet = 0
                self.arrow[self.currentArrow].fire()
                
    
       
                           
def main():
    game = Game()
    game.start()
    pygame.mouse.set_visible(True)
    
if __name__ == "__main__":
    main()