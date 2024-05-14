#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import rospy
import sys
import moveit_commander


class MoveitDemo:
    def __init__(self):
        rospy.loginfo("init Moveit")
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)
        # 初始化ROS节点
        rospy.init_node('moveit_robot', anonymous=True)

        rospy.loginfo("planning group: manipulator")
        self.arm = moveit_commander.MoveGroupCommander('manipulator')
        # 设置机械臂运动的允许误差，单位弧度
        self.arm.set_goal_joint_tolerance(0.001)

        # 设置机械臂运动的允许的最大速度和加速度
        self.arm.set_max_acceleration_scaling_factor(0.5)
        self.arm.set_max_velocity_scaling_factor(0.5)

    def home(self):
        self.arm.set_named_target('home')
        self.arm.go()
        rospy.sleep(1)

    def go_to_joint(self, joint_position):
        # joint_position = [2.53, -0.24, -1.02, 1.10, 0.72, 1.24]
        self.arm.set_joint_value_target(joint_position)
        self.arm.go()
        rospy.sleep(1)

    def shutdown_moveit(self):
        moveit_commander.roscpp_shutdown()
        # moveit_commander.os._exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    joint_position = [2.53, -0.24, -1.02, 1.10, 0.72, 1.24]
    position1 = [0.06, -0.5831, -0.8965, -0.0349, -1.6052, -0.1047]
    position2 = [-0.0388, -0.6981, -1.2391, -0.0523, -1.4959, -0.7853]
    position3 = [-0.1939, -0.4538, -0.5236, -0.1221, -1.2467, 0.0698]
    position4 = [-0.6593, -0.4189, -0.9250, -0.0523, -1.5957, -0.0698]
    move = MoveitDemo()
    move.go_to_joint(joint_position=position1)

    raw_input('Press Enter to Start.')

    move.go_to_joint(joint_position=position2)

    raw_input('Press Enter to Start.')

    move.go_to_joint(joint_position=position3)

    raw_input('Press Enter to Start.')

    move.go_to_joint(joint_position=position4)

    raw_input('Press Enter to Start.')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
