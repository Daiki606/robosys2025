import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Trigger

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('talker')

        # パラメータ宣言 (Hz)
        self.declare_parameter('talk_rate', 1.0)
        rate = self.get_parameter('talk_rate').value

        # Timer (publish frequency)
        self.timer = self.create_timer(1.0 / rate, self.timer_callback)
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.count = 0

        # Servicio: resetear contador
        self.srv = self.create_service(
            Trigger,
            'reset_count',
            self.reset_count_callback
        )

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello ROS2: {self.count}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count += 1

    def reset_count_callback(self, request, response):
        self.count = 0
        response.success = True
        response.message = "Counter reset to 0"
        self.get_logger().info("Reset service called.")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

