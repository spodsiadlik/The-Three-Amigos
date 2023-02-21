(2%) An overview section to introduce your robot with the most highlighted functions and
features

(15%) A specification section to describe all the detailed features, including those listed in 2
Analyzed Features. You may want to attach the hardware configuration (all the dimensions
including screw holes), part list and wiring diagram here.

(15%) An experiment(analyzes) section to describe the methods of how you evaluate the
interested but not straightforward features and facts. Please reveal the results of your
experiments and/or analyzes.

(3%) A summary and discussion section to close up the report and share any interesting findings.

## Overview


## Analysis
Robot weight.

The weight of the robot was one of our initial concerns, and we consequently used lighter materials in the construction of the robot. We still used the aluminum extrusions for our base frame, but instead of using wood or metal for our second level, we used an acrylic sheet that would allow us to easily mount everything we needed. We also used a 3-D printer to print any extra additions we needed, including a mount for the PiCamera (which will be used in future projects), a base for the Lidar and RPi (using the same design as the one from last semester), and small platforms that allow us to lower our caster wheels to the same height as the skateboard wheels.   

Base dimensions (include the add-ons).

Max speed (linear, angular).
The wheel has a radius of 8.4 cm.

Payload capacity.



Battery (minimum) life span
When constructing the robot, we considered the battery life and decided to have two separate power supplies: one to power the motors and one to power the Raspberry Pi and the RPi Pico. Then, the batteries wouldn't be simultaneously drained by both components, and we could individually power each part. The first type of power supply uses three lithium ion batteries to power our motors, and we chose this specific method because the batteries were easily removable. Because of that, we wouldn't need to disassemble anything to recharge the batteries, and they would be much less dangerous that LiPo batteries. Our other power source would be an Anker Power Bank, which we could use to power the Pi and Pico. It would last much longer than the batteries, so it would need to be recharged less.

Finding capacity of Lithium Ion batteries, then determine how much power is used by the motors
OR Filluy charge the batteries and manually discharge them to 9V.


Safety Features
One of the most important considerations that we had while designing our robot was involving safety features, since we want to make sure that our bot is safe to use. We considered two different types of safety additions: physical and software features. The main physical safety feature that we included was bumpers made of weather 
stripping that could reduce damamge if the bot bumped into anything. It was placed strategically on the corners and sharper edges of the bot in order to maximize its effieciency.

Software safety features
-Key used to stop the bot
CTRL-C is used interrupt and stop the program

Physical safety features
-Weather Stripping to round off sharp edges
-Tying down cables

## Evaluation
Leaving space for future additions (Lidar, PiCamera, Pico)

PhaseEnableRobot class
ROS Workspace

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

## Summary


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
| Nuts and Bolts | Used to Attach Parts to the Bot | ~ |
| RPLIDAR | Used to Guide the Robot and Judge Distances from Obstacles | 1 |
| Pi Camera | Used to Guide the Robot and Analyze Surroundings | 1 |
