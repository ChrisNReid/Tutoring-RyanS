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
  
  import math
  import time
  
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
