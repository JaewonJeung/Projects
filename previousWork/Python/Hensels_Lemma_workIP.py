#HENSEL'S LEMMA
#Hensel's lemma solves congruences for polynomials 

def displayEq(alist, a, p): #displays the equation with coefficient list input
  print ("Your equation is: ", end =" ")
  for x in reversed(alist):
    if alist.index(x) == 0:
      print (x, end = " ")
    else:
      print ("%dX^%d" %(x, alist.index(x)), end =" + ")
  print ("= %d mod %d" %(a,p))

def derive(alist):#derives with coefficient list input
  derived = []
  for x in (alist):
    derived.append((x*alist.index(x)))
  derived = derived [1:]
  return derived

def gettingZ(p):
  alist = []
  temp = 0
  for x in range (2, p):
    if (p % x == 0):
      temp = x
      break
    else:
      temp = p
  for x in range (temp):
    alist.append(x)
  return alist

def subCalc(equation, number):
  solution = 0
  for x in equation:
    if (equation.index(x) == 0):
      solution += x
    else:
      solution += (x*(number**equation.index(x)))
  return solution

highestPower = int(input("What's the number of the highest power?"))
coef = [0] * (highestPower+1)

for x in reversed(range (highestPower+1)):
  print ("What is the coefficient of x^%d?" %x)
  coef[x] = int(input())

print ("Study the following format: a mod p")
print ("What is your 'a' value?")
aValue = int(input ())
print ("What is your 'p' value?")
mod = int(input ())

Z = gettingZ(mod)
y = subCalc(coef, 3)




