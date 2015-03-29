import math

def check(a,b):

	"""
		for i in range(0,10,1):
			print math.fmod(1,i/10) 
			print i/10
		#if math.fmod(1,(i/10)) < -1:

	print check()


	print math.log10(math.sin(math.pi))

    print prod(a,b) = a*b
    print avg(a,b) = 0.5*(a+b)
    print cos_pi(a) = cos(pi*a)
    print sin_pi(a) = sin(pi*a)
    print x(a,b) = a
    print y(a,b) = b
"""

def bound_log(a,b):
 
	bound = (math.log10(a))
	#checking to see if it satisfyies our requirements
	if bound >= -1 and bound <=1:
		return bound

	#the base case for this recursive function is that the log is between -1 and 1
	else:
		reduced = bound/10
		#print bound_log(reduce_log)
		return bound_log(reduced,0)


	"""
	if bound_log >= 1 or bound_log <= -1:
		bound_log = bound_log/10
		bound_log(bound_log)
		if bound_log <= -1 and bound_log <=1:
			return bound_log
			"""


print bound_log(100,100)