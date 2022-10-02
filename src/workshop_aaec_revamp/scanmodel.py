from compas.geometry import Frame
from compas.rpc import Proxy
from compas.geometry import Point
from compas.geometry import Pointcloud
from compas.geometry import Transformation as Tf
from compas.geometry import KDTree
# from compas.geometry import is_point_infront_plane
from .utilities import point_above_frame
import time


class ScanModel():
    def __init__(self, base_frame=None, tool_frame=None, pointcloud=None):
        self.t0 = time.time()
        print("t0: ", self.t0)
        if base_frame is None:
            self.base_frame = Frame([0, 0, 0], [1, 0, 0], [0, 1, 0])
        else:
            self.base_frame = base_frame
        if tool_frame is None:
            self.tool_frame = self.base_frame
        else:
            self.tool_frame = tool_frame
        self._pointcloud_base = pointcloud
        self._pointcloud_tf = None
        if self._pointcloud_base is not None and self.tool_frame!=self.base_frame:
            self._pointcloud_tf = self.set_pc_in_tcp()
        self._mesh = None

    @property
    def pointcloud(self):
        if self._pointcloud_tf is not None:
            return self._pointcloud_tf
        else:
            return self._pointcloud_base

    @pointcloud.setter
    def pointcloud(self, pointcloud):
        self._pointcloud_base = pointcloud

    @property
    def mesh(self):
        return self._mesh

    @mesh.setter
    def mesh(self, mesh):
        self._mesh = mesh

    def set_pc_in_tcp(self, tool_frame=None):
        print("t1: ", self.t0 - time.time())
        if tool_frame is not None:
            self.tool_frame = tool_frame
        T = Tf.from_frame_to_frame(self.base_frame, self.tool_frame)
        print("t2: ", self.t0 - time.time())
        points_tf = Point.transformed_collection(self._pointcloud_base.points, T)
        print("t3: ", self.t0 - time.time())
        self._pointcloud_tf = Pointcloud(points_tf)
        print("t4: ", self.t0 - time.time())
        return self.pointcloud

    def build_tree(self):
        self.kdtree = KDTree(self.pointcloud.points)

    def split_pointcloud_by_frame(self, frame):
        if self.pointcloud:
            pts = []
            for pt in self.pointcloud.points:
                if point_above_frame(pt, frame):
                    pts.append(pt)
        return pts

    def split_mesh_by_frame(self, frame):
        if self._mesh:
            pass
