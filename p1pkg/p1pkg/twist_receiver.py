# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from gpiozero import PhaseEnableRobot
from time import sleep

bot = PhaseEnableRobot(right = (13, 26), left = (25, 24))

def forward_right():
    bot.left_motor.forward(1)
    bot.right_motor.forward(0.6)
def forward_left():
    bot.left_motor.forward(0.6)
    bot.right_motor.forward(1)
def backward_right():
    bot.left_motor.backward(1)
    bot.right_motor.backward(0.6)
def backward_left():
    bot.left_motor.backward(0.6)
    bot.right_motor.backward(1)

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        #subscribe to the teleop_twist_key publisher topic cmd_vel
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.listener_callback, 1)
        

    def listener_callback(self, msg):
        print(msg.linear.x)
        print(msg.angular.z)
        if msg.linear.x > 0 and msg.angular.z == 0: 
            bot.forward(0.5)
        elif msg.linear.x < 0 and msg.angular.z == 0:
            bot.backward()
        elif msg.linear.x == 0 and msg.angular.z > 0:
            bot.left()
        elif msg.linear.x == 0 and msg.angular.z < 0:
            bot.right()
        elif msg.linear.x > 0 and msg.angular.z > 0:
            forward_left()
        elif msg.linear.x > 0 and msg.angular.z < 0:
            forward_right()
        elif msg.linear.x < 0 and msg.angular.z < 0: 
            backward_left()
        elif msg.linear.x < 0 and msg.angular.z > 0: 
            backward_right()
        elif msg.linear.x == 0 and msg.angular.z == 0: 
            bot.stop()

        


        

        
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
