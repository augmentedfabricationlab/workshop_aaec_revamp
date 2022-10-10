from compas.geometry import dot_vectors

def point_above_frame(point, frame):
    n = frame.zaxis
    v = point
    p = frame.point
    d = dot_vectors(n, p)
    return dot_vectors(n, v) >= d

def points_above_frame(points, frame):
    n = frame.zaxis
    p = frame.point
    d = dot_vectors(n, p)
    ndot = n.dot
    return filter(lambda v: ndot(v)>=d, points)

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self