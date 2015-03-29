def sum(n):
	x = 0
	for i in range(n + 1):
		x = x + i
	return x
def recursive_sum(n):
	if n == 1:
		return 1
	else:
		return recursive_sum(n-1) + n

#print recursive_sum(5)

def recursive_fib(n):
	if n < 0:
		return 0
	if n==2:
		return 1
	elif n==1:
		return 1
	else:
		return recursive_fib(n-2) + recursive_fib(n-1)

for n in range(5):
	#print recursive_fib(n)

	"""
	put n+2 inside of n+1 inside of n
	base case: single random function, non-nested inside another function
	"""

def build_random_function(min_depth,max_depth):
	import random
	import math_functions

	list_x = []

import random

"""
def random_list(n,list_x):
	list_x = ['x']*n
	list_functions = ["prod","avg","cos_pi","sin_pi","x","y"]

	random.shuffle(list_functions)
	list_functions
		print list_x[i]
		print list_functions[i]
	
	list_x[i] = list_functions[i]
"""
		
def random_func(n):

	import random

	list_x = ["q"]*n
	list_functions = ["prod","avg","cos_pi","sin_pi","x","y"]

	for i in range(n):
		
		random.shuffle(list_functions)
		list_x[i] = list_functions[0]		

	return list_x
	
def random(n):
	import random
	#print random_func(10) 
	list_functions = ["prod","avg","cos_pi","sin_pi","x","y"]
	random.shuffle(list_functions)
	rando = list_functions[1]

	def of_x(n,rando):

		#list_x = ["x"]*n

		#for i in range(n):
		#	list_x[i] = list_x[i] + random.shuffle(list_x)[i]

		if n == 0:
			return 0

		if n > 0:
			return of_x(n-1).append(of_x(n))

	return of_x(n,rando)

print random_func(10)