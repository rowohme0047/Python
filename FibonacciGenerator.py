"""
	In this code a recursive function is developed to 
	generate the first n numbers of the Fibonacci series
"""

def  fibonacci(n):

	if n == 1  or n == 0:

		return n

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


numero = int(input("Enter a number: "))

if numero < 0:
	print("Invalid Number")

i = 0

print("Fibonacci series: ")

for i in range(0, numero):
	print(fibonacci(i))
