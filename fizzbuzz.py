# Create a program that replicates the famous game Fizz Buzz. The program will take an input, e.g. 20, and then print out the list of Fizz Buzz up to and including that number, where:
# • Any multiple of 3 is replaced by the word ‘Fizz’
# • Any multiple of 5 is replaced by the word ‘Buzz’
# • Any multiple of both 3 and 5 is replaced by the word ‘Fizzbuzz'

userinp = int(input("Please input a number\n"))
fizzbuzz = []

for i in range (1, (userinp+1)):
  fizzbuzz.append(i)
  #print (fizzbuzz)
  
for j in range(0, (len(fizzbuzz)-1)):
    if fizzbuzz[j] % 3 == 0 and fizzbuzz[j] % 5 == 0:
      fizzbuzz[j] = ("Fizzbuzz")
    elif fizzbuzz[j] % 3 == 0:
      fizzbuzz[j] = ("Fizz")
    elif fizzbuzz[j] % 5 == 0:
      fizzbuzz[j] = ("Buzz")


print (fizzbuzz)