

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())


#run(inp)


def maths():
  matharr = ["Quadraticcalculator.py"]
  mathchoice = input("Please select an option\n(1) Quadratic stuff")
  run(matharr[mathchoice])

def physics():
  physarr = ["accelerationnotime.py"]
  physchoice = input("Please select an option\n(1) Accleration, no time ")
  run(physarr[physchoice])

def computerscience():
  csarr = ["binarycalculator.py", "hex.py","8bitconverter.py","Binary.py"]
  cschoice = input("Please select an option\n(1) Binary Calculator ")
  run(csarr[cschoice])

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
  
  

