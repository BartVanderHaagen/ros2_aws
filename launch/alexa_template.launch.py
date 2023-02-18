import rclpy
import zenoh
from rclpy.node import Node
from std_msgs.msg import String

class AlexaNode(Node):
    def __init__(self):
        super().__init__("alexa_node")
        self.zenoh_session = zenoh.net.open()
        self.subscription = self.create_subscription(
            String,
            "alexa",
            self.listener_callback,
            10
        )
        self.confirmation_pub = self.create_publisher(
            String,
            "confirmation",
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")
        confirm_msg = f"Confirm you want me to {msg.data}"
        self.get_logger().info(confirm_msg)
        self.confirmation_pub.publish(String(data=confirm_msg))
        response = self.zenoh_session.get("/confirmation")
        if response.get_value().decode() == "confirm":
            self.send_msg_to_ec2(msg.data)

    def send_msg_to_ec2(self, msg):
        # Code to send message to EC2 instance
        pass

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()    
