
import time
import random
import turtle
import math

def processing():
    print('   . .             . .' )
    print('   /|\            ¬/|\
  ')
    print('    /\              /\  ')
    print('\n')
    time.sleep(1)
    print('   . .             . .' )
    print('   /|\          - ¬/|\
  ')
    print('    /\              /\  ')
    print('\n')
    time.sleep(1)
    print('   . .             . .' )
    print('   /|\        -   ¬/|\
  ')
    print('    /\              /\  ')
    print('\n')
    time.sleep(1)
    print('   . .             . .' )
    print('   /|\       -    ¬/|\
  ')
    print('    /\              /\  ')
    print('\n')
    time.sleep(1)
    print('   . .             . .' )
    print('   /|\    -       ¬/|\
  ')
    print('    /\              /\  ')
    print('\n')
    time.sleep(1)
    print('   . .             . .' )
    print('   /|\ -          ¬/|\
  ')
    print('    /\              /\  ')
    print('\n')
    time.sleep(1)
    print('   . .             . .' )
    print('   /|\-           ¬/|\
  ')
    print('    /\              /\  ')
    print('\n')
    time.sleep(1)
    print('    x x             . .' )
    print('-   /|\            ¬/|\
  ')
    print('     /\              /\  ')
    print('\n')
    time.sleep(1)
    print('The end.')

def choice():
    firstchoice = input('Do you want to play a game (1) or be boring (2)?\n')
    if firstchoice == '1':
        print('Game options: \n (1)Higher or lower \n (2)Luck \n (3)Letter List\n (4)No\n')
        gamechoice = int(input('Enter game name \n'))
        if gamechoice == 1:
            higherorlower()
        elif gamechoice == 2:
            luckchoice = int(input('Do you want \nLazyman verion (1) \nEffort version(2)\n'))
            if luckchoice == 1:
                lazymanluck()
            else:
                luck()
        elif gamechoice == 3:
            letterlist()
        elif gamechoice == 4:
            no()
    elif firstchoice == '2':
        print('Game options: \nCalculator (1)\nCurrency Converter (2)\nTime Converter (3)\n')
        boringchoice = int(input('Enter boring name \n'))
        if boringchoice ==1:
            calculator()
        elif boringchoice == 2:
            converter()
        elif boringchoice == 3:
            timeconverter()
            
def letterlist():
        
    #Letter List
    #user enters a letter, outputs all words with that letter from list
    #output how any words

    array = ['animal', 'hello', 'bye' 'letter', 'shoe', 'rock','shalom']
    letter = input('Enter a letter\n')

    i=0
    temp = ''
    counter = 0

    while i < len(array):
        temp = array[i]
        if  temp[0] == letter:
            print(array[i])
            counter +=1
       
        i=i+1
    print(counter, 'Matches found')
    if counter == 0:
        print('Do another letter')
    choice()
        
def luck():
    print('Guess the randomly generated number correct 10 times to leave')
    correct = 0
    while correct <= 10:
        compnum = random.randint(1,10)
        num = int(input('Enter a number between 1-10\n'))

        if num == compnum:
            print('Correct')
            correct +=1
        else:
            print('Unlucky...incorrect it was ', compnum)
    choice()

def lazymanluck():
    print('Guess the randomly generated number')
    limattempts = int(input('How many attempts do you want the computer to have?\n'))
    limcorrect = int(input('How many should the computer get correct?\n'))
    limrange = int(input('Max range of numbers?\n'))
    correct = 0
    attempts = 0
    while correct <= limcorrect and attempts < limattempts:
        compnum = random.randint(1,limrange)
        num = random.randint(1,100)
    
        if num == compnum:
            print('You guessed ', num, 'which was correct!')
            correct +=1
        else:
            
            print('Unlucky... you guessed ', num, '\nIncorrect it was ', compnum)
        attempts = attempts+1
    if correct == limcorrect and attempts<= limatempts:
        print(' \nYou Passed, it took ' , attempts, 'attempts')
    else:
        print('\nYou Failed')
    
    choice()
        
def quadraticstuff():
  #1|square b
  #2|4 x a x c
  #3|(1) - (2)
  #4|square root (3)
  #5| -b + (4)
  #6|2 x a
  #7|(5)/(6)
  #8|-b - (4)
  #9| (8) -(6)
  #10| x = (7)
  #11| x (+-) (7) = 0
  
  #import math
  #import time
  
  def quadraticformula():
      ainp = float(input("Please enter a\n"))
      binp = float(input("Please enter b\n"))
      cinp = float(input("Please enter c\n"))
      step1 = (binp)*(binp)
      step2 = 4 * ainp * cinp
      step3 = step1 - step2
      step4 = math.sqrt(step3)
      step5 = -(binp)+ step4
      step6 = 2 * ainp
      step7 = step5/step6
      step8 = -(binp) - step4
      step9 = step8/step6
      step10 = step7-step7-step7
      step11 = step9-step9-step9
      if step10 < 0 and step11 < 0:
          print ("(x",step10,")(x",step11,")")
          print (step7,"OR",step9)
          step12 = input("Would you like to round your answer?\nYes (1)\nNo (2)\n")
          if step12 == '1':
              step13 = int(input("How many significant figures would you like to round to?\n"))
              step14 = round(step10, step13 - int(math. floor(math. log10(abs(step10)))) - 1)
              step15 = round(step11, step13 - int(math. floor(math. log10(abs(step11)))) - 1)
              step16 = round(step9, step13 - int(math. floor(math. log10(abs(step9)))) - 1)
              step17 = round(step7, step13 - int(math. floor(math. log10(abs(step7)))) - 1)
              if step14 < 0 and step15< 0:
                  print ("(x",step14,")(x",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              elif step14 > 0 and step15 < 0:
                  print ("(x +",step14,")(x",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              elif step14 < 0 and step15 > 0:
                  print ("(x",step14,")(x +",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              else:
                  print ("(x +",step14,")(x +",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
          else:
              print ("(x",step10,")(x",step11,")")
              print (step7,"OR",step9)
              quadraticdelay()
      elif step10 > 0 and step11 < 0:
          print ("(x +",step10,")(x",step11,")")
          print (step7,"OR",step9)
          step12 = input("Would you like to round your answer?\nYes (1)\nNo (2)\n")
          if step12 == '1':
              step13 = int(input("How many significant figures would you like to round to?\n"))
              step14 = round(step10, step13 - int(math. floor(math. log10(abs(step10)))) - 1)
              step15 = round(step11, step13 - int(math. floor(math. log10(abs(step11)))) - 1)
              step16 = round(step9, step13 - int(math. floor(math. log10(abs(step9)))) - 1)
              step17 = round(step7, step13 - int(math. floor(math. log10(abs(step7)))) - 1)
              if step14 < 0 and step15< 0:
                  print ("(x",step14,")(x",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              elif step14 > 0 and step15 < 0:
                  print ("(x +",step14,")(x",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              elif step14 < 0 and step15 > 0:
                  print ("(x",step14,")(x +",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              else:
                  print ("(x +",step14,")(x +",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
          else:
              print ("(x +",step10,")(x",step11,")")
              print (step7,"OR",step9)
              quadraticdelay()
      elif step10 < 0 and step11 > 0:
          print ("(x",step10,")(x +",step11,")")
          print (step7,"OR",step9)
          step12 = input("Would you like to round your answer?\nYes (1)\nNo (2)\n")
          if step12 == '1':
              step13 = int(input("How many significant figures would you like to round to?\n"))
              step14 = round(step10, step13 - int(math. floor(math. log10(abs(step10)))) - 1)
              step15 = round(step11, step13 - int(math. floor(math. log10(abs(step11)))) - 1)
              step16 = round(step9, step13 - int(math. floor(math. log10(abs(step9)))) - 1)
              step17 = round(step7, step13 - int(math. floor(math. log10(abs(step7)))) - 1)
              if step14 < 0 and step15< 0:
                  print ("(x",step14,")(x",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              elif step14 > 0 and step15 < 0:
                  print ("(x +",step14,")(x",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              elif step14 < 0 and step15 > 0:
                  print ("(x",step14,")(x +",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              else:
                  print ("(x +",step14,")(x +",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
          else:
              print ("(x",step10,")(x +",step11,")")
              print (step7,"OR",step9)
              quadraticdelay()
      else:
          print ("(x +",step10,")(x +",step11,")")
          print (step7,"OR",step9)
          step12 = input("Would you like to round your answer?\nYes (1)\nNo (2)\n")
          if step12 == '1':
              step13 = int(input("How many significant figures would you like to round to?\n"))
              step14 = round(step10, step13 - int(math. floor(math. log10(abs(step10)))) - 1)
              step15 = round(step11, step13 - int(math. floor(math. log10(abs(step11)))) - 1)
              step16 = round(step9, step13 - int(math. floor(math. log10(abs(step9)))) - 1)
              step17 = round(step7, step13 - int(math. floor(math. log10(abs(step7)))) - 1)
              if step14 < 0 and step15< 0:
                  print ("(x",step14,")(x",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              elif step14 > 0 and step15 < 0:
                  print ("(x +",step14,")(x",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              elif step14 < 0 and step15 > 0:
                  print ("(x",step14,")(x +",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
              else:
                  print ("(x +",step14,")(x +",step15,")")
                  print (step16,"OR",step17)
                  quadraticdelay()
          else:
              print ("(x +",step10,")(x +",step11,")")
              print (step9,"OR",step7)
              quadraticdelay()
  
  
  #1|square b
  #2|4 x a x c
  #3|(1) - (2)
  #4|square root (3)
  #5| -b + (4)
  #6|2 x a
  #7|(5)/(6)
  #8|-b - (4)
  #9| (8) -(6)
  #10| x = (7)
  #11| x (+-) (7) = 0
  
  #1|bracket 1 x
  #2|bracket 1
  #3|bracket 2 x
  #3|bracket 2
  #((1x) +/- (1))((2x) +/- (2))
  #4|(1x) x (2x)
  #5|(1x) x (2)
  #6|(2x) x (1)
  #7|(#5) + (#6)
  #8|(1) x (2)
  #9|(#4) (#7) (#8)
  
  def quadraticformulaback():
      br1x = int(input("Input Bracket 1 x\n"))
      br1 = int(input("Input Bracket 1 number\n"))
      br2x = int(input("Input Bracket 2 x\n"))
      br2 = int(input("Input Bracket 2 number\n"))
      bstep4 = br1x * br2x
      bstep5 = br1x * br2
      bstep6 = br2x * br1
      bstep7 = bstep5+bstep6
      bstep8 = br1 * br2
      if bstep7 > 0:
          print (bstep4 ,"x^2 +", bstep7,"x", bstep8)
          quadraticdelay()
      else:
          print (bstep4 ,"x^2", bstep7,"x", bstep8)
          quadraticdelay()
  
  
  
  def quadraticmenu():
      inp = input("Quadratic formula (1)\nExpanding Brackets (2)\n")
      if inp == '1':
          quadraticformula()
      elif inp == '2':
          quadraticformulaback()
      else:
          quadraticmenu
  
  def quadraticdelay():
      time.sleep(10)
      quadraticmenu()
  
  quadraticmenu()
        

    
def converter():
    pounds = float(input('Please enter the amount in Pounds\n'))
    currency = ''
    while currency != '1' or currency != '2':
        currency = input('enter final currency (Euro (1)/Dollar (2))\n')
        if currency == '1':
            result = pounds*1.17
            print(result)
            choice()
        elif currency == '2':
            result = pounds*1.38
            print(result)
            choice()
        else:
            print('Invalid...enter correct currency')
    

def add(num1, num2):
    print(num1 + num2)
def multiply(num1, num2):
    print(num1 * num2)
def divide(num1, num2):
    print( num1 / num2)
def subtract(num1, num2):
    print(num1 - num2)

def calculator():
    num1 = float(input('Enter a number \n'))
    num2 = float(input('enter a number \n'))
    sign  = input('enter sign \n')
    if sign == 'add' or sign == '+':
        add(num1,num2)
        
    elif sign == 'subtract' or sign == '-':
        subtract(num1,num2)
    elif sign == 'multiply' or sign == '*':
        multiply(num1,num2)
    elif sign == 'divide' or sign == '/':
        divide(num1,num2)
    else:
        print('Invalid entry')
    time.sleep(5)
    choice()

def sec(value):
    import time
    ty_res = time.gmtime(value)
    res = time.strftime("%H:%M:%S",ty_res)
    print(res)
    
def timeconverter():
    first = input('What unit is your first entry?\n')
    value = int(input('what value is your first entry?\n'))
    second = input('what unit is your second entry?\n') 
    if first == 'seconds':
        sec(value)
    elif first == 'minutes' and second == 'seconds':
        print(first*60)
    elif first == 'minutes' and second == 'hours':
        print(first/60)
    elif first == 'hours' and second == 'seconds':
        print(first*60*60)
    elif first == 'hours' and second == 'minutes':
        print(first*60)
        
    time.sleep(5)
    choice()

def binarycalculator():
  limit = int(input("Enter how many bits you want: "))
  
  num1 = input("Enter an 8 bit number\n")

  
  bin = []*limit
  dec = limit-1
  for i in range (0, limit):
    temp = 2**dec
    bin.append(temp)
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

def higherorlower():
    choice = int(input('Welcome to the Higher or Lower Game\nWhat range would you like; 1-10 (10), 1-100 (100), 1-1000(1000)? \n'))
    
    import random
    answer = random.randint(1,choice)
    guess = 0
    counter = 0

    print('      Welcome to higher or Lower with range ', choice)
    while guess != answer:
        guess = int(input('Enter number\n'))
        counter = counter + 1

        if guess>answer:
            print('Too high')
        elif guess<answer:
            print('Too low')

    print('correct answer in', counter, 'trys')
    time.sleep(5)
    choice()

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

def no():
    no = random.randint(1,10000)
    guess = int(input("Guess how many no's\n"))
    score = no-guess
    if score < 0:
        score = score - (score*2)

    score = 10000-score
    for i in range(no):
        print('No')
    print("That was ", no, "no's")
    print('Score is ', score)
    time.sleep(5)
    choice()


def deadlylogin(array):
    print('Unlucky, you have to confirm your details! ')
    secusername = input('Enter username\n')
    secpassword = input('Enter password\n')

    if (secusername == array[0]) and (secpassword == array[1]):
        print('Access granted')
    else:
        print('Press alt F4')

        for i in range(1,11):
            print(i)
            time.sleep(1)
            
        quit()
        

    
def stupid():
    for i in range(100):
        print('\n')
def signup():
    array=[]
    print('Sign Up')
    username = input('Enter a username \n')
    password = ''

    while len(password) < 6:
        password = input('Enter a password \n')

        if len(password) < 6:
            print('Password too short\n')
        else:
            print('processing...')
            processing()
            time.sleep(5)
            stupid()
            
    attempts = 0
    confpassword =''
    while confpassword != password:
        if attempts <5:
            print('Confirm your password\n')
            confpassword = input('enter password\n')
            
            if confpassword == password:
                print('Correct')
                array.append(username)
                array.append(password)
                
            else:
                print('Access denied')

            attempts=attempts+1

    
    num = random.randint(1,100)
    if num <= 25:
        stupid()
        deadlylogin(array)
        choice()
        

    else:
        print('Absolute nothing happening here...')
        choice()

def main():
  print ("*******************************************")
  print("WELCOME TO THE Project")
  print("*******************************************")


  print ("Please select an option")
  mainselect = input("(1) School\n(2) Definetly School\n")
  if mainselect == '1':
    school()
  else:
    print ("Please select a valid option")
    main()
  
  
def school():
  print("Choose a subject:")
  print("(1) - Maths")
  print ("(2) - Physics")
  print ("(3) - Computer Science")
  schoolselect = input ("")
  if schoolselect == '1':
    maths()
  elif schoolselect == '2':
    physics()
  elif schoolselect == '3':
    computerscience()
  else:
    print ("Please select a valid option")
    school()

def maths():
  mathchoice = input("Please select an option\n(1) Quadratic stuff")
  if mathchoice == '1':
    quadraticstuff()
  if mathchoice == '2':
    
  
  else:
    print ("Please select a valid option")
    maths()

def physics():
  #bunch of formulas
  x = 1

def computerscience():
  print ("Choose an option")
  compscchoice = input("(1) Binary Calculator\n(2) Hexadecimal Calculator\n")
  if compscchoice == '1':
    binarycalculator()
  elif compscchoice == '2':
    hmmmmmmmmmmm()
  else:
    print ("Please input a valid input")
    computerscience ()

def games():
  print ("Select which game you want to play:\n(1) Processing\n(2) Luck\n(3) Lazyman Luck\n(4) Letterlist\n(5) Higher or Lower\n(6) Budget Wordle\n(7) No\n(8)Codebreaker\n(9) Menu")
  gamemenu = []
main()