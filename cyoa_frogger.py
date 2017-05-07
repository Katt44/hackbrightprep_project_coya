""" 
Create Your Own Adventure  The Frogger Story
this story is mainly made to fill in space and serves the code

"""

#
def display_intro():
	print " You are Frogger, but why is it that you hate water so much you die?"

def intro_choice():
	print "Well it started like any day being green and a frog… (1)"
	print "It was a dark and murky day in forgo-land. (2)"
	choice = raw_input(" 1 or 2? ")
	choice = int(choice)
	return choice

	# happy begining or darker begining 
	if choice < 2:
		print "The sun was shining happy dumb rainbow colored frogs everywhere. Then pink frog, your current mate,  came up to you and said 'I am bored of all this rainbow glitz lets GTFO.'"
	else: 
		print "You were dumped for a faster brighter frog that loved water. This filled you with little froggy rage. You decide its a great idea to hunt your girlfriend and your competition down. You want to explain to them in a series of hops and jumps how stupid  they are."






#calls

display_intro()
intro_choice()