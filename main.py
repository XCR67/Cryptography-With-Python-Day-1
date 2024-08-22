#PYTHON BASICS, PASSWORD CHECKER / GENERATOR ON LINE 78
#DAY 1 - PYTHON BASICS
import random 
#^Dont type until line 21, make sure its written at the top
#This is just basics, if the students are struggling with a concept, go over it
#again with different examples
#String initilization examples
name = "Your name here"
name2 = input("Give me your name: ")
print(name)
print(name2)
#String concantanation and casting
print(name + name2 = "Type whatever here")
n = int(input("Give me a number: "))
print(str(n))
#Substrings
strExample = input("Give me a string: ")
strIndex = int(input("Give an index within the string length: ")
print(strExample[strIndex] + " < Letter at " + str(strIndex))
print(strExample[strIndex:] + " < Everything after it ")
print(strExample[:strIndex] + " < Everything before it")
#Num Initilization
num = 2
num2 = 14
#Math operation examples and using variables as parameters
sum = num + num2
print(sum)
diff = num2 - num
print(diff)
prod = num * num2
print(prod)
quot = num2 / num
print(quot)
#Random number, at this point import random
print(random.randrange(0, 9))#Note randrange will never print 9, just 0 to 8
#Examples with randrange and math
randSum = random.randrange(1, 11) + 5 #Num 1 to 10 plus 5
#if statements
myName = "Your name here"
if myName == "Jason":
  print("Your name is Jason!")
#and or operators
if myName == "Jason" or myName == "Craig":
  print("Your name is either Jason or Craig!")
myNumber = 5 #any number really
if myNumber < 10 and myNumber > 0:
  print("Your number is between 0 and 10")
if myNumber == (2 + 3):
  print("Your number is the sum of 2 and 3")
#if else
if myName == "Jason":
  print("Your name is Jason!")
else:
  print("Your name is not Jason")
#elif statements
if myNumber < 5:
  print("You have a small number")
elif myNumber == 5:
  print("Your number is equal to 5")
else:
  print("Your number is bigger than 5")
#Booleans
isBig = True
myNumber = 5 #any number really
if myNumber >= 3 + 7:
  isBig = True
  print(isBig)
else:
  isBig = False
  print(isBig)
  
if isBig:
  print("Your number is at least the sum of 3 + 7")
else:
  print("The number is small")
#Not operator
print("isBig is " + str(isBig) + " and not " + str(not isBig))
#loops and substrings
for i in range(10):
  print(i)
myName = "Your name here"
for i in range(len(myName)):
  print(myName[i])


#Checks to see if a password is secure enough
def passwordChecker(password):
  #Variable Creation, need a result string and a boolean for
  #lowercase letters, uppercase letters, numbers, and special characters
  recc = ""
  hasLow = False
  hasUpp = False
  hasNum = False
  hasSpe = False
  #Loop through each letter in the password, checking to see if it is a
  #letter(Upp), letter(Low), number, or special character
  for i in range(len(password)):
    #If the current character is a letter (Then chcecks for upper / lower)
    if password[i].isalpha(): #isAlpha() checks if it is a letter
      if password[i].upper() == password[i]:
        hasUpp = True
      else:
        hasLow = True
    #If the current character is a number
    elif password[i].isnumeric(): #isnumeric() checks if it is a number
      hasNum = True
    #If the current chracter is a special character
    else: #It must be a special character due to process of elimination
      hasSpe = True
  #Add reccomendations based off of what the password doesn't have
  #The not operators are basically asking "If hasWhatever is False"
  if len(password) < 12:
    recc += "Needs to be at least 12 chracters.\n"
  if not hasLow:
    recc += "Needs lowercase letters.\n"
  if not hasUpp:
    recc += "Needs uppercase letters.\n"
  if not hasNum:
    recc += "Needs numbers.\n"
  if not hasSpe:
    recc += "Needs special characters."
  if len(recc) < 1:
    return "Password is secure"
  else:
    return recc
#Makes a password of a given length
def passwordGenerator(length):
  #Variable creation
  result = ""
  specChar = "`~!@#$%^&*-_=+;:',<.>/?' "
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  #Loops to make a password of the given length
  for i in range(length):
    #Randomly adds a letter (Upp / low), number, or a special character
    choice = random.randrange(0, 4)
    if choice == 0:
      result += str(random.randrange(0, 9))#add num
    elif choice == 1:
      result += alpha[random.randrange(0, len(alpha) - 1)]#add capital let
    elif choice == 2:
      result += alpha[random.randrange(0, len(alpha) - 1)].lower()#add lower let
    else:
      result += specChar[random.randrange(0, len(specChar) - 1)]#add special char
  return result
#Password Checker using a randomly generated password
randpassword = passwordGenerator(16) #Can use input() instead
print(randpassword)
print(passwordChecker(randpassword))
#Password Checker with a user generated password
userpassword = input("Enter a password: ")
print(userpassword)
print(passwordChecker(userpassword))
