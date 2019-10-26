#Character Cipher: Affine Cipher

alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

def inverse (num):
  for x in range (100):
    if ((num*x)%26 == 1):
      return x

def numToAlpha (num):
  return (alphabets[num])
def alphaToNum (al):
  return int(alphabets.index(al))

s = input() #input string
s = s.replace(" ", "")
s = list(s) #separated into a list

tempList = []
for a in range (2, 100):
  if inverse(a) == None:
    continue

  for b in range (26):
    for x in s:
      tempList.append((inverse(a))*(int(alphaToNum(x))-b))

    for y in range (len(tempList)-2):
      if (tempList[y]%26)==19 and (tempList[y+1]%26)==7 and (tempList[y+2]%26)==4: #Seach values can be changed here
        for j in tempList:
          print (numToAlpha(j%26), end="")
        print ("\n a: %d  b: %d \n" %(a,b))
    tempList = []
