'''
Created on 22-05-2013

@author: Krzysztof Langner
'''

from robotics.tiled import tmxreader
 

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
        print(world_state)
        self.path = []
        pos = [self.pos_x, self.pos_y]
        while pos[0] < dest_x or pos[1] < dest_y:
            if dest_x-pos[0] > dest_y-pos[1]:
                pos = [pos[0]+1, pos[1]]
            else:
                pos = [pos[0], pos[1]+1]
            self.path.append(pos)
            