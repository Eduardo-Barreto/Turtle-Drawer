import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill, SetPen
from geometry_msgs.msg import Twist, Vector3
from math import pi
import time
import random


class DrawShape(Node):
    def __init__(self):
        super().__init__("draw_shape")
        self.publisher_ = self.create_publisher(Twist, "toruga/cmd_vel", 10)
        self.i = 0
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.instructions = []

    def spawn_turtle(self):
        spawn_service = self.create_client(Spawn, "spawn")
        while not spawn_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting again...")

        request = Spawn.Request()
        request.x = 5.5
        request.y = 5.5
        request.theta = 0.0
        request.name = "toruga"
        future = spawn_service.call_async(request)

    def kill_turtle(self, name):
        kill_service = self.create_client(Kill, "kill")
        while not kill_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting again...")

        request = Kill.Request()
        request.name = name
        future = kill_service.call_async(request)

    def set_pen(self, r, g, b, width):
        set_pen_service = self.create_client(SetPen, "toruga/set_pen")
        while not set_pen_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting again...")

        request = SetPen.Request()
        request.r = int(r * 255)  # Convertendo para o intervalo de 0 a 255
        request.g = int(g * 255)
        request.b = int(b * 255)
        request.width = width
        request.off = 0
        future = set_pen_service.call_async(request)

    def timer_callback(self):
        if self.i < len(self.instructions):
            self.set_pen(random.random(), random.random(), random.random(), 2)  # Define uma cor aleatória
            self.move_turtle(self.instructions[self.i])
        else:
            self.kill_turtle("toruga")
            self.timer.cancel()

    def move_turtle(self, instruction):
        msg = instruction
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing: {}".format(msg))
        time.sleep(1)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    draw_shape = DrawShape()

    draw_shape.kill_turtle("turtle1")
    draw_shape.spawn_turtle()

    instructions = [
        Twist(linear=Vector3(x=2.0), angular=Vector3(z=0.0)),
        Twist(linear=Vector3(x=0.0), angular=Vector3(z=pi / 2)),
        Twist(linear=Vector3(x=2.0), angular=Vector3(z=0.0)),
        Twist(linear=Vector3(x=0.0), angular=Vector3(z=pi / 2)),
        Twist(linear=Vector3(x=2.0), angular=Vector3(z=0.0)),
        Twist(linear=Vector3(x=0.0), angular=Vector3(z=pi / 2)),
        Twist(linear=Vector3(x=2.0), angular=Vector3(z=0.0)),
    ]
    draw_shape.instructions = instructions

    rclpy.spin(draw_shape)

    draw_shape.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
