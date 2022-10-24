def test1():
  print ("1")
def test2():
  print ("2")

def test3():
  print ("3")

def test4():
  print ("4")

inp = (input(""))





def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())


run(inp)