'''
Created on 24-05-2013

@author: Krzysztof Langner
'''


def astar_path(world_map, start_x, start_y, dest_x, dest_y):
    path = []
    pos = [start_x, start_y]
    distance = max(dest_x-start_x, dest_y-start_y)
    for _i in range(distance):
        pos = pos[:]
        if pos[0] < dest_x:
            pos[0] += 1
        if pos[1] < dest_y:
            pos[1] += 1
        path.append(pos)
    return path
