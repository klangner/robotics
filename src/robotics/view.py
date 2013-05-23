'''
Created on 22-05-2013

@author: Krzysztof Langner
'''

import pygame
import os
from robotics.tiled import helperspygame

os.environ['SDL_VIDEO_CENTERED'] = '1'
TITLE_HEIGHT = 32
TITLE_WIDTH = 32
 
class MainFrame():
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Robotics sandbox" )
        self.screen_width = 1024
        self.screen_height = 768
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.canvas = Canvas(screen)
        
    def load_resources(self, model):
        self.model = model
        self.robot_view = RobotView(model.get_robot())
        resources = helperspygame.ResourceLoaderPygame()
        resources.load(model.get_map())        
        self.renderer = helperspygame.RendererPygame()
        camera_x = 0
        camera_y = 0
        self.renderer.set_camera_position_and_size(camera_x, camera_y, \
                                        self.screen_width, self.screen_height, "topleft")
        self.sprite_layers = helperspygame.get_layers_from_map(resources)
 
    def update(self):
        self.canvas.clear()
        self._draw_layers()
        self.robot_view.draw(self.canvas)
        pygame.display.flip()
        
    def _draw_layers(self):
        for sprite_layer in self.sprite_layers:
            if not sprite_layer.is_object_group:
                self.renderer.render_layer(self.canvas.get_surface(), sprite_layer)
        
        
class Canvas():
    ''' custom function for drawing on canvas
    '''
    
    def __init__(self, surface):
        self.surface = surface
        
    def get_surface(self):
        return self.surface
    
    def clear(self):
        self.surface.fill((0, 0, 0))
        
    def draw_circle(self, col, row, color, radius):
        x = col*TITLE_WIDTH+TITLE_WIDTH/2
        y = row*TITLE_HEIGHT+TITLE_HEIGHT/2 
        pygame.draw.circle(self.surface, color, (x, y), radius)
        
        
class RobotView():
    ''' Update view based on robot information
    '''
    
    def __init__(self, robot):
        self.robot = robot
        
    def draw(self, canvas):
        for step in self.robot.get_path():
            canvas.draw_circle(step[0], step[1], (255, 0, 0), 5)
        (robot_x, robot_y) = self.robot.get_position()
        canvas.draw_circle(robot_x, robot_y, (0, 0, 255), 16)
        
        