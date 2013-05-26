'''
Created on 22-05-2013

@author: Krzysztof Langner
'''

from robotics.tiled import tmxreader
from random import randint
 

class World():
    ''' World model. Contains map and robot
    '''
    
    def load(self, map_filename):
        self.world_map = tmxreader.TileMapParser().parse_decode(map_filename)
        self.robot = Robot(self.get_world_state())

    def get_map(self):
        return self.world_map
    
    def get_robot(self):
        return self.robot
    
    def get_world_state(self):
        ''' Return 2D array with information about world
            Transient places are marked with value 1. 
            Non-transient as -1
        '''
        state = []
        structures_layer = None
        for layer in self.world_map.layers:
            if layer.name == 'Structures':
                structures_layer = layer
                break
        for col in structures_layer.content2D:
            column = []
            state.append(column)
            for cell in col:
                if cell > 0:
                    column.append(-1)
                else:
                    column.append(1)
        return state
    
    
class Robot():
    ''' Robot model
    '''
    
    def __init__(self, world_state):
        self.world_state = world_state
        posx = randint(0, len(world_state))
        posy = randint(0, len(world_state[0]))
        self.position = (posx, posy)
        self.path = []
    
    def get_position(self):
        return self.position
    
    def get_world_state(self):
        return self.world_state
            
    def move(self, dx, dy):
        (posx, posy) = self.position
        posx = (posx+dx)%len(self.world_state)
        posy = (posy+dy)%len(self.world_state[0])
        self.position = (posx, posy)
