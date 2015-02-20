"""This program generates random functions to create art
Author: ALIX McCABE
"""

import random
from PIL import Image


def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth 

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    #case 1: you're building a function not with x and y, the max and min are both positive
    #case 2: min is below zero, you can stop with x or y, or use anything
    #case 3: max and min are below zero must stop with x or y
    
    list_functions = ["cos_pi","sin_pi","cubed","bound_log","prod","avg","x","y"]


    import random
    import math_functions
    #we'll need these bits of code later in the script!
    
    #setting up case 1
    if min_depth > 0 and max_depth > 0:

        index = random.randint(0,4)

    #setting up case 2
    elif min_depth <= 0 and max_depth >0:

        index = random.randint(0,6)

    #setting up case 3
    else:

        index = random.randint(6,7)

    #we need to discern whether the function we're using takes one or two inputs
    #that's what this series of if-statements is for!
    if index in [0,1,2,3]:
        return[list_functions[index],build_random_function(min_depth-1,max_depth-1)]

    elif index == 4 or index == 5:
        return[list_functions[index],build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
    
    else:

        return[list_functions[index]]



def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value
        prod: takes the product of constants x and y
        avg: takes the average value of constands x and y
        cos_pi: takes the cos of x times pi
        sin_pi: takes the sin of x times pi
        cubed: returns the cube of b
        bound_log: a recursive function that scales the log of a to be between -1 and 1

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    import math
    a = x
    b = y

    def prod(a,b):
        """
        takes the product of constants x and y
        """
        return a*b
      
    def avg(a,b):
        """
        avg: takes the average value of constands x and y
        """
        return 0.5*(a+b)

    def cos_pi(a) :
        """
        cos_pi: takes the cos of x times pi
        """
        return math.cos(math.pi*a)

    def sin_pi(a):
        """
        sin_pi: takes the sin of x times pi
        """
        return math.sin(math.pi*a)

    def x(a,b):
        """
        returns constant a
        """
        return a

    def y(a,b):
        """
        returns constant b
        """
        return b

    def cubed(b):
        """
        cubed: returns the cube of b
        """
        #if a is i the interval -1:1, a^3 will be, as well!
        return b**3

    def bound_log(a):
        """
        bound_log: a recursive function that scales the log of a to be between -1 and 1
        """
        # this is a recursive function that takes a log of a and reduces it until it's between -1 and 1!
        bound = (math.log10(a))
        #checking to see if it satisfyies our requirements
        if bound >= -1 and bound <=1:
            return bound

        #the base case for this recursive function is that the log is between -1 and 1
        else:
            reduced = bound/10
            #print bound_log(reduce_log)
            return bound_log(reduced)   

    if f == ["x"]:
        return a
    elif f == ["y"]:
        return b
    else:
        if f[0] == "sin_pi":
            return sin_pi(evaluate_random_function(f[1],a,b))

        elif f[0] == "cos_pi":
            return cos_pi(evaluate_random_function(f[1],a,b))

        elif f[0] == "cubed":
            return cos_pi(evaluate_random_function(f[1],a,b))

        elif f[0] == "bound_log":
            return cos_pi(evaluate_random_function(f[1],a,b))        

        elif f[0] == "avg":
            return avg(evaluate_random_function(f[1],a,b),evaluate_random_function(f[2],a,b))

        elif f[0] == "prod":
            return prod(evaluate_random_function(f[1],a,b),evaluate_random_function(f[2],a,b))


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    input_interval = float(input_interval_end - input_interval_start) #gives us the initial interval
    output_interval = float(output_interval_end - output_interval_start) #the interval that we're mapping to

    mapped = (((val - input_interval_start) * output_interval)/input_interval) + output_interval_start
    
    """
    We get these equations because we know that the ratio of the input_interval to the output_interval has to equal
    the ratio of (output_val - output_interval_start) to (val - input_interval_start)
    """
    return mapped

def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


"""
I got rid of the "test_image" function because it was 
unnecessary in the final iteration of my code
"""

def generate_art(filename, x_size=700, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 700 by 350)
    
    red_function = ["x"]
    green_function = ["y"]
    blue_function = ["x"]
    """

    # Functions for red, green, and blue channels - where the magic happens!

    red_function = build_random_function(7,9)
    print red_function
    green_function = build_random_function(7,9)
    print green_function
    blue_function = build_random_function(7,9) 
    print blue_function

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (

                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),    
                    color_map(evaluate_random_function(blue_function, x, y))

                    )

    im.save(filename)


def random_name():
    """
    This function returns a random name for each new art file and checks if that name
    already exists
    If the name exists, it generates a new name for the file

        name: the randomly generated name of the function composed of a repeated vowel (beta) 
        and a repeated consonent (alpha)

    """

    import random
    import os.path

    i = 0

    alpha = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    beta = ['a','e','i','o','u']
    
    random.shuffle(alpha)
    random.shuffle(beta)
    
    name = alpha[1] + beta[1] + beta[1] + alpha[1]

    if os.path.isfile(name) == True:
        return random_name()
    else:
        return name

generate_art(random_name()+".png")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
