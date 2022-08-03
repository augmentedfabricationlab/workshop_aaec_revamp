# License: Apache 2.0. See LICENSE file in root directory.
# Copyright(c) 2017 Intel Corporation. All Rights Reserved.

#####################################################
#                   Export to PLY                   #
#####################################################

import os
import numpy as np
# First import the library
import pyrealsense2 as rs
from compas.geometry import Point
from compas.geometry import Pointcloud

__all__ = [
    "export_to_ply",
    "get_depth_matrix",
    "get_points"
]


def export_to_ply(path):
    # Declare pointcloud object, for calculating pointclouds and texture mappings
    pc = rs.pointcloud()
    # We want the points object to be persistent so we can display the last cloud when a frame drops
    # points = rs.points()

    # Declare RealSense pipeline, encapsulating the actual device and sensors
    pipe = rs.pipeline()
    config = rs.config()
    # Enable depth stream
    # config.enable_stream(rs.stream.depth)

    resolution = 1280, 720
    config.enable_stream(rs.stream.depth, resolution[0], resolution[1], rs.format.z16, 6)
    config.enable_stream(rs.stream.color, rs.format.rgb8, 30)

    # Start streaming with chosen configuration
    pipe.start(config)

    # We'll use the colorizer to generate texture for our PLY
    # (alternatively, texture can be obtained from color or infrared stream)
    colorizer = rs.colorizer()
    decimate = rs.decimation_filter()
    decimate.set_option(rs.option.filter_magnitude, 1)
    filters = [rs.disparity_transform(),
               rs.spatial_filter(),
               rs.temporal_filter(),
               rs.disparity_transform(False)]

    try:
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        depth_frame = decimate.process(depth_frame)
        for f in filters:
            depth_frame = f.process(depth_frame)
        colorized_depth = colorizer.process(depth_frame)
        pc.calculate(depth_frame)
        pc.map_to(colorized_depth)

        # Create save_to_ply object
        ply = rs.save_to_ply(path)

        # Set options to the desired values
        # In this example we'll generate a textual PLY with normals (mesh is already created by default)
        ply.set_option(rs.save_to_ply.option_ply_binary, False)
        ply.set_option(rs.save_to_ply.option_ply_normals, True)

        print("Saving to {}...".format(path))
        # Apply the processing block to the frameset which contains the depth frame and the texture
        ply.process(depth_frame)
        print("Done")
    finally:
        pipe.stop()


def get_depth_matrix():
    resolution = 640, 480
    pipe = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, resolution[0], resolution[1], rs.format.z16, 6)
    pipe.start(config)

    colorizer = rs.colorizer()
    decimate = rs.decimation_filter()
    decimate.set_option(rs.option.filter_magnitude, 1)
    filters = [rs.disparity_transform(),
               rs.spatial_filter(),
               rs.temporal_filter(),
               rs.disparity_transform(False)]

    try:
        frames = pipe.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        depth_frame = decimate.process(depth_frame)
        for f in filters:
            depth_frame = f.process(depth_frame)
        colorized_depth = colorizer.process(depth_frame)
    finally:
        pipe.stop()

    depth_matrix = []
    for y in range(resolution[1]):
        line = []
        for x in range(resolution[0]):
            line.append(depth_frame.get_distance(x, y))
        depth_matrix.append(line)

    return depth_matrix

def get_points():
    resolution = 640, 480
    pipe = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, resolution[0], resolution[1], rs.format.z16, 6)
    pipe.start(config)

    colorizer = rs.colorizer()
    decimate = rs.decimation_filter()
    decimate.set_option(rs.option.filter_magnitude, 1)
    filters = [rs.disparity_transform(),
               rs.spatial_filter(),
               rs.temporal_filter(),
               rs.disparity_transform(False)]

    try:
        frames = pipe.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        depth_frame = decimate.process(depth_frame)
        for f in filters:
            depth_frame = f.process(depth_frame)
        colorized_depth = colorizer.process(depth_frame)
    finally:
        pipe.stop()
    pc = rs.pointcloud()
    points = pc.calculate(depth_frame)
    pc.map_to(colorized_depth)
    depth_intrinsics = rs.video_stream_profile(depth_frame.profile).get_intrinsics()
    w, h = depth_intrinsics.width, depth_intrinsics.height

    verts = np.asarray(points.get_vertices(2)).reshape(h, w, 3)
    points = [Point(x,y,z) for v in verts for (x,y,z) in v]
    return points


if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(directory, "data", "test_00.ply")
    export_to_ply(filepath)
    print(get_depth_matrix())
    pts = get_points()
