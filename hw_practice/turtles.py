from swampy.TurtleWorld import *



def draw_line(turtle, angle, start_x, start_y, line_length):
	"""
	Draws a line with specified turtle

	turtle: this is the turtle that will do the drawing
	angle: the angle in degrees where 0 degrees is East
	start_x: initialized line x-coordinate
	start_y: initialized line y-coordinate
	line_length: the length of the line that should be drawn
	"""
	#STEPS:

	#1. move the the approppriate starting location
	turtle.x = start_x
	turtle.y = start_y

	#2. turn to the appropriate angle
	turtle.lt(angle)

	#3. Put the pen down
	turtle.fd(line_length)

	#4. Walk forward appropriate number of steps

def my_square(turtle, angle, start_x, start_y, line_length):
	turtle.x = start_x
	turtle.y = start_y

	turtle.fd(line_length)
	turtle.rt(angle)
	turtle.fd(line_length)
	turtle.rt(angle)
	turtle.fd(line_length)
	turtle.rt(angle)
	turtle.fd(line_length)
	print line_length
	

def my_polygon(turtle, angle, start_x, start_y, line_length):
	turtle.x = start_x
	turtle.y = start_y

	turtle.fd(line_length)
	turtle.rt(angle)
	turtle.fd(line_length)
	turtle.rt(angle)
	turtle.fd(line_length)
	turtle.rt(angle)
	turtle.fd(line_length)
	turtle.rt(angle)
	turtle.fd(line_length)
	turtle.rt(angle)
	turtle.fd(line_length)
	turtle.rt(angle)
	turtle.fd(line_length)
	turtle.rt(angle)
	turtle.fd(line_length)

	print line_length

def my_circle(turtle, radius, start_x, start_y):
	turtle.x = start_x
	turtle.y = start_y
	turtle.pu()

	#turtle.fd(radius)
	turtle.pd()
	i = 0
	while i < 360:

		side_length = (2*3.14*radius) / 360
		
		turtle.fd(side_length)
		turtle.lt(10-i)
		turtle.fd(side_length)


		turtle.fd(side_length)
		turtle.lt(i)	
		print side_length
		print i
		i +=1

def my_name(turtle):
	turtle.x = 0
	turtle.y = 0

	#draw A
	turtle.lt(30)
	turtle.fd(50)
	turtle.rt(120)
	turtle.fd(50)
	turtl.lt(120)
	#space
	turtle.pu()
	turtle.fd(10)
	turtle.pd()
	#draw L
	turtle.lt(90)
	turtle.fd(40)
	turtle.lt(180)
	turtle.fd(40)
	turtle.lt(90)
	turtle.fd(25)

def snow_flake_side(turtle, length, level):
	"""draw a side of the snowflake curve with side length
	length and recursion depth of level """

	if level == 0:
	 	turtle.fd(length/0.3)
	 	turtle.rt(60)
	 	turtle.fd(length/0.3)
	 	turtle.lt(120)
	 	turtle.fd(length/0.3)
	 	turtle.rt(60)
	 	turtle.fd(length/0.3)
	else:
		turtle.lt(90)
		snow_flake_side(turtle, length, (level-1))
	 	turtle.rt(60)
	 	snow_flake_side(turtle, length, (level-1))
	 	turtle.lt(120)
	 	snow_flake_side(turtle, length, (level-1))
	 	turtle.rt(60)
	 	snow_flake_side(turtle, length, (level-1))
	 	

def tree(turtle, turtlex, turtley, branch_length, level):

	turtle.x = turtlex
	turtle.y = turtley

	#base case is drawing the "trunk" of the tree
	if level == 0:
		turtle.lt(90)
		turtle.fd(branch_length)
	
	#draw a line branch_length*0.6 at 30 deg to the left of base case
	#back up branch_length/3
	#turn to the right 40 deg. draw branch branch_length*0.64
	else:
		turtle.x = turtlex
		turtle.y = turtley
		print turtle.x
		print turtle.y
	"""
		turtle.fd(2*branch_length/3)
		print (2*branch_length/3)
		turtle.rt(30)
		turtle.fd(branch_length*0.64)

		turtlex = turtle.x
		turtley = turtle.y
		
	"""
	tree(turtle, turtlex, turtley, branch_length, level-1)





world = TurtleWorld()
beth = Turtle();

beth.set_color('green');
beth.set_pen_color('blue');
beth.delay = 0.01
#my_circle(beth, 1000, 0,0)
#my_square(beth,90,0,0,400)
#snow_flake_side(beth, 7, 12)
tree(beth, 0,0, 100, 2)
#my_name(beth)

wait_for_user()
beth.set_pen_color('green');
#my_polygon(beth,45,0,0,100)
wait_for_user()

