#Coding Exercise 1
#We have a list of two IPs in the code area.
#1. Prompts the user to input an index (e.g., 0 or 1).
#2. Depending on the user input, the program should return either You chose 100.122.133.111 or You chose 100.122.133.111

ip_addresses = ["100.122.133.111", "200.255.199.245"]

user_input=input("Enter an index : ")

index = int(user_input)

if index.isdigit() and 0 <= index < len(ip_addresses):
    ip = ips[index]
    print("You chose " + ip)
else:
    print("Invalid index. Please enter 0 or 1.")

#Coding Exercise 2
#Assign a list to the variable temperatures. The list should contain three items, a float, an integer, and a string.

temperatures = [72.5, 42, "hot"]


#Coding Exercise 3
#Assign a list to the rainfall variable. The list should contain four items, a float, an integer, a string, and a list*. 
rainfallvariable = [12.5, 5, "June", [10, 20, 30]]


#Coding Exercise 4
#Remove item 1.45 from seconds.

seconds = [1.23, 1.45, 1.02, 1.11]

seconds.remove(1.45)

print(seconds)

