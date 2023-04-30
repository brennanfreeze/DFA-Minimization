from collections import deque
from input import DFA


def hopcroft_minimization(delta, start_state, final_states):
    # Step 1: Partition the states into two sets, final and non-final
    F = set(final_states)
    Q = set(range(len(delta)))
    P = [F, Q - F]

    # Step 2: Initialize the split queue
    W = deque([F])
    if len(Q - F) > 0:
        W.append(Q - F)
    print(W)
    # Step 3: Process each set in the split queue
    while W:
        A = W.popleft()
        for c in set(delta[0]):
            X = set()
            for p in A:
                X.add(delta[p][c])
            for Y in P[:]:
                # Step 3.1: Split sets that intersect with X and differ from X
                if len(X & Y) > 0 and len(Y - X) > 0:
                    P.remove(Y)
                    P.append(X & Y)
                    P.append(Y - X)
                    if Y in W:
                        W.remove(Y)
                        W.append(X & Y)
                        W.append(Y - X)
                    else:
                        if len(X & Y) <= len(Y - X):
                            W.append(X & Y)
                        else:
                            W.append(Y - X)

    # Step 4: Build the new DFA
    d = {}
    new_start_state = None
    new_final_states = set()
    for i, pi in enumerate(P):
        for p in pi:
            if p == start_state:
                new_start_state = i
            if p in final_states:
                new_final_states.add(i)
        for c in set(delta[0]):
            X = set()
            for p in pi:
                X.add(delta[p][c])
            for j, pj in enumerate(P):
                if X <= pj:
                    d[i, c] = j
                    break

    return d, new_start_state, new_final_states
