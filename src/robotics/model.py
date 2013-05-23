'''
Created on 22-05-2013

@author: Krzysztof Langner
'''

from robotics.tiled import tmxreader
 

class World():
    
    def load(self, map_filename):
        self.world_map = tmxreader.TileMapParser().parse_decode(map_filename)

    def get_map(self):
        return self.world_map