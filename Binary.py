# A program that takes a  8 bit binary input and converts it to Hexidecimal

# take 8 bit binary input
# convert decimal/normal
# convert normal to hex

def binarycalculator():
  limit = input("Enter how many bits you want:")
  
  num1 = input("Enter an 8 bit number\n")

  
  bin = []*limit
  dec = limit
  for i in range (0, limit):
    temp = 2**dec
    bin.append[temp]
    temp = 0
    dec = dec -1
  
  print(bin)
  
        # 1  1  0  0  0 1 0 1
  
  # for loop that looks at each elemenet in num1
  # check if the element in num1  is 1 or 0
  
  count = 0
  
  for nope in range (8):
    if num1[nope] == '1':
      count = count + bin[nope]
  
  print (count)
binarycalculator()
