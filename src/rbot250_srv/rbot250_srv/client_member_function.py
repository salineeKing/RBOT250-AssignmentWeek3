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
                txt_message = "Header: \n frame_id:  {frame_id} \n child_frame_id: {child_frame_id} \n Vector3 translation: [{trans_x} {trans_y} {trans_z}]  \n \n Quaternion rotation: {{wx: {q_x} wy: {q_y} , wz: {q_z} , wq:  {q_w} }}".format(frame_id = response.tf.header.frame_id, child_frame_id = response.tf.child_frame_id, trans_x = response.tf.transform.translation.x, trans_y = response.tf.transform.translation.y, trans_z = response.tf.transform.translation.z, q_x = response.tf.transform.rotation.x, q_y = response.tf.transform.rotation.y, q_z = response.tf.transform.rotation.z, q_w = response.tf.transform.rotation.w)
                minimal_client.get_logger().info(
                    'Result of static TransformStamped msg by Python code: %s' % txt_message)
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
