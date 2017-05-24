""" 
FROGGEH

"""
from random import randint 

#
def display_intro():
	"""Displays Intro text and story"""
	print  """ Welcome to the frog lands, you guessed it, you're a frog! Your name is Froggggeeeh \n  and your great great great great greeaaat uncle was the one and only THE FROGGER! \n which makes you pretty cool... """
	print "\n  but also means your life sucks"	
	print """\n Because of your ancestry your incapable of surviving pools of water, BUT!!\n Your impressive jumps and leg muscles really make the other frogs swoon. \n Your a young wreckless stupid frog out to prove to all of frog land that you can handle whatever it can throw at you. \n and so you quest!"""

def intro_choice():
	""" Presents to user 2 options, returns choice	"""
	print "Do take your quest slow and with caution? (1)"
	print "Or do you say screw it: \n I'll be taken by the wind and jump as far as I can and see where I land! \n Because Nothing can hurt me! (2)\n"
	choice = raw_input("So what will it be the 1st or 2nd choice?\n ")
	choice = int(choice)


	return choice
###### choice 1

def movement(x,y,max_x,max_y):
	""" User picks the first choice, def movement allows user to navigate through cautious matrix by manipulating indices."""
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
			print "thats not a valid choice, or you hit a wall"
			
	return (x,y) #note


def cautious_matrix():
 	""" cautious matrix function creates the matrix, sets default location, records location and notifies if user hits end of matrix.
	"""
	cautious_mat = [
	["Cautiously you look around at where you started. Which way hmm", "You wander around kinda lost but still super cool.\n", "you hit the edge and you know the only way to go is down or back the way you came."],
	["You know your getting closer but really have no idea where you are.", "the lake is somewhere around here", "You know your close and headed the right way."],
	["At this point your taking your sweet ass time getting but your formidable ego and pride wont let you stop here and now ", "Your so close you can just smell the death and the damp anxiety.", "you found the lake! You get there and your over come with panic. You forgot just how freaking huge the lake is. You just nope you way out of that."]]
	x = 0
	y = 0
	while True:
		#row= x  col = y
		print cautious_mat[x][y]
		x,y = movement(x,y,2,2)#note # while  in movement function contiunes here
		if x == 2 and y == 2:
			print cautious_mat[2][2]
			break


##### choice2
def make_wreckless_matrix():
	"""Creates wreckless matrix, randomly makes puddle true and sets a random num to flies	"""
	wreckless_mat = [{"text": "HAH Didn't land in water, you got this! you can even catch flies!\n", "puddle": False, "flies": None},
	{"text":"you start to get anxious but you over compensate for your fears with pride yelling \n 'Hah  another jump! all water fears me! I dont fear water!'\n ", "puddle": False, "flies": None},
	{"text":"You barely missed that last puddle but you managed to avoid it, but you ALIVE! You take in a deep breath in relief and ready yourself for the next jump. ", "puddle": False, "flies": None}]

#NOT MVP:
	# [{"text":"stuff4", "puddle": False, "flies": None},
	# {"text":"stuff5", "puddle": False, "flies": None},
	# {"text": "stuff 6", "puddle": False, "flies": None}],

	# [{"text":"stuff7", "puddle": False, "flies": None},
	# {"text": "stuff8", "puddle": False, "flies": None},
	# {"text":"stuff9", "puddle": False, "flies": None}]   #note

	
	
		

#def increment(item):#for location on matrix

####for puddle value
	for _ in range(1):
		x = randint(0,2)
		#y = randint(0,2) not MVP
		wreckless_mat[x]["puddle"] = True


# def new_dict_text_mat():
# 	wreckless_mat = make_wreckless_matrix()
# 	if wreckless_mat[x]["puddle"] == True:
# 		new_dict_text = wreckless_mat[x]["text"] = "works here"
# 		print new_dict_text
	

###### for flies value
	for dictionary in wreckless_mat:#note
		dictionary["flies"] = randint(0,3)			 
	return wreckless_mat


def random_user_jump():
	"""for the 2nd choice allows user to jump to random dictionary inside of wreckless matrix. then links to  subtract lifepoints method and add flies to life points functions"""
	puddle = False
	lifepoints = 3
	wreckless_mat = make_wreckless_matrix()
	print "You jump high in the air not sure where you will land"
	while True:
		xx  = randint(0,2)
		# yy = randint(0,2) not MVP
		position = wreckless_mat[xx]#[yy]#note
		jump_again = raw_input("jump again? yes or no \n")
		jump_again.lower()
		#print position["text"]
		if jump_again == "no" or jump_again == "n":
			break	
	
	 	if position["puddle"] == True:
	 		num_flies = position["flies"]
	 		print "You've landed in a puddle, shaking in terror you thrash and nearly drown yourself in panic but luckily this time the puddle was shallow .\n You lose a lifepoint.\n"
	 		print "You managed to eat " + str(num_flies) + " flies mid jump, it improved your health and confidence. \n"
	 	

	 		
	 		lifepoints = add_flies_to_lifepoints(xx,wreckless_mat, lifepoints)#note	
	 		lifepoints = subtract_life_points(position,wreckless_mat,lifepoints)#note
	 	
	 	elif position["puddle"] ==  False:
	 		print position["text"]

	 
 		if lifepoints <= 0:
 			break
 		elif lifepoints == 8:
 			print "You got this no puddle can stop you, you win at life!"
 			break
		

def subtract_life_points(position,wreckless_mat, lifepoints):
	"""for the 2nd choice everytime puddle is true this function subtracts 1 from lifepoints and if life points = 0 its game over	"""
	
	if position["puddle"] == True and lifepoints != 0:
		lifepoints -= 1

		#print  "Even tho you lost some life points, you have " + str(lifepoints) + " life points left."
	
	elif position["puddle"] == False and lifepoints != 0:
		print  "you have " + str(lifepoints) + " life points left."
	

	else:
		print "something went wrong" 

	if lifepoints == 0:#note
		print "You panic and die choking on water and fear. game over."

	return lifepoints

def add_flies_to_lifepoints(position,wreckless_mat, lifepoints):
	"""for second choice  this functions takes the number of flies and adds it to life points"""
	
	

	new_life_points = wreckless_mat[position]["flies"]
	lifepoints = lifepoints + new_life_points 
	#print "lifepoints: ", lifepoints
	#print "points ", points
	print "Current health status: ",lifepoints
	if lifepoints >= 3 :
		print "You got this! Your getting the hang of this and no stupid puddle can stop you!"
	elif  lifepoints <= 3:
		print "From the flies you've gained " + str(new_life_points) + " healthpoints!"





	return lifepoints


#######calls

def calls():
	"""This functions calles the other functions  and intros to each choice	"""
	display_intro()
	wreckless_mat = []#note
	choice = intro_choice()
	# if statement
	if choice == 1:
		print "You decide the lake would be the best place to prove your fearlessness. \n but where was it again?\n"
		cautious_matrix()

	elif choice == 2:
		print "You decide to test your limits and use your legs.\n "
		random_user_jump()
	else:
		print "Wrong! 1 or 2!!"
	

	

calls()





####### TESTS
# let's test stuff
# wm = make_wreckless_matrix()
# pos = wm[0][0]
# print "matrix"
# print wm
# result = subtract_life_points(pos, 3)

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







"""" Notes:
Working through understanding whats happening:

Line 45:

line 59:

line 78:

line 109:

line 120:

line 121:

line 140:

line 164:




"""



































