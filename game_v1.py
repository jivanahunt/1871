#!/usr/local/bin/python
# coding: latin-1

# def set_up:
# 	print "What's your first name?"
# 		name = raw_input("> ")
# 	print "What's your gender? Please type in M or F"
# 		input = raw_input("> ")
# 	if "M" in input:
# 		gender = "he"
# 	elif "F" in input:
# 		gender = "she"
# 	else:
# 	 "1871 was as gender varied as 2019, please try again and choose between M and F" 

def start():
# sandboxed
	print "It's 1871 and the Prussians are about to besiege Paris. You can choose to either:"

	options = ('"1" - flee to the South with the rest of your family\n'
	'"2" - take up arms and join the militia to protect Paris\n'
	'"3" - carry on with baking bread (you don\'t think the Germans will stay for very long)')

	print options

	while True:
		decision = raw_input("> ")

		if decision == "1":
			print ("It was very close but you managed to escape the Prussians by leaving before the break "
			"of dawn, and once you passed Anvers you took a train to go South to some small village "
			"near Nice where you open a little café, go to the beach every morning, meet your significant "
			"other and make family with 5 children and to feed them all you work like a horse for the "
			"rest of your life.")
			exit(0)
		elif decision == "2":
			print ("You join the militia, get given an old rifle that often gets jam and only delivers "
			"once every three shots but nonetheless it's a gun and you get busy with learning how to "
			"shoot.")
			tavern_politics()
		elif decision == "3":
			print ("You fool! The Germans left quite soon after Rousseau's government abdiquated and "
			"paid a hefty fine, but the Parisians decided to become and independent and set-up la "
			"Commune, a bloody French revolution that would last 2 years, starve the capital. How long "
			"do you think you can carry on baking bread?")
			baking_bread()
		else:
			print "You're a creative kind, but in 1871 there were only 3 options:\n", options

	
# def exit_game():
# # do I want one?


def tavern_politics():
# sandboxed
# option1
	print ("After practicing on some targets set-up by the old square of blah blah, you go and refresh "
	"yourself in a bistro, find some hairy looking men who look like they've been fighting for "
	"a while and you decide to strike up a conversation with them to understand a bit more about "
	"the current situation.\n"
	"After a couple of drinks they ask you to share your thoughts about democracy:")
	
	confused = ("I have not idea what you're going on about but it doesn't really matter. Paris is about "
		"to be starved and burnt to the ground, and you probably won't make it past winter. But the "
		"hairy men seem to take an odd interest in you and ask you to be clarify your position.")
		
	while True:
		democracy = raw_input("> ")
	
		if "bourgeoisie" in democracy:
			print ("sounds like you're a Marxist. Man A takes you to an old tavern in "
			"an obscure part of Paris and you talk about blah blah till dawn.")
		elif "Anarchist" in democracy:
			print ("sounds like you're an Anarchist. Man B takes you to meet very "
			"famous Anarchist woman who carried on spreading anarchist and giving talks all over France "
			"until she was well in her 90s.")
		elif "Republican" in democracy:
			print ("sounds like you're a Republican. No one really likes you, and "
			"you undergo an identity crisis once the Germans have left.")
		elif "Feminist" in democracy:
			print ("sounds like you're a feminist. Feminism wasn't quite a thing yet, "
			"but lots of great things happened for the emancipation of women's rights, like blah and blah.")
		else:
			print confused
			print "-- you might want to use more ideology specific vocab --"


def baking_bread():
#sandboxed
	print ("The early days were not too bad, everything was like usual, you woke up early and baked "
	"bread sweating with all these hot ovens around you. It's true that whilst men still have "
	"bread, they will still carry on. All until one day you wake up and hear lots of chaos "
	"upstairs. The prussians have left, and the Commune is set-up. Your boss decides to flee "
	"Paris as otherwise he will persecuted and his property will be confiscated. He wasn't a "
	"very popular man in the revolutionary circles. However in an act of kindness, he offers "
	"you to go with him, to which you say Yes or No: ")
	
	escape = ("It was very close but you managed to escape the Prussians by leaving before the break "
	"of dawn, and once you passed Anvers you took a train to go South to some small village "
	"near Nice where you open a little café, go to the beach every morning, meet your significant "
	"other and make family with 5 children and to feed them all you work like a horse for the "
	"rest of your life.")
				
	while True:
		bakery_decision = raw_input("> ")
	
		if bakery_decision == "yes":
			print escape
			exit(0)
		elif bakery_decision == "no":
			opinion()
		else:
			print "There's only two options and time is ticking... decide now!"
		
def opinion():
#sandboxed
	print ("You stay and decide to run the bakery like a cooperative and support the poor and "
	"men at the front. However the wheat supplies and quickly running low and the council "
	"invites you to give your opinion about the future of bread in Paris. In an unexpected "
	"moment of eloquence, you tell them:\n"
	"- Ann Arendt quote on Bread and revolutions\n"
	"- quote 2 on bread and revolutions\n"
	"- quote 3 on revolutions and bread\n"
	"- quote 4 on both")

	Ann = "There's a lot of bread, but be careful"
	quote2 = "There are revolutions and there's bread"
	quote3 = "Sometimes there's bread an revolutions"
	quote4 = "sometimes there's both bread and revolutions"
	
	speech = raw_input("> ")

	if speech == "1":
		print Ann
	elif speech == "2":
		print quote2
	elif speech == "3":
		print quote3
	elif speech == "4":
		print quote4
	else:
		print "Too bad you can't type properly. They got you to read out some Ann Arendt\n", Ann

start()

# def ? I would like to link the outcome of function tavern_politics() to this function
# # needs to go through the sandbox
# # should I make this a function, or just a part of the script?
# # how can I attach the political identification/attribute to the outcome of this function
# # one option would be to make an object (the character) that has certain characteristics
# # attributes? that change over time -> that object should be able to traverse functions
# # another option could be to make mini-functions or methods that change according to the 
# # outcome of the previous function?

	# print "One night you get woken up in haste, your commander informs you that the French army is attacking simultaneously
	# "different areas of Paris and you need to go and take your positions to protect the city. You grab your old rifle,
	# "get given your ammunitions and run to your position. Once there you count how many bullets you have:

	# count_bullets = raw_input("Press enter to count how many bullets you have >")

	# if object == Marxist:
		# print "Bullets = 100\n"
		# print ("You're a Marxist and like the Anarchists, you were less well armed than the "
		# "Republicans who had more resources. You have 20 less bullets than them. After a 
		# "long night of fighting, you have only 8 bullets left. This is the show down and "
		# "you try to make every bullet count."
	# elif object == Anarchist:
		# print "Bullets = 100\n"
		# print "You're an Anarchist and like the Marxists, you were less well armed than the "
		# "Republicans who had more resources. You have 20 less bullets than them. After a "
		# "long night of fighting, you have only 8 bullets left. This is the show down and "
		# "you try to make every bullet count."
	# elif object == Republican:
		# print "Bullets = 100\n"
		# print "You're a Republican and you were better well armed than the Marxists and "
		# "Republicans. You have 20 bullets more than them. After a long night of fighting, "
		# "you have only 10 bullets left. This is the show down and you try to make every "
		# "bullet count."
	# else (do I need to put an elif for Femnisim or it will just treat any other outcome as such?):
		# print "Bullets = 100\n"
		# print "You're a Feminist and you were the least well armed. You have 40 less "
		# "bullets than the Republicans and 20 bullets less than the Marxists and Anarchists. "
		# "After a long night, you have only 6 bullets left. This is the show down and you "
		# "try to make every bullet count."


# def shoot_out():
	# # a list or some value that decrements i.e. -= 1 and a boolean if bullets == 0 then 
	# # execute.

# def shoot_out():
	# bullets = 10

	# shoot = raw_input("> ")
	
	# for i in bullets:
		# if bullets > 0:
			# bullets -= 1
		# else:
			# return bullets

	# # random generator
	# 1 - Well done! You shot a French bastard.
	# 2 - Damn it! Your rifle jammed and you had to duck real quick to not get shot.
	# 3 - Ouch! Your rifle jammed and you got shot in the:
	# # random generator
		# 3a - shoulder
		# 3b - arm
		# 3c - hand
		# 3d - leg
	# if bullets == 0
		# return """
		# You're out of bullets but don't worry, the French had a humiliating defeat and had to retreat. Everyone is 
		# celebrating and the injured are nursed. You're lucky or unlucky, you got shot in your ...
		# """
	
# def celebrate():	
# 	print """You decide to celebrate with your friends and go to the Oiseau Sauvage, your favorite tavern in Paris.
# 	On the menu:
# 	- rat saute
# 	- elephant
# 	- crocodile
# 
# 	What do you decide to eat?"""
# 	
# 	order = int(raw_input("> "))
# 
# 	elephant = 2
# 	crocodile = 2
# 	rat = 2
# 	
# 	if order == "elephant" or "crocodile":
# 		if money() >= 2:
# 			print "yum that was tasty!"
# 		else:
# 			print "sorry you can't afford it. You only have ", money, "francs."
# 
# 	elif order == "rat" "Ooh, that was a nice little variation to the usual daily stove grilled kind"
# 
# def count_money():
# 	print "That was tasty! Well at least better than usual. Are you still hungry?"
# 	
# 	still_hungry = raw_input("> ")
# 
# 	while True:
# 		if money > 0:
# 			if "Yes" and Marxist / Anarchist / Republican:
# 				print "You have", money, "left. What do you want?"
# 				order = raw_input("> ")
# 			elif "Yes" and Feminist:
# 				print "Sorry you can't afford anymore food. But hey! You contributed to builiding a school."
# 			elif "No":
# 			print "You're wise, you might need the money later."
# 		else:
# 			print "You fool! You have no money left! You will have to hunt and eat rat for the rest of the revolution."
# 
# def final_battle():
# 	print """
# 	News come that the French have reinforcements that came to surround Paris. They will surely attack by the
# 	break of dawn. This is the time to decide what you want to do:
# 	- Stay and fight
# 	- Flee Paris
# 	- Hide
# 	"""
# 	final_choice = raw_input("> ")
# 	
# 	if ("stay" and "fight") in final_choice:
# 		if money > 1:
# 			print "You were wise and you had enough bullets to fight and kill yourself before they got you"
# 		elif feminist:
# 			print """You're a feminist and you fought harder than anyone else, but yep, you die too. On the bright
# 		 side of things, the great French writer Victor Hugo wrote an ode to you. Well it wasn't really
# 		 Victor Hugo, just the writer of this game:""", Ode(name of player)
# 		else:
# 			print """You spent all your money on eating and celebrating so you can't afford enough ammunitions,
# 			you run out of bullet and you have an ultimate shoot out"""
# 	elif "flee" in final_choice:
# 		if money > 1:
# 			print """you were wise not to spend all your money on food. You were able to bribe out of Paris and went to the
# 	South of France.""" start.1
# 		else "you're too poor and couldn't afford the bribes. You got shot for deserting."
# 			exit(0)
# 	elif "Hide" in final_choice:
# 		print """Well done, you survived to tell the tale. However insignificant your part 
# 		was in it."""
# 		
# def ode(name, gender):
# 	import set_up
# 	"""Ode %r was the greatest fighter. %r was brave.""" % (name.set_up, gender.set_up)
# 	
start()