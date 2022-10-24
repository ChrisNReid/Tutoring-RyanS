import random
def computerguess ():
  print ("X = Not a colour\n_ = Correct colour, wrong location\nLetter means correct location, correct colour")
  colours = ["B","G","Y","R","W","P","O"]
  answer = []
  counter = 0
  while counter <= 6:
    answer.append(colours[random.randint(0,6)])
    counter += 1
  print ("The colours are")  
  print(colours)
  feedback = []
  i = 0
  guess = ''
  attempts = 0
  while feedback != answer:
    feedback = []
    i = 0
    guess = input("Enter a colour guess combination\n")
    print (list(guess))
    while i <=6:
      
      if guess[i] == answer[i]:
          #correct
        feedback.append(guess[i])
          
      elif guess[i] in answer:
          #correct but wrong place  
        feedback.append("_")
          
      else:
        feedback.append("X")
          #incorrect
      i += 1
    attempts +=1
    print(feedback)
    
      #_
  # WGGGGGGG
  # JSBWNJJN
  print ("Congratulations, the colours were",answer,"and it took you",attempts,"attempts")
  global globalusrattempts
  globalusrattempts = attempts
  
  #40min left
  
  
  
  #You need to be able to use selection, iteration and string manipulation for this   project.


#computerguess ()

  
#ask user to input
#add input to array
#have computer guess
#compare feedback to guess
#only change ones that are different
#when its wrong, try same letter



def notcomputerguess():
  userinp = input("Enter and your answer for opponent \n")
  userinparray = list(userinp)
  print(userinparray)
  
  colours = ["B","G","Y","R","W","P","O"]
  feedback = []
  i = 0
  compguess = ['B', 'B', 'B','B','B','B','B']
  #print(compguess)
  attempts = 0
  counter = 0
  while compguess != userinparray:
    i = 0
    while i <=6:
      if compguess[i] == userinparray[i]:
           #correct
        compguess[i] = (compguess[i])
            
      else:
        compguess[i] = (colours[counter])
      i+=1
    counter += 1
    attempts +=1
    #print(compguess)
    
      #_
  # WGGGGGGG
  # JSBWNJJN
  global globalcompattempts
  globalcompattempts = attempts
  
print("Main Menu")
print("-------------------")

notcomputerguess()
computerguess()
print("Computer guessed in ", globalcompattempts)

if globalusrattempts < globalcompattempts:
  print("Congrats, you beat the computer")
elif globalusrattempts > globalcompattempts:
  print("You are terrible at this game, a computer beat you")
else:
  print("You drew with computer")
  