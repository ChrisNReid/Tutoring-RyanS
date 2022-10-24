import csv

airportdeets = []
with open("airport.txt", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        airportdeets.append(row)

print(airportdeets)
#if you cannot understand this code then what are you doing marking it
def airportdetails():
  choice2 = input('Please enter Uk airport code\n')
  if choice2 == 'LPL' or choice2 == 'BOH':
    start = choice2
 
  else:
    print('invalid entry')
    airportdetails()
  
  choice3 = input("Please enter the overseas airport thingy\n")
  found = False
  for row in airportdeets:
    for element in row:
        if element == choice3:
            found = True
            break
    if found:
        break
  if found:
    print("Found")
  else:
    print("Not found")






choice1 = input ("Which option do you want?\nEnter airport details (1)\nEnter flight details (2)\nEnter price plan and calculate profit (3)\nClear data (4)\nQuit (5)\n")

if choice1 == '1':
  airportdetails()
if choice1 == '2':
  print ("work in progress")
if choice1 == '3':
  print ("work in progress")
if choice1 == '4':
  print ("work in progress")
if choice1 == '5':
  print ("Gooodbye")
  quit()
else:
  print ('idiot')

