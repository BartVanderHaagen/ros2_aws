# ros2_aws
ROS2 node to communicate with AWS Alexa 

an example ROS 2 node that uses Zenoh to subscribe to an alexa message and sends a confirmation message to the user before sending the message to an EC2 instance:

we are using Zenoh to subscribe to a confirmation topic and publish confirmation messages to it. When a message is received on the alexa topic, a confirmation message is sent to the confirmation topic using ROS 2's built-in create_publisher() method.

The listener_callback() function also retrieves the latest message on the confirmation topic using Zenoh's get() method. If the message is "confirm", the send_msg_to_ec2() function is called to send the original message to the EC2 instance.

Please note that this is just an example and may require modification to work in your specific use case. Also, be sure to import and configure Zenoh properly in your environment before running this code.

The ROS 2 node will keep running and listening for messages until it is explicitly shut down.

The spin() function will block the main thread of execution and keep the ROS 2 node alive until the node is shutdown, either by calling rclpy.shutdown() or by sending a SIGINT signal (e.g., by pressing Ctrl+C in the terminal).

Whenever a new message arrives on the alexa topic, the listener_callback() function will be called, and it will handle the message and potentially send a message to the confirmation topic and/or the EC2 instance. After each message is handled, the node will continue listening for new messages on the alexa topic.

To debug the ROS 2 node code

ros2 run my_package alexa_node --ros-args --log-level debug

When a message like "[alexa get my chair]" is received, you should see log messages that look something like this:
[DEBUG] [alexa_node]: Received: get my chair
[INFO] [alexa_node]: Confirm you want me to get my chair

The send_msg_to_ec2() function is W.I.P.



