import os
import sys
import time
#^^^^^^^^^^^^^^^^^^^^^^^^^
#these are required libraries, used for different things such as clearing console, making the program sleep/pause for a period of time, etc.

#basic code to assist you in learning the basics of python.
#i included notes to tell you what everything does.

#basic terms are below:
#if (if a condition is met)
#elif (else if, if the 'if' condition is not met, it will look for another condition)
#else (else, essentially if all other if/elif statements are not met, it will continue with the code under this)

#important knowledge below:
#indentations are super important, you need to learn them very quickly, tabs make a huge difference in python.

def main():
	os.system('cls') 
	print("""
		epic math python script

		1 / add / + | addition

		github.com/joshuadupont

	""") #outputs the base message to console, what you see when you run the script.

	mathC = input("What operation would you like to use? ") #asks the user for an input, which is used below this

	if mathC == "1" or mathC == "add" or mathC == "+": #filters out the users input, if the users input is what is in the quotes, it will then proceed to go on to other code.
		aInput1 = int(input("Number 1: ")) #user input code, asks the user for input (its also a integer input, so the input will be used as integers, for this script it is required, unless you want to convert them afterwards, which i do not recommend for something so small.)
		aInput2 = int(input("Number 2: ")) #user input code, asks the user for input (its also a integer input, so the input will be used as integers, for this script it is required, unless you want to convert them afterwards, which i do not recommend for something so small.)
		additionResults = aInput1 + aInput2 #the sum of both numbers, 
		print(f'The sum of {aInput1} + {aInput2} is:\n{additionResults}')
		time.sleep(5) #puts the program to sleep for 5 seconds, aka pauses the program. 
		main() #calls back to the main definition, pretty much resets the whole thing.
	
	else: #if the input does not match one of the conditions/choices in quotes in the if statement, it will go to this chunk of code. 
		print("Please input a valid operation.") #outputs to console that the choice is invalid.
		time.sleep(5) #puts the program to sleep for 5 seconds, aka pauses the program. 
		main() #calls back to the main definition, pretty much resets the whole thing.

main() #starts the program, if i were to not include a def() main:, then we would not need to do this.