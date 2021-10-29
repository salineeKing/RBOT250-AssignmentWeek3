#!/usr/bin/env python3

# Course: RBOT 250 Robot Manipulation, Planning and Control
# Description: Python code answer for homework3 (Subscriber)
# By: Salinee Kingbaisomboon (Sage ID: 20801897)

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from geometry_msgs.msg import TransformStamped


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('rbot250_subscriber')
        self.subscription = self.create_subscription(
            TransformStamped,
            'homeworks/hw1/tf', # Subscribed to this topic from c++
            self.listener_callback,
            30)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, message):
        txt_message = "Header: \n frame_id:  {frame_id} \n child_frame_id: {child_frame_id} \n Vector3 translation: [{trans_x} {trans_y} {trans_z}]  \n \n Quaternion rotation: {{wx: {q_x} wy: {q_y} , wz: {q_z} , wq:  {q_w} }}".format(frame_id = message.header.frame_id, child_frame_id = message.child_frame_id, trans_x = message.transform.translation.x, trans_y = message.transform.translation.y, trans_z = message.transform.translation.z, q_x = message.transform.rotation.x, q_y = message.transform.rotation.y, q_z = message.transform.rotation.z, q_w = message.transform.rotation.w)
        self.get_logger().info('Subscribe static TransformStamped msg by Python code: \n "%s"\n' % txt_message)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()