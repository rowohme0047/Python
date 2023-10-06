#Coding Exercise 1
#Create a program that:
1. Prompts the user to input a (dollar) amount.
2. Calculates the corresponding amount in euros, given an exchange rate of 2.
3. Prints out the amount in euros.


dollars = float(input("Enter the dollar amount: "))
exchange_rate = 2
euros = dollars / exchange_rate
print(f"{dollars} dollars is equal to {euros} euros.")



#Coding Exercise 2
#The ranking list given in the coding area represents the ranking of three athletes, John, Sen, and Lisa. John won 1st place, Sen got 2nd, and Lisa 3rd.
Your task is to create a program that:
1. Contains the above list.
2. Prompts the user to input a rank number.
3. Returns the person who has the given rank.

ranking = ['John', 'Sen', 'Lisa']

rank=int(input("Enter rank number: "))

match rank:
    
	case 1:
print(ranking[0])
    
	case 2:
print(ranking[1])

    	case 3:
print(ranking[2])


#Coding Exercise 3
#We have defined the same ranking list as in the previous exercise:
This time you should create a program that:
1. Contains the above list.
2 Prompts the user to input the person's name.
3. Returns the rank that person has.

ranking = ['John', 'Sen', 'Lisa']

name=input("Enter a name: ")

match name:
    
	case 'John':
        
		print(1)
    
	case 'Sen':
        
		print(2)
    
	case 'Lisa':
        
		print(3)

#Coding Exercise 4
#Create three variables mood, strength, and rank and assign a string to mood, a float to strength, and an integer to rank. 
The values you assign can be anything as long as they are of the correct type.

mood="Angry"

strength=99.9

rank=1

#Coding Exercise 5
#Create a color_codes variable and assign a tuple to it. The tuple should contain three tuples as items. 
The three tuples can contain any type of data inside them. In other words, your variable should be equal to a tuple of tuple of three items each.
t1=(1,2,3)
t2=("hello","world")

t3=("green",1,"black")

color_codes=(t1,t2,t3)