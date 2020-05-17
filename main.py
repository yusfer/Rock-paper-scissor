

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

def compare_value(p1,p2):

	print("%s :::: %s" %(p1.player_name,p1.chose))
	print("%s :::: %s" %(p2.player_name,p2.chose))

	val1 = p1.chose
	val2 = p2.chose

	if val1 == val2:
		print ("EMPATE")
	elif (val1=="Rock" and val2=="Scissor") or (val1=="Paper" and val2=="Rock") or(val1=="Scissor" and val2=="Paper"):
		print ("WIN FOR %s " %p1.player_name)
	else:
		print ("WIN FOR %s " %p2.player_name)

class player:
	player_name=""
	chose = ""
	def __init__(self,player_name,chose):
		self.player_name= player_name
		self.chose=chose


###  MAIN ###


# Take player name
print("Please, enter your name:")
player1 = player(input(),"")

# Take the election from player usin command line
# if value is not right, repeat and repeat

#this infinite loop is for repeat the game forever and ever
while True:
	execute = True
	while execute:
		print (" Rock, Paper or Scissor?")
		#player_chosen = input().capitalize()
		player1.chose = input().capitalize()
		execute=is_right(player1.chose)

	# election for CPU
	cpu = player("CPU", randomvalue())
	#cpu_chosen = randomvalue()

	#print ("Your selection is %s" %player1.chose)
	#print ("CPU selection is %s" %cpu.chose)


	# comparation of values
	compare_value(player1,cpu)

