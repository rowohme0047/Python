
#Coding Exercise 1
#Assign some values to variables x, y, and z. Then, insert x, y, and z inside a print() function to print out the values of those variables.
x=2

y=2

z=2

print(x,y,z)

#Coding Exercise 2
#Create a program that prompts the user to input their name once. Then, the program prints out the name once with the first letter capitalized.

name = input("What's your name ?")

print(name.capitalize())


#Coding Exercise 3
#Create a program that prompts the user to input their name once. Then, the program repeatedly prints out the name with the first letter capitalized.
name = input("What is your name? ")


while True:
    
	print(name.capitalize())


#Coding Exercise 4
#Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.
while True:
    
	name = input("What is your name? ")
    
	print(name.capitalize())
