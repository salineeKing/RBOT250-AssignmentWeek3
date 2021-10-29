# Course: RBOT 250 Robot Manipulation, Planning and Control
# Description: Python code answer for homework3 (Service)
# By: Salinee Kingbaisomboon (Sage ID: 20801897)

from geometry_msgs.msg import TransformStamped

import rclpy
from rclpy.node import Node

import math


class MinimalService(Node):

    def __init__(self):
        super().__init__('rbot250_service')
        self.srv = self.create_service(TransformStamped, 'request_tf_msg', self.callback)

    def callback(self, request, response):
    
        static_transformStamped = TransformStamped()

        static_transformStamped.header.frame_id = 'base'
        static_transformStamped.child_frame_id = 'elbow'
        static_transformStamped.transform.translation.x = 1.57
        static_transformStamped.transform.translation.y = 3.142
        static_transformStamped.transform.translation.z = 2 * math.pi
        quat = tf_transformations.quaternion_from_euler(0.123, 1.57,5*math.pi)
        static_transformStamped.transform.rotation.x = quat[0]
        static_transformStamped.transform.rotation.y = quat[1]
        static_transformStamped.transform.rotation.z = quat[2]
        static_transformStamped.transform.rotation.w = 1
        
        response.tf = static_transformStamped
        self.get_logger().info('Incoming request...')

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
