'''
Created on 22-05-2013

@author: Krzysztof Langner
'''

from robotics.tiled import tmxreader
from robotics.slam.pathfinding import astar_path
 

class World():
    ''' World model. Contains map and robot
    '''
    
    def __init__(self):
        self.robot = Robot()
        
    def load(self, map_filename):
        self.world_map = tmxreader.TileMapParser().parse_decode(map_filename)

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
    
    def __init__(self):
        self.pos_x, self.pos_y = 0, 0
        self.path = []
    
    def get_path(self):
        return self.path
    
    def get_position(self):
        return (0, 0)
    
    def set_destination(self, dest_x, dest_y, world_state):
        self.world_state = world_state
        self.path = astar_path(world_state, self.pos_x, self.pos_y, dest_x, dest_y)
            
    def get_world_state(self):
        return self.world_state
            