'''
Created on 22-05-2013

@author: Krzysztof Langner
'''

import pygame
import os
from robotics.tiled import helperspygame

os.environ['SDL_VIDEO_CENTERED'] = '1'
 
class MainFrame():
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Robotics sandbox" )
        self.screen_width = 1024
        self.screen_height = 768
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
    def load_resources(self, world_map):
        resources = helperspygame.ResourceLoaderPygame()
        resources.load(world_map)        
        self.renderer = helperspygame.RendererPygame()
        cam_world_pos_x = 0
        cam_world_pos_y = 0
        self.renderer.set_camera_position_and_size(cam_world_pos_x, cam_world_pos_y, \
                                        self.screen_width, self.screen_height, "topleft")
        self.sprite_layers = helperspygame.get_layers_from_map(resources)
 
    def update(self):
        self.screen.fill((0, 0, 0))
        for sprite_layer in self.sprite_layers:
            if sprite_layer.is_object_group:
                # we dont draw the object group layers
                # you should filter them out if not needed
                continue
            else:
                self.renderer.render_layer(self.screen, sprite_layer)
        pygame.display.flip()