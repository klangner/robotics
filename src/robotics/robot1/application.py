'''
Created on 22-05-2013

@author: Krzysztof Langner
'''

import sys, pygame
from robotics.robot1.view import MainFrame
from robotics.robot1.model import World
 

class RobotApp():
    
    def __init__(self):
        self.main_frame = MainFrame()
        self.model = World()

    def loadMap(self, map_filename):
        self.model.load(map_filename)
        self.main_frame.load_resources(self.model)
    
    def run(self):
        self.robot = self.model.get_robot() 
        self.running = True
        while self.running:
            self.process_events()
            self.main_frame.update()
            
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_UP:
                    self.robot.move(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.robot.move(0, 1)
                elif event.key == pygame.K_RIGHT:
                    self.robot.move(1, 0)
                elif event.key == pygame.K_LEFT:
                    self.robot.move(-1, 0)
