import random
import time

array = [
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g",
    "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4",
    "5", "6", "7", "8", "9", "0", "!", "£", "$", "%", "^", "&", "*", "(", ")",
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G",
    "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"
]
feedback = []
count = 0
for j in range(1,51):
  print("\n--------------")
  print("Round: ", j)
  print("-------------")
  select = random.randint(0, len(array)+1)
  print("Enter character: ", array[select])

  start = time.time()
 
  userinp = input()
  current = time.time()
 
  if (current - start) < 2:
    if userinp == array[select]:
        print("correct")
        count +=1   
    else:
        print("wrong")
        feedback.append(j)
        feedback.append(array[select])
  else:
      print("times up")
      feedback.append(j)
      feedback.append(array[select])
        
print("Your score was", count)

if count < 40:
    print("You are horrendous at this game, do better")
elif count < 49:
      print("Meh, do better")
else:
  print ("Good, do better")

print("Feedback")
# while k< len(feedback)):
#   print("Round ",feedback[k], " : ", feedback[k+1])
#   k = k +2
print (feedback)
