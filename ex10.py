
#exercise 1

file = open('bear.txt','r')

todas = file.readLines()

file.close()

for index,item in enumerate(todas):
   
 row = f"{index+1}-{item}"
    
print(row)

 #Exercise 2
Take a look at the essay.txt file tab. That file contains some text.
You should create a program that reads the essay.txt file, converts the first letter of each word to uppercase and prints out the converted text.


file= open('essay.txt','r')
text = file.read()
words = text.split()
converted = []
for word in words:
    word = word.capitalize()
    converted.append(converted)
convertedtext = ' '.join(converted)
print(convertedtext)


#Exercise 3

Write a program that reads the essay.txt file and returns the number of characters contained in the file.

file= open('essay.txt','r')
text = file.read()
count = len(text)
print(count)

#Exercise 4

Use Python to create a file with name file.txt and write the text snail there.

file= open('file.txt','w')
file.write('snail')
print('File "file.txt" has been created and the text "snail" has been written to it.')
