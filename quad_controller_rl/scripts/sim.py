import numpy as np
from geometry_msgs.msg import Vector3, Point, Quaternion, Pose, Twist, Wrench

class Sim():
    def __init__(self):
        self.gravity = -9.81
        self.mass = 2
        self.drag = 0.3
        self.dt = 1/30.0
        
        cube_size = 300.0  # env is cube_size x cube_size x cube_size
        self.bounds_low  = np.array([- cube_size / 2, - cube_size / 2,         0])
        self.bounds_high = np.array([  cube_size / 2,   cube_size / 2, cube_size])
        
        self.time = 0
        self.position = np.zeros(3)
        self.velocity = np.zeros(3)
        self.lin_acc = np.zeros(3)
        
    def set_state(self, pose, vel):
        self.time = 0
        self.position = np.array([pose.position.x, pose.position.y, pose.position.z])
        self.velocity = np.array([vel.linear.x, vel.linear.y, vel.linear.z])
        self.lin_acc = np.zeros(3)
    
    def get_state(self):
        pose = Pose(position=Point(self.position[0], self.position[1], self.position[2]),
                    orientation=Quaternion(0,0,0,0))
        angular = Vector3(0, 0, 0)
        linear_acceleration = Vector3(self.lin_acc[0], self.lin_acc[1], self.lin_acc[2])
        
        return self.time, pose, angular, linear_acceleration
        
    def process_action(self, cmd):
        force = np.array([cmd.force.x, cmd.force.y, cmd.force.z])
        force += np.array([0,0,self.gravity*self.mass])
        v = np.linalg.norm(self.velocity)
        vhat = self.velocity/v
        force -= vhat*np.square(v)*self.drag
        
        self.lin_acc = self.dt*(force/self.mass)
        self.velocity += self.dt*(force/self.mass)
        self.position += self.dt*self.velocity
        self.time += self.dt
        
        self.position = np.clip(self.position, self.bounds_low, self.bounds_high)