"""Reinforcement Learning controller that sets state representation and rewards."""

import numpy as np
from rl_agent import RLAgent

class RLController:
    def __init__(self, gamma=0.9, alpha=0.01, epsilon=0.1):
        # Initialize agent
        self.agent = RLAgent(gamma, alpha, epsilon)
        self.reset_episode()

    def reset_episode(self):
        #print("RLController.reset_episode()")  # [debug]
        self.last_timestamp = 0.0
        self.last_position = 0.0

    def set_params(self, gamma, alpha, epsilon):
        self.agent.set_params(gamma, alpha, epsilon)

    def set_target(self, target):
        print("RLController.set_target({})".format(target))  # [debug]
        self.target = target

    def update(self, timestamp, position, done):
        # Compute delta_time
        delta_time = timestamp - self.last_timestamp
        self.last_timestamp = timestamp

        # Compute delta_position
        delta_position = position - self.last_position
        self.last_position = position

        # Check for t = 0 or dt = 0 (special case: send action = 0)
        if timestamp == 0.0 or delta_time <= 0.0:
            return 0.0
        
        # Prepare state vector
        velocity = delta_position / delta_time
        state = np.array([position, velocity, self.target]).reshape(1, -1)

        # Compute reward / penalty (note: current action's effect may be delayed)
        reward = -min(abs(self.target - position), 20.0)

        # Take one RL step, passing in current state and reward, and return action
        action = self.agent.step(state, reward, done)
        if done:
            self.reset_episode()
        return np.clip(action, -50.0, 50.0)  # clamp final action
