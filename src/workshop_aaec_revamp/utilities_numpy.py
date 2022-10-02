import numpy as np


def point_above_frame(pt, frame):
    n = np.asarray(frame.zaxis)
    v = np.asarray(pt)
    p = np.asarray(frame.point)
    d = n.dot(p)
    return n.dot(v) >= d
