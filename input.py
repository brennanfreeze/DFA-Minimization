import random
import numpy as np


class DFA:
    def __init__(self, sigma, start, final, q, delta):
        self._sigma = sigma
        self._start = start
        self._final = final
        self._q = q
        self._delta = delta

    def sigma(self):
        return self._sigma
    
    def start(self):
        return self._start
    
    def final(self):
        return self._final
    
    def q(self):
        return self._q
    
    def delta(self):
        return self._delta


def create_random_dfa():
    random_range_state = random.randint(5, 15)
    states = np.arange(0, random_range_state)

    sigma = np.arange(0, random.randint(1, 5))
    num_transitions = len(sigma)
    delta = {}

    for state in states:

        for _ in sigma:

            transitions = {}
            for i in range(num_transitions):

                next_state = random.choice(states)
                transitions[i] = next_state

            delta[state] = transitions

    start_state = [0]
    final_states = \
    np.arange (
        random_range_state -
        random.randint(1, 3), \
        random_range_state
    )

    return DFA(sigma, start_state, final_states, states, delta)


def create_static_dfa():
    sigma = [0, 1]
    start_state = [0]
    final_states = [1, 2, 4]
    states = [0, 1, 2, 3, 4, 5]
    delta = {
        0: {
            0: 3,
            1: 1
        },
        1: {
            0: 2,
            1: 5
        },
        2: {
            0: 2,
            1: 5
        },
        3: {
            0: 0,
            1: 4
        },
        4: {
            0: 2,
            1: 5
        },
        5: {
            0: 5,
            1: 5
        },
    }
    return DFA(sigma, start_state, final_states, states, delta)
