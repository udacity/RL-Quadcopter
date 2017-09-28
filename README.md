# DeepRL Quadcopter Controller

_Teach a Quadcopter How to Fly!_

In this project, you will design a Deep Reinforcement Learning agent to control several quadcopter flying tasks, including take-off, hover and landing.


# Table of Contents

- [Install](#install)
- [Download](#download)
- [Develop](#develop)
- [Submit](#submit)


# Install

This project uses ROS (Robot Operating System) as the primary communication mechanism between your agent and the simulation. You can either install it on your own machine ("native install"), or use a Udacity-provided Virtual Machine (recommended).

## ROS Virtual Machine

Download the compressed VM disk image and unzip it:

- Compressed VM Disk Image: [RoboVM_V2.1.0.zip](https://s3-us-west-1.amazonaws.com/udacity-robotics/Virtual+Machines/Lubuntu_071917/RoboVM_V2.1.0.zip)
- MD5 checksum: `MD5(Ubuntu 64-bit Robo V2.1.0.ova)= 95bfba89fbdac5f2c0a2be2ae186ddbb`

You will need a Virtual Machine player to run the VM, such as VMWare or VirtualBox. We recommend using [VMWare](http://www.vmware.com/). Open your VM player, and then "Open" / "Import" the VM disk image that you just unzipped (there are two other small configuration files in the zip archive that you may or may not need).

Configure the settings for your VM to allocate at least 2 processors and 4GB of RAM (more the merrier!). Now launch the VM, and follow the on-screen instructions for one-time setup steps.

- Username: `robo`
- Password: `robo-nd`

To open a terminal in your VM, press `Ctrl+Alt+T` (or `Ctrl+Option+T` on a Mac). This is where you will be able to execute your project code.

## ROS Native Install

If you choose to install ROS (Robot Operating System) on your own machine, it is recommended that you use Ubuntu 16.04 LTS as your operating system. To install ROS, please follow the instructions here: [ROS Installation](http://wiki.ros.org/kinetic/Installation)

_Note: This method is not supported by Udacity. If you have trouble performing a native install of ROS, please visit [ROS answers](http://answers.ros.org/questions/) or you can try troubleshooting your install with other students in the Udacity Robotics Slack community ([robotics.udacity.com](https://www.robotics.udacity.com)) in the **#ros** channel._


# Download

## Project Code

Clone this repository or download it where you have installed ROS (on the VM, or your local machine). This is where you will develop your project code. If you're using a VM, you can also share a folder on your file-system between the host and VM. That might make it easier for you to prepare your report and submit your project for review.

Wherever you download the code, we recommend the following folder structure (ROS has a fairly complicated build system, as you will see!):

- ~/catkin_ws/
  - src/
    - RL-Quadcopter/
      - quad_controller_rl/
        - ...

The root of this structure (`catkin_ws`) is a [catkin workspace](http://wiki.ros.org/catkin/workspaces), which you can use to organize and work on all your ROS-based projects (the name `catkin_ws` is not mandatory - you can change it to anything you want).

## Simulator

Download the Udacity Quadcopter Simulator, nicknamed **DroneSim**, for your host computer OS [here](https://github.com/udacity/RoboND-Controls-Lab/releases). 

_Note: If you are running ROS in a Virtual Machine (VM), you cannot use the simulator inside the VM. You have to use the simulator for your host operating system and connect it to your VM (see below)._

### Using the Simulator

If using the VM, inside the simulator's `_data` or `/Contents` folder, edit `ros_settings.txt` and set `vm-ip` to the VM's IP address and set `vm-override` to `true`. If not using a VM, no edit is necessary.

To find the ip of your VM, type `echo $(hostname -I)` into a terminal of your choice. Be aware that the ip address of your VM can change. If you are experiencing problems, be sure to check that the VM's ip matches that of which you have in `ros_settings.txt`.

To start the simulator, simply run the downloaded executable file.


# Develop

Starter code is provided in `quad_controller_rl/src/`:

- `rl_controller.py`: The controller gets raw position data from the simulation, prepares the state representation and reward, supplies them to the agent and passes back the agent's actions to the simulation.
- `rl_agent.py`: The agent is where you will implement your reinforcement learning algorithm. A sample agent is provided, which tries to learn using stochastic policy search (but performs very poorly!).

## Build

To prepare your code to run with ROS, you will first need to build it. This compiles and links different modules ("ROS nodes") needed for the project. Fortunately, you should only need to do this once, since changes to Python scripts don't need recompilation.

- Go to your catkin workspace (`catkin_ws/`):

```bash
$ cd ~/catkin_ws/
```

- Build ROS nodes:

```bash
$ catkin_make
```

- Enable command-line tab-completion and some other useful ROS utilities:

```bash
$ source devel/setup.bash
```

## Run

To run your project, start ROS with the `rl_controller.launch` file:

```bash
$ roslaunch quad_controller_rl rl_controller.launch
```

You should see a few messages on the terminal as different nodes get spun up. Now you can run the simulator, which is a separate Unity application (note that you must start ROS first, and then run the simulator). Once the simulator initializes itself, you should start seeing additional messages in your ROS terminal, indicating a new episode starting every few seconds. The quadcopter in the simulation should show its blades running as it gets control inputs from the agent, and it should reset at the beginning of each episode.

Tip: If you get tired of this two-step startup process, edit the `quad_controller_rl/scripts/drone_sim` script and enter a command that runs the simulator application. It will then be launched automatically with ROS!

_Note: If you want to learn more about how ROS works and how you can use it for robotics applications, you can take the [ROS Essentials](https://classroom.udacity.com/nanodegrees/nd209/parts/af07ae99-7d69-4b45-ab98-3fde8b576a16) module from Udacity's [Robotics Nanodegree Program](https://www.udacity.com/robotics)._

## Implement

Once you have made sure ROS and the simulator are running without any errors, and that they can communicate with each other, start modifying your code in `rl_agent.py`. Every time you make a change, you will need to stop the simulator (press `Esc` with the simulator window active), and shutdown ROS (press `Ctrl+C` in the terminal). Save your change, and `roslaunch` again.

While you are working on your agent code, open the project notebook for guidance (assuming you are in your catkin workspace):

```bash
$ jupyter notebook src/RL-Quadcopter/quad_controller_rl/notebooks/RL-Quadcopter.ipynb
```


# Submit

Complete the required sections in the notebook. Once done, save/export the notebook as a PDF (`RL-Quadcopter.pdf`). This will serve as your project report.

If you are enrolled in a Udacity program, you can submit your completed project for review. You can upload a zip file that includes the following:

- Project notebook with all sections completed (`RL-Quadcopter.ipynb`).
- PDF report (`RL-Quadcopter.pdf`, which can be an export of the notebook).
- Agent code (`rl_agent.py`).
- Controller code (`rl_controler.py`).
- Any other supporting code or other files used by your project (e.g. you can write different agents in separate files).
