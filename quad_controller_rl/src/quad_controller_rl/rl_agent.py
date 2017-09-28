"""Reinforcement Learning agents for controlling a quadcopter."""

import numpy as np
from scipy.stats import norm
from collections import deque

import sklearn.pipeline
import sklearn.preprocessing
from sklearn.kernel_approximation import RBFSampler

class RLAgent:
    """Sample Reinforcement Learning agent."""

    def __init__(self, gamma=0.9, alpha=0.01, epsilon=0.1):
        print("RLAgent(gamma={}, alpha={}, epsilon={})".format(gamma, alpha, epsilon))  # [debug]

        # Parameters
        self.set_params(gamma=gamma, alpha=alpha, epsilon=epsilon)

        # Feature transformers
        self.scaler = None  # will be initialized when we see the first state
        self.featurizer = None

        # Model
        self.w = None  # will be initialized when we see the first state
        self.best_w = None
        self.best_score = -np.inf
        self.noise_scale = 0.1

        # Other variables
        self.reset_episode()

    def reset_episode(self):
        #print("RLAgent.reset_episode()")  # [debug]
        self.last_state = None
        self.last_action = None
        self.total_reward = 0.0
        self.count = 0

    def set_params(self, gamma, alpha, epsilon):
        print("RLAgent.set_params(gamma={}, alpha={}, epsilon={})".format(gamma, alpha, epsilon))  # [debug]
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon

    def step(self, state, reward, done):
        # Initialize feature transformers (one time)
        if self.scaler is None or self.featurizer is None:
            observation_examples = np.array([[np.random.uniform(0.0, 300.0), np.random.normal(0.0, 25.0), np.random.uniform(0.0, 300.0)] for x in range(1000)])
            self.scaler = sklearn.preprocessing.StandardScaler()
            self.scaler.fit(observation_examples)

            self.featurizer = sklearn.pipeline.FeatureUnion([
                    ("rbf1", RBFSampler(gamma=5.0, n_components=5)),
                    ("rbf2", RBFSampler(gamma=2.0, n_components=5)),
                    ("rbf3", RBFSampler(gamma=1.0, n_components=5)),
                    ("rbf4", RBFSampler(gamma=0.5, n_components=5))
                    ])
            self.featurizer.fit(self.scaler.transform(observation_examples))

        # Transform state
        state = self.featurizer.transform(self.scaler.transform(state))

        # Initialize parameters (one time)
        if self.w is None:
            self.w = np.random.normal(size=state.shape)

        # Choose an action
        action = self.act(state)
        
        # Save experience / reward
        if self.last_state is not None and self.last_action is not None:
            self.total_reward += reward
            self.count += 1

        # Learn, if at end of episode
        if done:
            self.learn()
            self.reset_episode()
        
        self.last_state = state
        self.last_action = action
        return action

    def act(self, state):
        action = norm.rvs(loc=float(np.dot(state, self.w.T)), scale=0.1, size=1)  # single variable
        #print("RLAgent.act(): action = {}".format(action))  # [debug]
        return action

    def learn(self):
        # Learn by random policy search, using a reward-based score
        score = self.total_reward / float(self.count) if self.count else 0.0
        if score > self.best_score:
            self.best_score = score
            self.best_w = self.w
            self.noise_scale = max(0.5 * self.noise_scale, 0.01)
        else:
            #self.w = self.best_w
            self.noise_scale = min(2.0 * self.noise_scale, 4.0)

        self.w += self.noise_scale * np.random.normal(size=self.w.shape)  # equal noise in all directions
        print("RLAgent.learn(): score = {} (best = {}), noise_scale = {}".format(score, self.best_score, self.noise_scale))  # [debug]
        print(self.w)  # [debug]
