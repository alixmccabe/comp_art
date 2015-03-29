def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    import random

    import math_functions

    function = []
    list_x = []
    list_y = []

    list_functions = ["prod","avg","cos_pi","sin_pi","x","y"]
    
    list_index = 0

    while list_index < max_depth/6:
        
        list_functions = list_functions + list_functions
        random.shuffle(list_functions)
        list_index += 1

    #shuffles the list of functions so that it's randomized
    
    #generates the first function in the return list randomly
    function = [list_functions[1]]
    x = list_functions[0]
    i = 0
    i2 = 0

    #generate list of random functions the length of  min_depth for list_x
    while i < min_depth:
        list_x.append([list_functions[i]])
        i += 1

    random.shuffle(list_functions)

    #generate list of random functions the length of  min_depth for list_y
    while i2 < min_depth:
        list_y.append([list_functions[i2]])
        i2 += 1


    #return grouped lists in the format required
    return function + [list_x[0:len(list_x)/2]] + [list_x[len(list_x)/2:len(list_x)]] + [list_y[0:len(list_y)/2]] + [list_y[len(list_y)/2:len(list_y)]

    """
    for i in range(0,min_depth):
        print i
        print list_x[0]
        print list_functions[0]
        list_x[i] = list_functions[i]
        print list_functions

    for i in range(0,min_depth):
        list_y[i] = list_functions[i]   
"""

    #return list_y.append(list_x.append(list_functions))

print build_random_function(7,9)