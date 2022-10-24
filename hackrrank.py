phrase = str(input("Enter a phrase\n"))
vowelcount = 0

counter = 0
while counter < len(phrase):
  if (phrase[counter] == "a") or (phrase[counter] == "e") or (phrase[counter] == "i") or (phrase[counter] == "o") or (phrase[counter] == "u") or (phrase[counter] == "A") or (phrase[counter] == "E") or (phrase[counter] == "I") or (phrase[counter] == "O") or (phrase[counter] == "U"):    
    counter +=1
    vowelcount +=1
  else:
    counter +=1

print("There are",vowelcount,"vowels in", phrase)


  # 