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
    
    
class Robot():
    ''' Robot model
    '''
    
    def get_path(self):
        path = [[0,0], [0,1], [1,1], [1,2], [1,3]]
        return path
    
    def get_position(self):
        return (0, 0)