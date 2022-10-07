import time
from roslibpy import Topic
from compas.geometry import Point
from compas.geometry import Pointcloud


class DataRecorder():
    def __init__(self):
        self.data = []

    def __call__(self, msg):
        self.data.append(msg)


class PointcloudRecorder():
    def __init__(self, ros_client=None):
        self.ros_client = ros_client
        self.pointcloud = None

    def start_recording(self):
        dr = DataRecorder()
        self.listener.subscribe(dr)
        self.data_recorder = dr
        # self.listener.subscribe(lambda message: print(message['data']))

    def stop_recording(self):
        self.listener.unsubscribe()

    def record_once(self, pointcloud):
        self.listener.subscribe(pointcloud)
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

    def convert_data_to_pc(self):
        pc = Pointcloud([])
        for line in self.data_recorder.data:
            data = line["data"]
            n = 3
            pts = [Point.from_data(data[i:i+n]) for i in range(0, len(data), n)]
            self.pointcloud.points.extend(pts)
        self.pointcloud = pc


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
    
    
