#Coding Exercise 1
#Complete the script so that it prints out the 3rd item of list serials.
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

#Coding Exercise 2
#Append the value of current to the end of the list seconds Please use the list.append() method to accomplish that.
seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)


#Coding Exercise 3
#We have a list of three strings defined in the code area. Extend the code so your program prints out the following out of that list:

#0-Document.txt, 1-Report.txt, 2-Presentation.txt

filenames =  ["Document.txt", "Report.txt", "Presentation.txt"]

for index, file in enumerate(filenames):
   
print(f"{index}-{file}"


#Coding Exercise 4 
#We have a list of two IPs in the code area.
Extend the code so your program:
1. Prompts the user to input an index (e.g., 0 or 1).
2. Depending on the user input, the program should return either You chose 100.122.133.111 or You chose 100.122.133.111

ip_addresses = ["100.122.133.111", "200.255.199.245"]

user_input=input("Enter an index (0 or 1): ")

index = int(user_input)

