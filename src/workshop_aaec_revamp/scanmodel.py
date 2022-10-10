import os.path as path

from compas.files import PLY

from compas.geometry import Frame, Point, Pointcloud, Transformation, KDTree

from compas.rpc import Proxy

from .utilities import point_above_frame, points_above_frame


class ScanModel():
    def __init__(self, base_frame=None, tool_frame=None, pointcloud=None):
        self.base_frame = Frame([0, 0, 0], [-1, 0, 0], [0, 1, 0]) if base_frame is None else base_frame
        self.tool_frame = self.base_frame if tool_frame is None else tool_frame
        self._pointcloud = pointcloud
        self._pointcloud_tf = None
        self._pointcloud_trimmed = None
        if (self.pointcloud is not None and self.tool_frame != self.base_frame):
            self.set_pc_in_tcp()

    @property
    def pointcloud(self):
        if self._pointcloud_trimmed is not None:
            return self._pointcloud_trimmed
        elif self._pointcloud_tf is not None:
            return self._pointcloud_tf
        else:
            return self._pointcloud

    @pointcloud.setter
    def pointcloud(self, pointcloud):
        self._pointcloud = pointcloud

    @classmethod
    def from_ply(cls, filepath):
        sm = cls()
        sm.pointcloud_from_ply(filepath)
        return sm

    def points(self):
        return [{"pos": v.data} for v in self.pointcloud.points]

    def pointcloud_from_ply(self, filepath):
        ply = PLY(filepath)
        ply.read()
        vertices = ply.parser.vertices
        self._pointcloud = Pointcloud(vertices)

    def pointcloud_from_bag(self, bag_filepath, ply_filepath):
        if ply_filepath is None:
            bag_path, bag_filename = path.split(bag_filepath)
            ply_filename = bag_filename.split('.')[0]+'.ply'
            ply_filepath = path.join(bag_path, ply_filename)
        with Proxy("workshop_aaec_revamp.utilities_proxy") as util:
            util.bag_to_ply(bag_filepath, ply_filepath)

        self.pointcloud_from_ply(ply_filepath)

    def set_pc_in_tcp(self):
        del self._pointcloud_tf
        T = Transformation.from_frame_to_frame(self.base_frame, self.tool_frame)
        self._pointcloud_tf = self._pointcloud.transformed(T)

    def build_tree(self):
        self.kdtree = KDTree(self.pointcloud.points)

    def split_pointcloud_by_frame(self, frame):
        if self.pointcloud:
            points = points_above_frame(self.pointcloud.points, frame)
            self._pointcloud_trimmed = Pointcloud(points)
            return points
            # for pt in self.pointcloud.points:
            #     if point_above_frame(pt, frame):
            #         pts.append(pt)
        return None

    def split_mesh_by_frame(self, frame):
        if self._mesh:
            raise NotImplementedError

if __name__ == '__main__':
    bag_filepath = r"C:\Users\Gido\Documents\workspace\development\workshop_aaec_revamp\matlab_file\2022-08-05-13-28-46.bag"
    ply_filepath = r"C:\Users\Gido\Documents\workspace\development\workshop_aaec_revamp\matlab_file\test_bag_to.ply"
    # import matlab.engine
    # eng= matlab.engine.start_matlab()
    # path = r"C:\Users\Gido\Documents\workspace\development\workshop_aaec_revamp\src\workshop_aaec_revamp"
    # eng.cd(path, nargout=0)
    # p = eng.bag_to_ply(bag_filepath, ply_filepath)
    # print(p)
    sm = ScanModel()
    sm.pointcloud_from_bag(bag_filepath, ply_filepath)
