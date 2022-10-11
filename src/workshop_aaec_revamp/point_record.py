import time
from roslibpy import Topic
from compas.geometry import Point
from compas.geometry import Pointcloud
from compas.datastructures import Mesh
from compas.files import PLY


class DataRecorder():
    def __init__(self):
        self.data = []

    def __call__(self, msg):
        self.data.append(msg)

class PointcloudRecorder():
    def __init__(self, ros_client=None):
        self.ros_client = ros_client
        self.pointcloud = Pointcloud([])
        self.data_recorder = DataRecorder()

    def clear(self):
        self.pointcloud = Pointcloud([])
        self.data_recorder = DataRecorder()

    def start_recording(self):
        self.listener.subscribe(self.data_recorder)
        # self.listener.subscribe(lambda message: print(message['data']))

    def stop_recording(self):
        self.listener.unsubscribe()

    def record_once(self, dr=None):
        self.listener.subscribe(self.data_recorder)
        # self.listener.subscribe(lambda message: print(message['data']))
        time.sleep(1)
        self.listener.unsubscribe()

    def set_topic(self, 
                  topic_name="/point_cloud_data2",
                  msg_type="std_msgs/Float32MultiArray",
                  throttle_rate=1,
                  queue_size=10):
        self.listener = Topic(self.ros_client, topic_name, msg_type,
                              throttle_rate=throttle_rate, queue_size=queue_size)

    def points(self):
        return [{"pos": v.data} for v in self.pointcloud.points]

    def convert_data_to_pc(self):
        for line in self.data_recorder.data:
            data = line["data"]
            n = 3
            pts = [Point.from_data(data[i:i+n]) for i in range(0, len(data), n)]
            self.pointcloud._points.extend(pts)
        return self.pointcloud

    def save_to_file(self, filepath):
        mesh = Mesh()
        for x, y, z in iter(self.pointcloud.points):
            mesh.add_vertex(x=x, y=y, z=z)
        ply = PLY(filepath)
        ply.write(mesh)


if __name__ == "__main__":
    from compas_fab.backends import RosClient

    ros_client = RosClient("192.168.0.4", 9090)
    ros_client.run(5)

    pcr = PointcloudRecorder(ros_client)
    pcr.set_topic()
    pcr.start_recording()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pcr.stop_recording()
        pcr.convert_data_to_pc()
        print(len(pcr.pointcloud.points))
    
    
