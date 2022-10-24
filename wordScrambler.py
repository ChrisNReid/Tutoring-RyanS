import random
#ask user for input
#keep the 1st and last
#rearrange everything in between by randomly assigning

#input

#check if 3 letters+

#rearrange everything in between by randomly assigning

#output final word/ sentence

userinp = input("Enter a word or phrase\n")
word = []
newphrase = []
if len(userinp) > 3:
  phrasearr = userinp.split()
  #print(phrasearr)
  for i in range(0,len(phrasearr)):
    word = list(phrasearr[i])
    #print("word: ", word)
    if len(word) > 3:
      
      startend = []
      startend.append(word[0])
      startend.append(word[len(word)-1])
      #print (startend)
      word.remove(word[0])
      word.remove(word[len(word)-1])
      newword = ""
      count = 0
      x = True
      while (x == True) and (count != 50):
        #print (phrasearr[i])
        j = 0
        for j in range (0,50):
          count += 1
          shuffled = list(word)
          random.shuffle(shuffled)
          shuffledmiddle = ''.join(shuffled)
          #print(shuffledmiddle)
          newword = startend[0] + shuffledmiddle + startend[1]
          #print(newword)
          if newword != phrasearr[i]:
            x = False
        newphrase.append(newword)
      
    else:
      newphrase.append(phrasearr[i])
    #print (newphrase)
    
newerphrase = ""
for k in range (0, len(newphrase)):
  newerphrase = newerphrase + newphrase[k] + " "
  #print (newerphrase)
print("\n --------------The Answer------------- \n")
print (newerphrase)
  # print (newphrase)
  # newphrase.append(small)
  # print (newphrase)
      

      
      
    