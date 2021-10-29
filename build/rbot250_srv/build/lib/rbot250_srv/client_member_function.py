# Course: RBOT 250 Robot Manipulation, Planning and Control
# Description: Python code answer for homework3 (Client)
# By: Salinee Kingbaisomboon (Sage ID: 20801897)

import sys

from std_msgs.msg import String

from geometry_msgs.msg import TransformStamped

import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('rbot250_client_async')
        self.cli = self.create_client(TransformStamped, 'request_tf_msg')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = TransformStamped.Request()

    def send_request(self):
        self.future = self.cli.call_async(self.req)


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info(
                    'Result of add_two_ints: YES')
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
