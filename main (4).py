#PYTHON BASICS, PASSWORD CHECKER / GENERATOR ON LINE 36
#DAY 1 - PYTHON BASICS
#This is just basics, if the students are struggling with a concept, go over it
#again with different examples

#String initilization examples

#Num Initilization

#Math operation examples and using variables as parameters

#Random number, at this point import random
  #Note randrange will never print 9, just 0 to 8 only

#Examples with randrange and math

#if statements

#and or operators

#if else

#elif statements

#Booleans

#Not operator

#loops and substrings




#PASSWORD CHECKER
#Check to see if a password is secure enough
#def passwordChecker(password):
  #Variable Creation, a boolean variable for lowLeters, uppLeters, nums, 
  #and sepc chars, as well as a result string

  #Loop thorugh each character in the password to check for each requirement
    #If the current character is a letter using isalpha(), then checks for upper / lower
    #If the current character is a number using isnumeric()
    #If the current chracter is a special character, though it must be a special 
    #character due to process of elimination

  #Add reccomendations based off of what the password doesn't have by asking if
  #hasWhatever is False and also reccomends it is at least 12 chars if its too
  #short


#PASSWORD GENERATOR
#Makes a password of a given length
#def passwordGenerator(length):
  #Variable creation, make a string of the alphabet and special characters
  #as well as a result string

  #Loops length times make a password of the given length
    #Randomly adds a letter (Upp / low), number, or a special character

#Password Checker using a randomly generated password

#Password Checker with a user generated password
