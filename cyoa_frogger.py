""" 
Create Your Own Adventure  The Froggeh Story
this story is mainly made to fill in space and serves the code

"""
from random import randint 

#
def display_intro():
	print " You are Frogger, but why is it that you hate water so much you die?"

def intro_choice():
	print "Well it started like any being green and a frog...  1())"
	print "It was a dark and murky day in forgo -land. (2)"
	choice = raw_input(" 1 or 2? ")
	choice = int(choice)

	
	# for choice should  keep it like this or should i separate it into another function?
	# will this allow me to use this  choice later?
	return choice
def movement(x,y,max_x,max_y):
	while True:
		direction = raw_input("left, right, up, down ")

		if direction == "right" and  y != max_y:
			y += 1
			break
		elif direction == "left" and y != 0:
			y -= 1
			break

		elif direction == "down" and x != max_x:
			x += 1
			break
		elif direction == "up" and x != 0:
			x -= 1
			break
		else:
			print "thats not a valid choice"
	return (x,y) #tuple


def happy_matrix():
 	print "this works!"
# 	#I want user to be able to move up down and left and right
	hap_mat = [["this is here yyay", "hello", "yup"],["meow", "purr", "hiss"], ["wolf", "howl", "growl"]]
	x = 0
	y = 0
	while True:
		#row= x  col = y
		print hap_mat[x][y]
		x,y = movement(x,y,2,2)

def sad_matrix():
	lifepoints = 5
	puddle = False
	# row_x = randint(0,3)
	# col_y = randint(0,3)
	# sad_mat =  [["what", "is", "happening"],["hello", "there", " !! "],["good ", "bye", "farewell"]]
	# print sad_mat[row_x][col_y] # this is finding the location and printing it
	#print "this works!"
	sad_mat = [[{"text":"stuff1", "puddle": False},{"text": "stuff 2", "puddle": False},{"text":"stuff3", "puddle": False}],
	[{"text":"stuff4", "puddle": False},{"text":"stuff5", "puddle": False},{"text": "stuff 6", "puddle": False}],
	[{},{},{}]]
	for i in range(4):
		x = randint(0,3)
		y = randint(0,3)
		sad_mat[x][y]["puddle"] = True

	if puddle == True and lifepoints != 0:
		lifepoints -= 1
		print  "you have" + lifepoints + " life points left."
	elif puddle == False and lifepoints != 0:
		print  "you have" + lifepoints + " life points left."
	elif lifepoints == 0:
		print "game over"
	else:
		print "something went wrong" 


"""
What I want to happen here is I want the user to have a starting life of 5 points
and every time puddle is true i want life points to go down by 1  and when it hits zero its game over.
not sure how to connect  it.
"""




		


	#calls

def calls():
	display_intro()
	# if you wanna use another variable inside anothe function this is how
	choice = intro_choice()
	# if statement
	if choice == 1:
		print "The sun was shining happy dumb rainbow colored frogs everywhere. Then pink frog, your current mate,  came up to you and said 'I am bored of all this rainbow glitz lets GTFO.'"
		happy_matrix()

	else:
		print "You were dumped for a faster brighter frog that loved water. This filled you with little froggy rage. You decide its a great idea to hunt your girlfriend and your competition down. You want to explain to them in a series of hops and jumps how stupid  they are."
		sad_matrix()
	


calls()
