

# I will going to create a quick Rock, Paper and Scissor game
# using PYTHON. Idea is start with easy functionalities for 
# add some more after the game creation

import random
import pandas as pd

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
def is_right(val,):
	if val=="Rock" or val=="Paper" or val=="Scissor":
		return False
	elif val == "exit":
		return False
	else:
		print ("Please, insert a right option for the game")
		
		return True

def compare_value(p1,p2,punt):

	print("%s :::: %s" %(p1.player_name,p1.chose))
	print("%s :::: %s" %(p2.player_name,p2.chose))

	val1 = p1.chose
	val2 = p2.chose

	if val1 == val2:
		print ("EMPATE")
		punt["P1"].append("-")
		punt["CPU"].append("-")
	elif (val1=="Rock" and val2=="Scissor") or (val1=="Paper" and val2=="Rock") or(val1=="Scissor" and val2=="Paper"):
		print ("WIN FOR %s " %p1.player_name)
		punt["P1"].append("X")
		punt["CPU"].append("-")
	else:
		print ("WIN FOR %s " %p2.player_name)
		punt["P1"].append("-")
		punt["CPU"].append("X")

def sum_punt(table):
	punt1 = 0
	punt2 = 0

	for num in table["P1"]:
		print(num)
		if num == "X":
			punt1 += 1

	for num2 in table["CPU"]:
		print(num2)
		if num2 == "X":
			punt2 += 1

	table["P1"].append(punt1)
	table["CPU"].append(punt2)


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

punctuation = {
	"P1":[],
	"CPU":[]
}
# Take the election from player usin command line
# if value is not right, repeat and repeat

#this infinite loop is for repeat the game forever and ever until player write "exit"
exit = False
while not exit:
	execute = True
	#that loop is executing until value is right
	while execute:
		print (" ---Rock, Paper or Scissor? (exit for leave)")
		#player_chosen = input().capitalize()
		player1.chose = input().capitalize()

		#if player want to leave, break execution loop
		if player1.chose == "Exit":
			exit = True
			break

		execute=is_right(player1.chose)

	#if player want to leave, dont generate value for CPU

	if not exit:
			# election for CPU and comparation
		cpu = player("CPU", randomvalue())
		compare_value(player1,cpu,punctuation)
	else:

		#EXIT PROCEDURE, SHOW PUNTUATION AND FARAWELL
		print(punctuation)
		#sum of every puntuation and add to dictionary of punt
		sum_punt(punctuation)

		#adjustmen of name in puntuation table
		#punctuation[player1.player_name]=punctuation["P1"]
		#del punctuation["P1"]

		# change dict to dataframe to show it
		punt_table = pd.DataFrame(punctuation)
		maxim=punt_table.index.max()
		punt_table.rename(columns={"P1":player1.player_name}, index={maxim:"TOTAL"},inplace=True)
		print(punt_table)


		print("See you soon!")

