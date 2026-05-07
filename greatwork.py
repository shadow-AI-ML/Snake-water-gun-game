import random
"""
1 for snake
0 for water
-1 for gun
"""
computer=random.choice([1,0,-1])
youstr=int(input("Enter your choice:"))
youDict={"s":1,"w":0,"g":-1}
reverseDict={1:"snake",0:"water",-1:"gun"}

you=youstr

print(f"you chose {reverseDict[you]}/ncomputer chose {reverseDict[computer]}")

if (computer==you):
	print("Draw!")
else:
  if (computer==-1 and you==1):
  	print("You Win!")
	
  elif (computer==-1 and you==0):
	  print("You Lose!")
	
  elif (computer==1 and you==-1):
	  print("You Lose!")
	
  elif (computer==1 and you==0):
	  print("You Win!")
	
  elif (computer==0 and you==-1):
	  print("You Win!")
	
  elif (computer==0 and you==1):
	  print("You Lose!")
	
  else:
      print("something went wrong")	