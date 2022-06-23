# utilities.py - AIFCA utilities
# dependency needed for agents.py
# AIFCA Python3 code Version 0.7.1 Documentation at http://aipython.org


# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en


import random


class Displayable(object):
    max_display_level = 4   # can be overridden in subclasses

    def display(self, level, *args, **nargs):
        """print the arguments if level is less than or equal to the
        current max_display_level.
        level is an integer.
        the other arguments are whatever arguments print can take.
        """
        if level <= self.max_display_level:
            print(*args, **nargs)  # if error you are using Python2 not Python3


def argmax(gen):
    """gen is a generator of (element,value) pairs, where value is a real.
    argmax returns an element with maximal value.
    If there are multiple elements with the max value, one is returned at random.
    """
    maxv = float('-Infinity')       # negative infinity
    maxvals = []      # list of maximal elements
    for (e, v) in gen:
        if v > maxv:
            maxvals, maxv = [e], v
        elif v == maxv:
            maxvals.append(e)
    return random.choice(maxvals)

# Try:
# argmax(enumerate([1,6,3,77,3,55,23]))


def flip(prob):
    """return true with probability prob"""
    return random.random() < prob


def dict_union(d1, d2):
    """returns a dictionary that contains the keys of d1 and d2.
    The value for each key that is in d2 is the value from d2,
    otherwise it is the value from d1.
    This does not have side effects.
    """
    d = dict(d1)    # copy d1
    d.update(d2)
    return d


def test():
    """Test part of utilities"""
    assert argmax(enumerate([1, 6, 55, 3, 55, 23])) in [2, 4]
    assert dict_union({1: 4, 2: 5, 3: 4}, {5: 7, 2: 9}) == {1: 4, 2: 9, 3: 4, 5: 7}
    argmax(enumerate([1,6,3,77,3,55,23]))
    
    from agentEnv import Rob_body, Rob_env
    from agentMiddle import Rob_middle_layer
    from agentTop import Rob_top_layer,Plot_env

    #1.(a)
    #env = Rob_env({((20,0),(30,20)), ((70,-5),(70,25))})
    #body = Rob_body(env)
    #middle = Rob_middle_layer(body)
    #top = Rob_top_layer(middle)

    #try:
    #pl=Plot_env(body,top)
    #top.do({'visit':['o109','storage','o109','o103']})
    # You can directly control the middle layer:
    #middle.do({'go_to':(30,-10),'timeout':200})
    #top.do({'visit': ['mail']})
    #middle.do({'go_to': (0, 0), 'timeout': 200})
    #middle.do({'go_to': (20, 1), 'timeout': 200})

    #I think that, if we put as final destination one coordinate that makes contact with one of the barrier u make it crash
    #It also makes the shape of a rat smoking.


    #1.(b) Robot Trap for which the current controller cannot escape:
    trap_env = Rob_env({((10,-21),(10,0)), ((10,10),(10,31)), ((30,-10),(30,0)),
    ((30,10),(30,20)), ((50,-21),(50,31)), ((10,-21),(50,-21)),
    ((10,0),(30,0)), ((10,10),(30,10)), ((10,31),(50,31))})
    trap_body = Rob_body(trap_env,init_pos=(-1,0,90))
    trap_middle = Rob_middle_layer(trap_body)
    trap_top = Rob_top_layer(trap_middle,locations={'goal':(71,0)})

    # Robot trap exercise:
    pl=Plot_env(trap_body,trap_top)
    trap_middle.do({'go_to': (0, -30), 'timeout': 200})
    trap_middle.do({'go_to': (70, -30), 'timeout': 200})
    trap_body.do({'steer':'left'})
    trap_top.do({'visit':['goal']})


    print("Passed unit test in utilities")


if __name__ == "__main__":
    test()
