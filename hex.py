# takes a hex input and converts to denary
def hmmmmmmmmmmm():
  hex1 = input("Please enter hexadecimal number\n")
  # d3
  # d x 16 + 3

  table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C','D','E', 'F']


  # multiply the first number by 16
  # print(table.index("f")) = 15

  # get 1st and 2nd letter
  letter1 = hex1[0]
  letter2 = hex1[1]

  # getting location of the individual inputs
  pos1 = table.index(letter1)
  pos2 = table.index(letter2)

  # now we have what the user input means aka D now equals 13 (pos1) 

  # multiply 1st input by 16
  hexletter1 = pos1*16

  finalhex = hexletter1 + pos2

  print(finalhex)


# add 2nd number 
hmmmmmmmmmmm()