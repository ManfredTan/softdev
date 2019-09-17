#ROUGH DRAFT

import random

occupationsDict = {}

def makeDict( filename):
  data = open( filename, "r")
  for line in data:
    occupationDict.update({ line[0] : line[1] })
    print(line[0] + "," + line[1])
  
  
def randomOccupation(filename):
  percent = random.randint(0,101)
  data = open( filename, "r")
  place = 0
  for line in data:
    place = place + line[1]
    if place > percent:
      return line[0]
  
  
 
 
 
 dictOccupation( "occupations.csv")
 randomOccupation( "occupations.csv")
