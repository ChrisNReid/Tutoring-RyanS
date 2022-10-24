#Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.
# vowels: a e i o u 
def vowelcounter():
  userinp = input ("Please enter a sentence or whatever you want \n")
  vowels = ['a', 'e', 'i', 'o', 'u'] 
  counter = 0
  vowelcount = [0]*5
  
  sum = 0
  
  for i in range(0,len(userinp)):
    for j in range (0,len(vowelcount)):
      if userinp[i] == vowels[j]:
        vowelcount[j] += 1
        sum = sum+1
  print (vowelcount)
  print(sum)

#adding elemenst in a list to get a sum
#overall = 0

#for i in range (0,len(vowelcount)):
 # overall = vowelcount[i] + overall

#print (overall)

vowelcounter()