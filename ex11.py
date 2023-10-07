

SECTION 8
Coding Exercise 1
Extend the given code ["John Smith", "Jay Santi", "Eva Kuki"]
 so the code capitalizes all the names and surnames of the list and then prints the new list. 
The output of your code should be as below:
['John Smith', 'Jay Santi', 'Eva Kuki']

capitalized_names = []
for name in names_list:
   
    first_name, last_name = name.split()
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    capitalized_name = f"{first_name} {last_name}"
    capitalized_names.append(capitalized_name)
print(capitalized_names)


Coding Exercise 2
Extend the given code so the code prints out a list containing the number of characters for each username.
The output of your code should be as below:
[9, 11, 11]

usernames = ["john 1990", "alberta1970", "magnola2000"]
character_counts = []
for username in usernames:
    character_count = len(username)
    character_counts.append(character_count)
print(character_counts)