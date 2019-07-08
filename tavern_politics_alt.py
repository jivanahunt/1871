#!/usr/local/bin/python
# coding: latin-1

def tavern_politics():
# option2
# sandboxed
	def ideology():
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
			print ("I have not idea what you're going on about but it doesn't really matter. Paris is about "
			"to be starved and burnt to the ground, and you probably won't make it past winter. But the "
			"hairy men seem to take an odd interest in you and ask you to be clarify your position.")
			print "-- you might want to use more ideology specific vocab --"
			ideology()

	print ("After practicing on some targets set-up by the old square of blah blah, you go and refresh "
		"yourself in a bistro, find some hairy looking men who look like they've been fighting for "
		"a while and you decide to strike up a conversation with them to understand a bit more about "
		"the current situation.\n"
		"After a couple of drinks they ask you to share your thoughts about democracy:")
		
	ideology()
					
tavern_politics()