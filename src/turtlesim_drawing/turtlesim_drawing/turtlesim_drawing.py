import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class TurtlesimDrawing(Node):
    def __init__(self):
        super().__init__("turtlesim_drawing")
        self.publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.subscription = self.create_subscription(
            Pose, "turtle1/pose", self.pose_callback, 10
        )
        self.subscription  # prevent unused variable warning

    def pose_callback(self, msg):
        self.draw_pattern()

    def draw_pattern(self):
        twist = Twist()
        twist.linear.x = 1.0
        twist.angular.z = 0.0
        self.publisher_.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    turtlesim_drawing = TurtlesimDrawing()
    try:
        rclpy.spin(turtlesim_drawing)
    except KeyboardInterrupt:
        pass
    finally:
        turtlesim_drawing.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
