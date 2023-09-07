import random

class TicTacToeAI:
    def __init__(self, epsilon=0.1, alpha=0.3, gamma=0.9):
        self.q_table = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def get_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.get_possible_actions(state))
        else:
            return self.get_best_action(state)

