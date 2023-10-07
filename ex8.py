
#Extend the given code so the code prints out a list containing the same items as floats.
The output of your code should be as below:
[10.0, 19.1, 20.0]

user_entries = ['10', '19.1', '20']
float_entries = []
for entry in user_entries:
    float_value = float(entry)
    float_entries.append(float_value)
print(float_entries)


#Extend the given code so it prints out the sum of the numbers.
The output of your code should be as below:
49.1

user_entries = ['10', '19.1', '20']
total_sum = 0.0
for entry in user_entries:
    total_sum += float(entry)
print(total_sum)


#Write a program that:
1. asks users to enter a password.
2. returns "Great password there!" if the password has more than 7 characters. 
3. returns "Your password is weak." if the password has 7 or fewer characters. 


password = input("Enter your password: ")
if len(password) > 7:
    print("Great password there!")
else:
    print("Your password is weak.")


#Write a program that: 
1. asks users to enter a password.
2. returns "Great password there" if the password has more than 7 characters. 
*3. returns "Password is OK, but not too strong" if the password has exactly 7 characters.
4. returns "Your password is weak" if the password has 7 or fewer characters.

password = input("Enter a password: ")
if len(password) > 7:
    print("Great password there")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak")
