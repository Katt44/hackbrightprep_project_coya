""" 
FROGGEH
cyoa frogger vs frogtesting, frog testing was used to test  making smaller functions and linking them


"""
from random import randint 

#
def display_intro():
	print  """ Welcome to the frog lands, you guessed it, you're a frog! Your name is Froggggeeeh \n  and your great great great great greeaaat uncle was the one and only THE FROGGER! \n which makes you pretty cool... \n  but also means your life sucks\n Because of your ancestry your incapable of surviving pools of water, BUT!!\n Your impressive jumps and leg muscles really make the other frogs swoon. \n Your a young wreckless stupid frog out to prove to all of frog land that you can handle whatever it can throw at you. \n and so you quest!
	 """

def intro_choice():
	print "Do take your quest slow and with caution? (1)"
	print "Or do you say screw it! I'll be taken by the wind and jump as far as I can! and see where I land! Nothing can hurt me! (2)"
	choice = raw_input(" 1 or 2? ")
	choice = int(choice)


	return choice
###### choice 1

def movement(x,y,max_x,max_y):
	while True:
		direction = raw_input("left, right, up, down, or stop ")
		direction = direction.lower()
		if direction == "right" or direction == "r" and y != max_y:
			y += 1
			break
		elif direction == "left" or direction == "l" and y != 0:
			y -= 1
			break

		elif direction == "down" or direction == "d" and x != max_x:
			x += 1
			break
		elif direction == "up" or direction == "u" and x != 0:
			x -= 1
			break
		elif direction == "stop" or direction == "s":
			print "stopping game"
			exit()
		else:
			print "thats not a valid choice"
			
	return (x,y) #tuple


def cautious_matrix():
 	print "this works!"
# 	#I want user to be able to move up down and left and right
	cautious_mat = [["Cautiously you look around at where you started", "ro1 col2", "row1 col3"],
	["row2col1", "row2 col2", "row2 col3"],
	 ["row3 col1", "row3 col2", "row3 col3"]]
	x = 0
	y = 0
	while True:
		#row= x  col = y
		print cautious_mat[x][y]
		x,y = movement(x,y,2,2) # while  in movement function contiunes here
		if x == 2 and y == 2:
			print "end of the line!"
			break
#def catch_flies():
	# What i want this function to do: 
	# I want to


##### choice2
def make_wreckless_matrix():
	
	wreckless_mat = [{"text":"stuff1", "puddle": False, "flies": None},
	{"text": "stuff 2", "puddle": False, "flies": None},
	{"text":"stuff3", "puddle": False, "flies": None}]

	# [{"text":"stuff4", "puddle": False, "flies": None},
	# {"text":"stuff5", "puddle": False, "flies": None},
	# {"text": "stuff 6", "puddle": False, "flies": None}],

	# [{"text":"stuff7", "puddle": False, "flies": None},
	# {"text": "stuff8", "puddle": False, "flies": None},
	# {"text":"stuff9", "puddle": False, "flies": None}]

	
	
		

#def increment(item):#for location on matrix
	for _ in range(1):
		x = randint(0,2)
		#y = randint(0,2)
		wreckless_mat[x]["puddle"] = True

		#testing
		#print x
		#print y

	# for flies value
	for dictionary in wreckless_mat:
		dictionary["flies"] = randint(0,3)			 
	return wreckless_mat


def random_user_jump():
	#random  square
	puddle = False
	lifepoints = 3
	wreckless_mat = make_wreckless_matrix()
	print "You jump high in the air not sure where you will land"
	while True:
		xx  = randint(0,2)
		# yy = randint(0,2)
		posistion = wreckless_mat[xx]#[yy]
		jump_again = raw_input("jump again? yes or no ")
		jump_again.lower()
		if jump_again == "no" or jump_again == "n":
			break	
	
	 	if posistion["puddle"] == True:
	 		#print posistion["text"]
	 		num_flies = posistion["flies"]
	 		print "There are " + str(num_flies) + " flies left."
	 		if num_flies > 0:
	 			lifepoints = add_flies_to_lifepoints(xx,wreckless_mat, lifepoints)	
	 		lifepoints = check_life_points(posistion,wreckless_mat,lifepoints)
	 		if lifepoints <= 0:
	 			break
	 	else:
	 		print "No Puddle! You do not drown today!"
		

# working on life points, almost working
# I need to connect this to the while loop some how so that the user can jump again
# and lifepoints are kept track of and shown

def check_life_points(posistion,wreckless_mat, lifepoints):
	
	if posistion["puddle"] == True and lifepoints != 0:
		lifepoints -= 1
		print "You've landed in a puddle you start to drown! and lose a life!"
		print  "you have " + str(lifepoints) + " life points left."
	
	elif posistion["puddle"] == False and lifepoints != 0:
		print  "you have " + str(lifepoints) + " life points left."
	

	else:
		print "something went wrong" 
	if lifepoints == 0:
		print "game over you drowned"
	return lifepoints

def add_flies_to_lifepoints(posistion,wreckless_mat, lifepoints):
	# used to test :print "HERE",posistion,lifepoints
	
	print "Current health status: ",lifepoints

	new_life_points = wreckless_mat[posistion]["flies"]
	# for dictionary in wreckless_mat:
	# 	new_life_points = dictionary["flies"] 
	lifepoints += new_life_points 
	print "You've gained " + str(new_life_points) + " healthpoints!"





	return lifepoints

"""
What I want to happen here is I want the user to have a starting life of 5 points
and every time puddle is true i want life points to go down by 1  and when it hits zero its game over.
not sure how to connect  it.
""" 


	#calls

def calls():
	display_intro()
	wreckless_mat = []
	# if you wanna use another variable inside anothe function this is how
	choice = intro_choice()
	# if statement
	if choice == 1:
		print "The sun was shining happy dumb rainbow colored frogs everywhere. Then pink frog, your current mate,  came up to you and said 'I am bored of all this rainbow glitz lets GTFO.'"
		cautious_matrix()

	else:
		print "You were dumped for a faster brighter frog that loved water. This filled you with little froggy rage. You decide its a great idea to hunt your girlfriend and your competition down. You want to explain to them in a series of hops and jumps how stupid  they are."
		random_user_jump()
	

	

calls()





####### TESTS
# let's test stuff
# wm = make_wreckless_matrix()
# pos = wm[0][0]
# print "matrix"
# print wm
# result = check_life_points(pos, 3)

# print result

# test movement

#mov = movement(0,0,2,2)

#print mov
#print caut

# let's test cautious matrix
#caut = cautious_matrix()
# wm = make_wreckless_matrix()
# wp = add_flies_to_lifepoints(wm,2)
# add_flies_to_lifepoints(wm,lp)











































