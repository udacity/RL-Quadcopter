cmake_minimum_required(VERSION 2.8.3)
project(quad_controller_rl)

###########################
## General configuration ##
###########################

## Add support for C++11, supported in ROS Kinetic and newer
# add_definitions(-std=c++11)

##################
## Dependencies ##
##################

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED
  rospy
  message_generation
  std_msgs
  geometry_msgs
  nav_msgs
  dynamic_reconfigure
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

##################
## Python setup ##
##################

## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   EulerAngles.msg
# )

## Generate services in the 'srv' folder
add_service_files(
  FILES
#   SetFloat.srv
#   SetInt.srv
  SetPose.srv
#   SetPath.srv
#   GetPath.srv
)

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
#   std_msgs  # Or other packages containing msgs
  geometry_msgs
#   nav_msgs
)

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

## Generate dynamic reconfigure parameters in the 'cfg' folder
generate_dynamic_reconfigure_options(
  cfg/rl_controller_params.cfg
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES quad_controller_rl
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
  DEPENDS message_runtime
)

###########
## Build ##
###########

## Specify additional header file locations
## Declare C++ libraries/executables
## Add dependencies/links for above libraries/executables

#############
## Install ##
#############

## Note: All install targets should use catkin DESTINATION variables
## See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

#############
## Testing ##
#############

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
