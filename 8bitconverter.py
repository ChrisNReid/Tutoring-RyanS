def bintohex():
  loop = int(input("How many times do you want to loop the code?\n"))
  for definetlynot in range (loop):  
    # A program that takes a  8 bit binary input and converts it to Hexidecimal

    # take 8 bit binary input
    # convert decimal/normal
    # convert normal to hex


    num1 = input("Enter an 8 bit binary number\n")



    bin = [128,64,32,16,8,4,2,1]

          # 1  1  0  0  0 1 0 1

    # for loop that looks at each elemenet in num1
    # check if the element in num1  is 1 or 0

    count = 0

    for nope in range (8):
      if num1[nope] == '1':
        count = count + bin[nope]

    print ("Decimal number: \n",count)

    #  how do we convert decimal to hex
    # divide by 16 and have a remainder

    # divide by 16 is first hex number, remainder is the second hex number

    # 7/2 = 3.5

    # div //
    # returns a division without a remainer 
    # e.g 7 DIV 2 = 3

    # MOD %
    # only returns remainder 
    # e.g. 7 mod 2 = 1
    num2 = count//16
    num3 = num2%16


    table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C','D','E', 'F']

    # getting the data for the given location
    pos1 = table[num2]
    pos2 = table[num3]
    print ("Hex number:\n#",pos1,pos2)
    print ("Binary number", num1)

bintohex()