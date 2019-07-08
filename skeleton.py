class Set_Up(object):

	def __init__(self):
		print 'name'
		print 'gender'
		print 'ammunitions'
		print 'money'
		pass

class Scene(Set_Up):
	
	def enter(self):
		pass
	
class Intro(Scene): # 1871 (map?)

	print 'flee'
	print 'fight'
	print 'bake'
	
	def ideology(self):
		print 'idelogy' # does it belong here, or further down in each scene?
		pass
		
class Southern_France(Scene):
	
	def enter(self):
		pass

class Tavern_Politics(Scene):

# 	self.idelogy(Scene) = idelogy
 	print 'ideology'
	
# 			*marxist
# 			*anarchist
# 			*republican
# 			*feminist

class Bakery_Politics(Scene):

	print 'stay'
	print 'flee'
	print 'keep_baking'
	
class Speech(Scene):

	print 'ideology'
	

#			func political_speech (could this be under 'ideology' function
# 			func ideology
# 				*marxist
# 				*anarchist
# 				*republican
# 				*feminist

class Shoot_Out(Scene): #(checking ammunitions)

	print 'counting_ammunitions' # (could I combine simplify it under just count?)
	print 'shooting'

class Celebration(Scene):

	print 'choosing food'
	print 'option to eat more?"
	print 'counting_money'

class Last_Battle(Scene):
	print 'hide'
	print 'fight'
	print 'counting_ammunitions'
	print 'flee'
	print 'counting_money'
	print 'bribing'
	print 'executed'
	
class Death(Scene):

	def enter(self):
		pass
		
jivana.Set_Up(object) = jivana # not sure about this and what it does