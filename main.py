

# I will going to create a quick Rock, Paper and Scissor game
# using PYTHON. Idea is start with easy functionalities for 
# add some more after the game creation

import random

# switcher function to translate number-to-value
def switch_values(num):
	switcher = {
		1:"Rock",
		2:"Paper",
		3:"Scissor",
	}

	return switcher.get(num,"Invalid number")

#retun a random value from Rock, Paper and Scissor
def randomvalue():	
	
	number = random.randint(1,3)
	return switch_values(number)

# compare if value is a right option for the game
# modify "cont" boolean for finish the loop
def is_right(val):
	if val=="Rock" or val=="Paper" or val=="Scissor":
		return False
	else:
		print ("Please, insert a right option for the game")
		return True



###  MAIN ###

# Get the election from player usin command line
# if value is not right, repeat and repeat
execute = True
while execute:
	print (" Rock, Paper or Scissor?")
	player_chosen = input().capitalize()
	execute=is_right(player_chosen)


cpu_chosen = randomvalue()

print ("Your selection is %s" %player_chosen)
print ("CPU selection is %s" %cpu_chosen)