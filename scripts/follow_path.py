import rclpy
from rclpy.node import Node
from nav2_msgs.action import FollowPath
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path

class CustomPathFollower(Node):
    def __init__(self):
        super().__init__('custom_path_follower')
        self._action_client = ActionClient(self, FollowPath, '/follow_path')
        self.send_goal()

    def send_goal(self):
        goal_msg = FollowPath.Goal()
        goal_msg.path = Path()
        goal_msg.path.header.frame_id = 'map'

        # Define custom path (example with 3 poses)
        for x, y in [(2.0, 12.0), (1.0, 12.0), (0.0, 12.0), (0.0, 13.0), (0.0, 14.0), (1.0, 14.0), (1.0, 13.5)]:
            pose = PoseStamped()
            pose.header.frame_id = 'map'
            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.orientation.w = 1.0  # facing forward
            goal_msg.path.poses.append(pose)

        self._action_client.wait_for_server()
        self._action_client.send_goal_async(goal_msg)

rclpy.init()
node = CustomPathFollower()
rclpy.spin(node)
