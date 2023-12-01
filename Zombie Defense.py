# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:57:55 2023

@author: pclee
"""

import pygame, simpleGE, random
    
pygame.init()

class Tower(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("tower2.png")
        self.setSize(120, 460)
        self.y = (270)
        self.x = (115)
        
    def setPosition (self, position):
        (self.x, self.y) = position
        self.rect.center = self.x, self.y
        
class Archer(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Archer_ready.png")
        self.setSize(50, 50)
        self.y = (170)
        self.x = (200)
        
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
        
class Lizard(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Lizard.png")
        self.setSize(50, 50)
        self.y = random.randint(180, 400)
        self.x = 660
        self.speed = random.randint(-6, -2)
    
    def checkEvents(self):
        if self.collidesWith(self.scene.tower):
            self.reset()
        if self.collidesWith(self.scene.arrow):
            self.reset()
        
    def reset(self):
        self.y = random.randint(180, 400)
        self.x = 640
        self.dx = random.randint(-6, -2)

        
class Arrow(simpleGE.SuperSprite):
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
        self.setImage("crosshair6.png")
        self.setSize(50, 50)

    def checkEvents(self):
        (mx, my) = pygame.mouse.get_pos()
        self.x = mx
        self.y = my

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Arrow keys to aim")
        self.archer = Archer(self)
        self.NUM_ARROW = 100
        self.currentArrow = 0       
        self.arrow = []
        for i in range(self.NUM_ARROW):
            self.arrow.append(Arrow(self, self.archer))
            
        self.lizard = []
        for i in range(7):
            self.lizard.append(Lizard(self))
                                
        self.background = pygame.image.load("Defense_Background.png")
        self.background = pygame.transform.scale(self.background, (640,480))

        pygame.mouse.set_visible(False)
        
        self.crosshair = Crosshair(self)
        self.tower = Tower(self)

        self.sprites = [self.archer, self.arrow, self.tower, self.crosshair, self. lizard]


    def doEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.currentArrow += 1
                if self.currentArrow >= self.NUM_ARROWS:
                    self.currentArrow = 0
                self.arrow[self.currentArrow].fire()
                
    
       
                           
def main():
    game = Game()
    game.start()
    pygame.mouse.set_visible(True)
    
if __name__ == "__main__":
    main()