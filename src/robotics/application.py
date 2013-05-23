'''
Created on 22-05-2013

@author: Krzysztof Langner
'''

import sys, pygame
from robotics.view import MainFrame
from robotics.model import World
 

class RobotApp():
    
    def __init__(self):
        self.main_frame = MainFrame()
        self.model = World()

    def loadMap(self, map_filename):
        self.model.load(map_filename)
        self.main_frame.load_resources(self.model)
    
    def run(self):
        while True:
            self.process_events()
            self.main_frame.update()
            
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
