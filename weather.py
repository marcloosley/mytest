import math
import weather

def weatherMessage(temp, low, med):
	temp = 40 * math.sin(2.5)
	if temp < 3:
		print ("wear wool trousers")
	elif temp < 10:
		print ("wear trousers")
	else:
		print ("wear shorts")
		
#weatherMessage(15, 5, 20)

#for i in range(0,100):
	#print weatherMessage(i, 7, 15)
	

import random
"""
def predictTomorrowsTemp():
	return random.choice(range(-3,25))
"""	
def predictTomorrowsTemp(todaysTemp):
	change = random.choice(range(-1,2))
	newTemp = todaysTemp + change
	return newTemp

"""	
today = 10
tomorrow = predictTomorrowsTemp(today)
nextday = predictTomorrowsTemp(tomorrow)
print today
print nextday
"""



