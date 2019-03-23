from flow_util import read, Point, grid, Shape

import numpy as np

def read_lvl3(id):

    raw = read(3,id).split()

    data = {}
    data['rows'] = int(raw[0])
    data['cols'] = int(raw[1])
    data['shape'] = Shape(data['rows'], data['cols'])
    print(data['shape'])
    data['array'] = grid(data['shape'])
    data['no_points'] = int(raw[2])
    offset = 3+data['no_points']*2
    piter = iter(list(map(int,raw[3:offset])))
    data['points'] = list(map(lambda x: Point.fromIndex(
            x, data['shape'], color=next(piter)), piter))
    data['no_paths'] = int(raw[offset])
    poffset = offset + 1 
    data['paths'] = []
    
    
    
    return data