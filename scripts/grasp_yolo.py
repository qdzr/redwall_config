#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import rospy
import sys
import torch
import message_filters
import torch.nn as nn
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import Header
from yolov5_ros_msgs.msg import BoundingBoxes


def callback(image, BoundingBoxes):
    pass


if __name__ == '__main__':
    rospy.init_node('message_filter')

    depth_image_sub = message_filters.Subscriber('/camera/depth/image_meters', Image)
    yolo_boxes = message_filters.Subscriber('/yolov5/BoundingBoxes', BoundingBoxes)

    message = message_filters.ApproximateTimeSynchronizer([depth_image_sub, yolo_boxes],
                                                          queue_size=10, slop=0.1)
    message.registerCallback(callback)

    rospy.spin()