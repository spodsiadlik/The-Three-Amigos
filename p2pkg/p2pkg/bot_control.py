import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
from tf_transformations import quaternion_about_axis
from math import cos, sin

from tf2_ros import TransformBroadcaster

import serial

class BotInterface(Node):
    def __init__(self):
        super().__init__(node_name="bot_interface")
        self.ser = serial.Serial(port="/dev/ttyACM0", baudrate = 115200)
        self.odom_pub_timer = self.create_timer(timer_period_sec=0.02, callback=self.odom_pub_cb)
        self.odom_publisher = self.create_publisher(
            msg_type=Odometry,
            topic='odom',
            qos_profile=1,
        )
        self.transform_broadcaster = TransformBroadcaster(self)
        self.cmd_vel_sub = self.create_subscription(
            Twist, 
            'cmd_vel', 
            self.cmd_vel_cb, 
            1,
            
            )
        #variables
        self.lin_vel = 0.
        self.ang_vel = 0.
        self.x = 0.
        self.y = 0.
        self.z = 0.06 #set to reasonable value
        self.th = 0.
        self.curr_ts = self.get_clock().now()
        self.prev_ts = self.get_clock().now()

    def odom_pub_cb(self):
        if self.ser.inWaiting() > 0:
            data_line = self.ser.readline().decode('utf-8').rstrip()
            vel_list = data_line.split(',')
            self.lin_vel = float(vel_list[0]) 
            self.ang_vel = float(vel_list[1])
        # print(f"robot velocity: {self.lin_vel}, {self.ang_vel}")
        self.curr_ts = self.get_clock().now()
        dt = (self.curr_ts - self.prev_ts).nanoseconds * 1e-9
        dx = self.lin_vel * cos(self.th) * dt
        dy = self.lin_vel * sin(self.th) * dt
        dth = self.ang_vel * dt
        self.x += dx
        self.y += dy
        self.th += dth
        quat = quaternion_about_axis(self.th, (0,0,1))
        self.prev_ts = self.curr_ts
        #pub odom
        odom_msg = Odometry()
        odom_msg.header.stamp = self.curr_ts.to_msg()
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = 'base_link'
        odom_msg.pose.pose.position.x = self.x
        odom_msg.pose.pose.position.y = self.y
        odom_msg.pose.pose.position.z = self.z
        odom_msg.pose.pose.orientation.x = quat[0]
        odom_msg.pose.pose.orientation.y = quat[1]
        odom_msg.pose.pose.orientation.z = quat[2]
        odom_msg.pose.pose.orientation.w = quat[3]
        odom_msg.twist.twist.linear.x = self.lin_vel
        odom_msg.twist.twist.angular.z = self.ang_vel
        self.odom_publisher.publish(odom_msg)
        #broadcast odom to base link transformation
        trans_msg = TransformStamped()
        trans_msg.header.stamp = self.curr_ts.to_msg()
        trans_msg.header.frame_id = 'odom'
        trans_msg.child_frame_id = 'base_link'
        trans_msg.transform.translation.x = self.x
        trans_msg.transform.translation.y = self.y
        trans_msg.transform.translation.z = self.z
        trans_msg.transform.rotation.x = quat[0]
        trans_msg.transform.rotation.y = quat[1]
        trans_msg.transform.rotation.z = quat[2]
        trans_msg.transform.rotation.w = quat[3]
        self.transform_broadcaster.sendTransform(trans_msg)

    def cmd_vel_cb(self, msg):
        lin_x = msg.linear.x
        ang_z = msg.angular.z
        target_vel_str = f"{lin_x},{ang_z}\n"
        print(f"{target_vel_str}")
        self.ser.write(bytes(target_vel_str.encode('utf-8')))

def main(args=None):
    rclpy.init(args=args)
    bot_node = BotInterface()
    rclpy.spin(bot_node)
    bot_node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()