# import functions to create DFAs
from input import create_random_dfa, create_static_dfa, DFA
from collections import deque  # import deque data structure for queue operations
import copy  # import copy module for deep copying of DFA

def reachable_states(dfa):

    reachable_states = {dfa.start()[0]}
    new_states = {dfa.start()[0]}

    while new_states:
        temp = set()
        for q in new_states:
            for c in dfa.sigma():
                p = dfa.delta()[q][c]
                temp.add(p)
        new_states = temp - reachable_states
        reachable_states |= new_states

    new_q = list(reachable_states)
    new_delta = {}
    for q in new_q:
        new_delta[q] = {}
        for c in dfa.sigma():
            p = dfa.delta()[q][c]
            if p in reachable_states:
                new_delta[q][c] = p

    return DFA(sigma=dfa.sigma(), start=dfa.start(), final=dfa.final(), q=new_q, delta=new_delta)


def hopcroft_dfa_minimization(dfa):
    # create a copy of the input DFA
    w_dfa = copy.deepcopy(dfa)

    # separate the states into final and other states
    w_other = []
    w_final = []
    p_other = []
    p_final = []

    for i in range(len(w_dfa.q())):
        if (i in w_dfa.final()):
            p_final.append(i)
            w_final.append(i)
        else:
            p_other.append(i)
            w_other.append(i)

    # create initial partition and add to queue
    w = deque([w_other, w_final])
    p = [set(p_other), set(p_final)]

    # repeat until the queue is empty
    while (w):
        # remove a set A from the front of the queue
        a = w.popleft()
        # for each symbol c in the input alphabet
        for c in w_dfa.sigma():
            # create a set X of states that transition to A on symbol c
            x = set()
            for q_sub in w_dfa.q():
                if w_dfa.delta()[q_sub][c] in a:
                    x.add(w_dfa.delta()[q_sub][c])

            # for each set Y in the current partition P
            for y in p:
                # if Y intersects with X and the difference between Y and X is
                # nonempty
                if (len(y & x) >
                        0 and len(y - x) > 0):
                    # replace Y in partition P with the intersection of X and
                    # Y, and the difference of Y and X
                    p.remove(y)
                    p.append(y & x)
                    p.append(y - x)

                    # if Y is in the queue W, replace it with the new sets
                    if y in w:
                        w.remove(y)
                        w.append(y & x)
                        w.append(y - x)
                    # otherwise, add the set with the smaller cardinality to W
                    else:
                        if (len(y & x) <=
                                len(y - x)):
                            w.append(y & x)
                        else:
                            w.append(y - x)

    for i in p:
        if len(i) < 1:
            p.remove(i)
    print(p)

    


def main():

    test_0_dfa = create_static_dfa()

    test_1_dfa = create_random_dfa()

    hopcroft_dfa_minimization(reachable_states(test_1_dfa))

    return


if __name__ == "__main__":
    main()
