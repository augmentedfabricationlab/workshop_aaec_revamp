import os

from compas.files import PLY

from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Pointcloud
from compas.geometry import Transformation as Tf
from compas.geometry import KDTree

from compas.datastructures import Mesh
from compas.rpc import Proxy

from .utilities import point_above_frame


class ScanModel():
    def __init__(self, base_frame=None, tool_frame=None, pointcloud=None):

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

    def pointcloud_from_ply(self, filepath):
        ply = PLY(filepath)
        ply.read()
        vertices = ply.parser.vertices
        faces = ply.parser.faces
        print(len(vertices))
        self.pointcloud = Pointcloud(vertices)
        if len(faces) > 0:
            self.mesh = Mesh.from_vertices_and_faces(vertices, faces)

    def points(self):
        return [{"pos": v.data} for v in self.pointcloud.points]

    def pointcloud_from_bag(self, bag_filepath, ply_filepath):
        if ply_filepath is None:
            bag_path, bag_filename = os.path.split(bag_filepath)
            ply_filename = bag_filename.split('.')[0]+'.ply'
            ply_filepath = os.path.join(bag_path, ply_filename)
        with Proxy("workshop_aaec_revamp.utilities_proxy") as util:
            util.bag_to_ply(bag_filepath, ply_filepath)

        self.pointcloud_from_ply(ply_filepath)

    def set_pc_in_tcp(self, tool_frame=None):
        if tool_frame is not None:
            self.tool_frame = tool_frame
        T = Tf.from_frame_to_frame(self.base_frame, self.tool_frame)
        points_tf = Point.transformed_collection(self._pointcloud_base.points, T)
        self._pointcloud_tf = Pointcloud(points_tf)
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
