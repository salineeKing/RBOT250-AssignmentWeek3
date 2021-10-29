// Course: RBOT 250 Robot Manipulation, Planning and Control
// Description: Python code answer for homework3 (Publisher)
// By: Salinee Kingbaisomboon (Sage ID: 20801897)


#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include <math.h>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

#include <geometry_msgs/msg/transform_stamped.hpp>

#include <rclcpp/rclcpp.hpp>
#include <tf2/LinearMath/Quaternion.h>

using namespace std::chrono_literals;
using std::placeholders::_1;

class MinimalPublisher : public rclcpp::Node
{
public:
  MinimalPublisher()
  : Node("rbot250_publisher"), count_(0)
  {
    publisher_ = this->create_publisher<geometry_msgs::msg::TransformStamped>("homeworks/hw1/tf", 30);
    timer_ = this->create_wall_timer(
      500ms, std::bind(&MinimalPublisher::timer_callback, this));
  }

private:
  void timer_callback()
  {
    auto message = geometry_msgs::msg::TransformStamped();
	
	// Set the static parameters
	message.header.frame_id = "base";
	message.child_frame_id = "elbow";
	message.transform.translation.x = 1.57;
    message.transform.translation.y = 3.142;
    message.transform.translation.z = 2 * M_PI/3;
    tf2::Quaternion q;
    q.setRPY(0.123, 1.57,5*M_PI/6);
    message.transform.rotation.x = q.x();
    message.transform.rotation.y = q.y();
    message.transform.rotation.z = q.z();
    message.transform.rotation.w = 1;
    
    RCLCPP_INFO(this->get_logger(), "Publishing static TransformStamped msg by C++ code: \n Header: \n frame_id: '%s' \n child_frame_id: '%s' \n Vector3 translation: ['%f' '%f' '%f']  \n Quaternion rotation: {'wx': '%f'  'wy': '%f' , 'wz': '%f' , 'wq': '%f' }", message.header.frame_id.c_str(), message.child_frame_id.c_str(), message.transform.translation.x, message.transform.translation.y, message.transform.translation.z, message.transform.rotation.x, message.transform.rotation.y, message.transform.rotation.z, message.transform.rotation.w);
    publisher_->publish(message);
  }
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<geometry_msgs::msg::TransformStamped>::SharedPtr publisher_;
  size_t count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}
