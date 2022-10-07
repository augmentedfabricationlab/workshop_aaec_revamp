import os
import numpy as np
import matlab.engine

def bag_to_ply(bag_filepath, ply_filepath):
    eng = matlab.engine.start_matlab()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    eng.cd(dir_path, nargout=0)
    eng.bag_to_ply(bag_filepath, ply_filepath)

def point_above_frame(pt, frame):
    n = np.asarray(frame.zaxis)
    v = np.asarray(pt)
    p = np.asarray(frame.point)
    d = n.dot(p)
    return n.dot(v) >= d
