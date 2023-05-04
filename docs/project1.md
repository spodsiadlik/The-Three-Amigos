# Overview
In this project, we strove to create a differential drive robot that could be controlled using ROS. It uses a Raspberry Pi in conjunction with high-torque motors, a motor driver board, and many other parts, which created a driving robot. Then, after considering features like the robot's weight and shape, we were able to optimize our bot for future assignments and could eventually use it to drive through the CCCS building. This basic robot was itterated upon with lidar, which enables us to autonomously navigate through a pre-mapped area using the ROS 2 navigation stack.


| Property | Quantity |
| --- | --- |
| Weight | 5.2 kg (11.47 lbs) |
| Dimension (Length x Width x Height) | 0.37 m x 0.371 m x 0.22 m |
| Battery Life (Motors) | 2.5 hours |
| Battery Life (Raspberry Pi) | Multiple Days |
| Maximum Speed (Linear) | 0.5 m/s |
| Maximum Speed (Radial) | 0.85π rad/s |
| Payload Capacity | At Least 12 kg (26.5 lbs) |
| Wheel Radius (Skateboard) | 4.15 cm |
| Wheel Radius (Caster) | 2.35 cm |
| Wheel Separation | 5.5 cm |
| Ground Clearance | 5.4 cm |

# Analysis

## Robot Weight
The weight of the robot was one of our initial concerns, and we consequently used lighter materials in the construction of the robot. We still used the aluminum extrusions for our base frame, but instead of using wood or metal for our second level, we used an acrylic sheet that would allow us to easily mount everything we needed. We also used a 3-D printer to print any extra additions we needed, including a mount for the PiCamera (which will be used in future projects), a base for the Lidar and RPi (using the same design as the one from last semester), and small platforms that allow us to lower our caster wheels to the same height as the skateboard wheels. In the end, the robot ended up having a mass of 5.2 kilograms (or 11.47 pounds).

## Base Dimensions
When considering the design for our robot, we were thinking ahead to the end goal and how we planned to use it when mapping out the CCCS building. To accomplish this, we decided to make the base of our robot a perfect square (or as close to one as we could make by cutting an acrylic sheet) with dimensions of 0.37 meters by 0.371 meters. This also allowed us to have more than enough space to mount all of our components. Lastly, we used the robot chassis design from last semester to create two layers, allowing us to mount our Lidar on top of the bot for future navigation projects. Overall, this addition made the height of the robot 0.22 meters.

![Acylic Sheet Blueprint](https://user-images.githubusercontent.com/112110593/220822932-0a08f132-286d-454d-8571-26bcb6e1f94d.JPG)
![Aluminum Extrusion Frame](https://user-images.githubusercontent.com/112110593/220675392-b7bee21e-1ffa-4ef2-9d62-bb76b9cf2d10.JPG)
![Side View - Robotics](https://user-images.githubusercontent.com/112110593/236246026-7b84e9dc-8f58-4fc0-ae7e-13c53edf4f3d.JPG)
![Electronics Layout - Robotics](https://user-images.githubusercontent.com/112110593/236246197-40934f7c-390a-489b-8daa-984fd2f39e86.JPG)


## Wiring Diagram
![Circuit Diagram - Fourth Amigo](https://user-images.githubusercontent.com/112110593/220675232-cb4112af-a8b4-48c7-9ff0-9cb7bf532950.JPG)


## Maximum Speed
When determining the speed our robot, we used different methods for finding the linear and angular velocities of the robot. To determine the linear velocity, we set up markers at every meter along the floor for four meters. Then, we drove our robot forward at its maximum speed and used a stopwatch (with a lap feature) to find how long it took to reach marker. Then, we averaged each lap value to determine the overall speed of the bot, and we determined that it took around 2 seconds to reach each marker. Therefore, it had a maximum linear speed of 0.5 m/s.
Next, we wanted to find the angular velocity, so we had the robot rotate in a circle for 2 rotations and determined how long it took to accomplish that task. In the end, it to 4.7 seconds to rotate twice, so it has an angular velocity of 0.85pi radians/s.

## Payload Capacity
To test the payload capacity, we added 2kg masses one by one onto our robot while it was running until the robot stopped working. However, after adding 6 of those masses, the robot was still functioning extremely well and we were risking destroying our acrylic sheet. Therefore, we stopped at that weight because we did not feel that it was worth risking our robot's functionality to add more weight. Overall, we determined that the payload capacity of our robot was at least 12 kilograms (or 26.46 pounds).

## Battery Life Span
When constructing the robot, we considered the battery life and decided to have two separate power supplies: one to power the motors and one to power the Raspberry Pi and the RPi Pico. Then, the batteries wouldn't be simultaneously drained by both components, and we could individually power each part. The first type of power supply uses three lithium ion batteries to power our motors, and we chose this specific method because the batteries were easily removable. Because of that, we wouldn't need to disassemble anything to recharge the batteries, and they would be much less dangerous that LiPo batteries. Our other power source would be an Anker Power Bank, which we could use to power the Pi and Pico. Since it would last much longer than the batteries, so it would need to be recharged less. The power bank has a few days worth of power, wheres the batteries for the motors can last for about two and a half hours until dropping to a voltage where they aren't fully effective (around 9V).

## Safety Features
One of the most important considerations that we had while designing our robot was involving safety features, since we want to make sure that our bot is safe to use. We considered two different types of safety additions: physical and software features. The main physical safety feature that we included was bumpers made of weather 
stripping that could reduce damamge if the bot bumped into anything. It was placed strategically on the edges of the bot in order to maximize its efficiency. Additionally, we used tape to fasten our cables and ensure that they do not move around while the bot is in motion. We also include two different software features to terminate the program. The first is the KeyboardInterrupt, which occurs when the CTRL and C keys are pressed at the same time, ending the program. The other option is used when the K key is pressed while the driving program is running, and it reduced the angular and linear velocity to zero.

## Parts List

| Name | Description | Quantity |
| --- | --- | --- |
| Raspberry Pi | CPU Unit Used to Run Functions | 1 |
| Raspberry Pi Pico | Used to Read Encoder Signals and Send PWM Signal to Driver | 1 |
| High-torque Motors | Used to Drive the Bot | 2 |
| Batteries | 3.7  V Lithium Ion Battery (Powers Motors) | 3 |
| Anker Power Bank | Serves as a Power Source for the Pi and Pico | 1 |
| Motor Driver Board | An Addition to the Raspberry Pi Unit That Allows Motors to Be Used | 1 |
| 30x30 Aluminum Extrusions | Used to Construct the Base Frame of the Bot | 4 |
| Skateboard Wheels | Used to Steer the Bot | 2 |
| Caster Wheels | Used to Stabilize of the Bot and Guide its Motion | 2 |
| Acrylic Sheet | Used as a Base to Attach Components | 1 |
| Nuts and Bolts | Used to Attach Parts to the Bot | 8 |
| Screws | Various Sized Screws Used to Attach Parts | 11 |
| RPLIDAR | Used to Guide the Robot and Judge Distances from Obstacles | 1 |
| Pi Camera | Used to Guide the Robot and Analyze Surroundings | 1 |

# Evaluation

## Future Additions
As we designed our robot, we made sure that we left space for future additions that would be used in other projects. These additions included a Lidar for navigation, a Pi Camera, and a Raspberry Pi Pico that checks the rotary encoders in the motor. Additionally, we found and 3D-printed an adjustable mount for the Pi Camera, and also created a reel to hold the long ribbon cable. This will ensure that all of our components are easily accessible in the future and have a place to be effectively mounted.

## Issues with Caster Wheels
Throughout the design process, the most common recurring issues have all been with the caster wheels. Initially, they were too high off the ground and caused the robot to not be level, so we used FreeCAD to create multiple platforms ranging from 5.5 to 6.4 millimeters. Eventually, we found that the 5.5 mm platforms were most effective and allowed the wheel to have more traction on a wide variety of terrains.

## Using ROS 
To run our robot, we needed to use ROS Humble, so we installed it on every teammate's personal laptop and the Raspberry Pi. Next, we acquired all of the needed libraries and installed the telep_twist_key package. After that, we created a shared GitHub repository for the group. A local package was created for use with the robot, and a listener template was used from GitHub to listen for input from the cmd_vel topic from the teleop_twist_key package. Teleop_twist_key allows input from the keyboard to change the values for the variables representing those keys, and it communicates the data with any other device with the same ROS domain. Therefore, we set the values for those variables within our code to have the robot perform different actions. Only values for linear and angular velocity are used; the table below details the actions performed based off those values. One final important thing to note is that we used the PhaseEnableRobot class (in the gpiozero library) to control each of the motors in our program.

| Function | Linear Velocity (x) | Angular Velocity (z) |
| --- | --- | --- |
| forward | Positive | Zero |
| forward_left | Positive | Positive |
| forward_right | Positive | Negative |
| left | Zero | Positive |
| right | Zero | Negative |
| backward | Negative | Zero |
| backward_left | Negative | Negative |
| backward_right | Negative | Positive |
| STOP | Zero | Zero |

## Adding autonomous driving
With the previous packages configured, we had the basic driving functionality needed to begin working on autonomous navigation using the Nav2 packages and the SLAM toolbox for Ros 2. Rviz was used to visualize lidar scans being processed by the slamtec RPLidar on the top of the robot. These readings allowed for an Rviz map which matched the environment that the lidar detected to be created. The Nav2 package provides a waypoint navigation system that can be used to navigate between points in the lidar map. A raspberry pi pico was used to read the actual rotation rate of each motor on our robot to publish a bot_odom topic which detailed the real position of our robot in the world. With these functionalities, the bot can autonomously navigate between two points in a pre-mapped area.

## Workflow of Navigation

## Factors Affecting Mapping and Navigation
As we were mapping out the hallway for future navigation, we ran into two main problems that were causing substantial error in the map. The first of these problems involved tire slipping due to low traction, which we remedied by removing the aluminum extrusion fram and adding two extra 2kg masses on top of the bot. This resulted in improved grip between the robot and the ground. The other main problem that we ran into was directional drift, which was caused by the slight unevenness of the wheels. To fix this, we used low driving speeds for the robot while mapping (about 6% speed) and gently nudged the robot along a straight path when it would begin to veer off course.

The next problem came when saving the map.

Navigation - 
Empty strings
People walking through and affecting the scans
Getting rid of initial doorway

## Summary
Overall, the experience of designing and running the robot has been enjoyable, and we have learned many things throughout the process. The primary knowledge that we gained was regarding ROS, as we learned all of the basics through multiple tutorials. Then, we were able to apply that knowledge using the teleop_twist_key package and drive the robot. We also gained more insight into the design process and found how various complications could come up. However, by using our problem-solving skills, we were able to find solutions including using using FreeCAD to print platforms and adding weather stripping to create protective bumpers. Lastly, we found how effectively planning and considering many features could result in a working project!

Here is an early video of "The Fourth Amigo" running! https://youtube.com/shorts/EfjXouigjik?feature=share
Here is the final video of "The Fourth Amigo" navigating through the hallway! https://youtu.be/RlqvqN4nuBk
