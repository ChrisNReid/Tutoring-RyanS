
counter = 0
array = []
#input option speed?
enter = 'yes'
while enter == 'Yes' or enter =='yes':
  
  spd1 = float(input("Please enter the speed of the car on the 1st camera\n"))
  spd2 = float(input("please enter the speed of the car on the 2nd camera\n"))
  spd3 = ((spd1+spd2)/2)
  rspd3 = round(spd3,2)
  if spd3 > 70:
    print ("It was speeding\nThe car was going at", rspd3)
    counter = (counter +1)
  elif spd3 > 0:
    print ("It was not speeding\nThe car was going at", rspd3)
  else:
    print ("Please find the drivers and arrest them")
  array.append(rspd3)
  enter = input('Enter speed Yes/No\n')
print (array)
print (counter,"cars were speeding")


def func2():
  #Program takes 2 inputs of speed. calculate average to see if speed is the speed limit. the cameras are 1 mile apart.
import random
file1=open('speeds.txt', 'r+')

for i in range(5000000000):
  speed = random.randint(71,300)
  file1.write(str(speed)+ "\n")
  
file1.close()

counter = 0
file1=open('speeds.txt', 'r') 
for line in file1:
  intline= int(line)
  if intline > 70:
    counter = (counter +1)
    
file1.close()
print (counter,"were speeding")

def tkinter():
  import tkinter as tk

  window = tk.Tk()

  window.title('Hello world')
  window.geometry("300x300")
  l = Label(window, text = "Fact of the Day")
  l.config(font =("Courier", 14))

  window.mainloop()