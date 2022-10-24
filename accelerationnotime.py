import math
import time
def acceleration():
    for i in range(100):
        print('\n')
    acc1 = input("Acceleration = (Final velocity - Initial Velocity)/Time (1)\nFinal velocity = Acceleration x Time + Initial velocity (2)\nInitial velocity = Final velocity/(Acceleration x Time) (3)\nTime = Final velocity - Initial Velocity/Acceleration (4)\n")
    if acc1 == '1':
        t1v1 = float(input("Please enter the final velocity in m/s\n"))
        t1u1 = float(input("Please enter the initial velocity in m/s\n"))
        t1t1 = float(input("Please enter the time in seconds\n"))
        print ("a = v - u / t")
        print ("v = ",t1v1,"m/s\nu = ",t1u1,"m/s\nt = ",t1t1,"s")
        t1c1 = t1v1-t1u1
        t1a1= t1c1/t1t1
        print (t1a1,"m/s2")
        sdt1 = input("Would you like to calculate the Distance?\nYes (1)\nNo (2)\n")
        if sdt1 == "1":
            print ("v2 = u2 + 2as")
            print ("v2 - u2 = 2as")
            print ("(v2 - u2) / 2a = s")
            print ("s = (v2 - u2) / 2a")
            print ("s = (",t1v1,"-",t1u1,") / 2x",t1a1)
            t1s1 = (t1v1 - t1u1)/(2*t1a1)
            print (t1s1,"m")
            rnd1 = input("Would you like to round it?\nYes (1)\nNo (2)\n")
            if rnd1 == '1':
                t1s1r = round(t1s1, 2)
                print (t1s1r,"m")
        else:
            rnd1 = input("Would you like to round it?\nYes (1)\nNo (2)\n")
            if rnd1 == '1':
                 t1a1r = round(t1a1, 2)
                 print (t1a1r,"m")
    elif acc1 == '2':
        t1a2 = float(input("Please enter the acceleration in m/s2\n"))
        t1u2 = float(input("Please enter the initial velocity in m/s\n"))
        t1t2 = float(input("Please enter the time in seconds\n"))
        print ("a = v - u / t")
        print ("at = v - u")
        print ("at + u = v")
        print ("v = at + u")
        print ("v =",t1a2,"x",t1t2,"-",t1u2)
        t1v2 = t1a2*t1t2-t1u2
        print (t1v2,"m/s")
        sdt2 = input("Would you like to calculate the Distance?\nYes (1)\nNo (2)\n")
        if sdt2 == "1":
            print ("v2 = u2 + 2as")
            print ("v2 - u2 = 2as")
            print ("(v2 - u2) / 2a = s")
            print ("s = (v2 - u2) / 2a")
            print ("s = (",t1v2,"-",t1u2,") / 2x",t1a2)
            t1s2 = (t1v2 - t1u2)/(2*t1a2)
            print (t1s2,"m")
            rnd2 = input("Would you like to round it?\nYes (1)\nNo (2)\n")
            if rnd2 == '1':
                t1s2r = round(t1s2, 2)
                print (t1s2r,"m")
        else:
            rnd2 = input("Would you like to round it?\nYes (1)\nNo (2)\n")
            if rnd2 == '1':
                 t1a2r = round(t1a2, 2)
                 print (t1a2r,"m")
    elif acc1 == '3':
        t1v3 = float(input("Please enter the final velocity in m/s\n"))
        t1a3 = float(input("Please enter the acceleration in m/s2\n"))
        t1t3 = float(input("Please enter the time in seconds\n"))
        print ("a = v - u / t")
        print ("at = v - u")
        print ("at + u = v")
        print ("u = v - at")
        print ("u = ",t1v3,"-",t1a3,"x",t1t3)
        t1u3 = t1v3-(t1a3*t1t3)
        print (t1u3,"m/s")
        sdt2 = input("Would you like to calculate the Distance?\nYes (1)\nNo (2)\n")
        if sdt2 == "1":
            print ("v2 = u2 + 2as")
            print ("v2 - u2 = 2as")
            print ("(v2 - u2) / 2a = s")
            print ("s = (v2 - u2) / 2a")
            print ("s = (",t1v3,"-",t1u3,") / 2x",t1a3)
            t1s3 = (t1v3 - t1u3)/(2*t1a3)
            print (t1s3,"m")
            rnd3 = input("Would you like to round it?\nYes (1)\nNo (2)\n")
            if rnd3 == '1':
                t1s3r = round(t1s3, 2)
                print (t1s3r,"m")
        else:
            rnd3 = input("Would you like to round it?\nYes (1)\nNo (2)\n")
            if rnd3 == '1':
                 t1a3r = round(t1a3, 2)
                 print (t1a3r,"m")
    elif acc1 == '4':
        t1v4 = float(input("Please enter the final velocity in m/s\n"))
        t1u4 = float(input("Please enter the initial velocity in m/s\n"))
        t1a4 = float(input("Please enter the acceleration in m/s2\n"))
        print ("a = v - u / t")
        print ("at = v - u ")
        print ("t = v - u / a")
        print ("t = ",t1v4,"-",t1u4,"/",t1a4)
        t1c4 = t1v4-t1u4
        t1t4 = t1c4/t1a4
        print (t1t4,"s")
        sdt4 = input("Would you like to calculate the Distance?\nYes (1)\nNo (2)\n")
        if sdt4 == "1":
            print ("v2 = u2 + 2as")
            print ("v2 - u2 = 2as")
            print ("(v2 - u2) / 2a = s")
            print ("s = (v2 - u2) / 2a")
            print ("s = (",t1v4,"-",t1u4,") / 2x",t1a4)
            t1s4 = (t1v4 - t1u4)/(2*t1a4)
            print (t1s4,"m")
            rnd4 = input("Would you like to round it?\nYes (1)\nNo (2)\n")
            if rnd4 == '1':
                t1s4r = round(t1s4, 2)
                print (t1s4r,"m")
        else:
            rnd4 = input("Would you like to round it?\nYes (1)\nNo (2)\n")
            if rnd4 == '1':
                 t1a4r = round(t1a4, 2)
                 print (t1a4r,"m")
    else:
        print ("Please enter valid entry")
        time.sleep(3)
        acceleration ()

acceleration ()
