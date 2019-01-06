import numpy as np
import itertools


PUZZLE = np.array([
    [0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
])


def move_length():
    return sum(PUZZLE.shape) + 1


def move_list():
    return list(range(move_length()))


def make_move(state, i):
    if i < PUZZLE.shape[0]:
        for j in range(PUZZLE.shape[1]):
            state[i][j] = 0 if state[i][j] == 1 else 1
    elif i == PUZZLE.shape[0]:
        i -= 1
        j = 0
        while i >= 0 and j < PUZZLE.shape[1]:
            state[i][j] = 0 if state[i][j] == 1 else 1
            i -= 1
            j += 1
    elif i > PUZZLE.shape[1] and i < move_length():
        i -= PUZZLE.shape[0] + 1
        for j in range(PUZZLE.shape[0]):
            state[j][i] = 0 if state[j][i] == 1 else 1
    else:
        raise ValueError('wtf?')
    return state


def make_sol(sol):
    state = PUZZLE.copy()
    for i in sol:
        state = make_move(state, i)
    return state


def check(state):
    return np.all(state == 1)


def solver(n):
    for sol in itertools.product(move_list(), repeat=n):
        state = make_sol(sol)
        if check(state):
            return sol
    return None

def inc_solver(limit=10, greedy=False):
    rv = []
    for i in range(1, limit):
        print(i)
        res = solver(i)
        if res is not None:
            if not greedy:
                return res
            else:
                rv.append(res)
                continue
    return rv


print(inc_solver())
# print(solver(4))
