
#Coding Exercise 1
#In the coding area, we have defined a country variable.
You should write a match-case block that checks the value of the country variable and:
Prints out Hello if the value of country is "USA".
Prints out Namaste if the value of country is "India".
Prints out Hallo if the value of country is "Germany".

country = "India"
match country:
   
case "USA" :
       
	print("Hello")
   
case "India" :
       
	print("Namaste")
   
case "Germany" :
       
	print("Hallo")

#Coding Exercise 2
#Complete the code by adding a for-loop that makes the program produce the following output:
John Smith
Sen Plakay
Dora Ngacely

members = ["john smith", "sen plakay", "dora ngacely"]

for i in range(0,len(members)):
    
	print(members[i].title())

#Coding Exercise 3
#Loop over the colors items and print out the item in every loop. So, the expected output of your code would be:

11
34
98
43
45
54
54


colors = [11, 34, 98, 43, 45, 54, 54]

print(*colors, sep="\n|")


Coding Exercise 4
Create three variables mood, strength, and rank and assign a string to mood, a float to strength, and an integer to rank. The values you assign can be anything as long as they are of the correct type.

mood = "angry"
strength= 9.8
rank = 3