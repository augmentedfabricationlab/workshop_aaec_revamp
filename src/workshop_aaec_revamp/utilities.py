from compas.geometry import dot_vectors

def point_above_frame(point, frame):
    n = frame.zaxis
    v = point
    p = frame.point
    d = dot_vectors(n, p)
    return dot_vectors(n, v) >= d