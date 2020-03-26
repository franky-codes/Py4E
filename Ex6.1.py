#Example - use while loop to itterate thru string & print each character
fruit = 'BANANA'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

#Exercise - use while loop to itterate thru string backwards
fruit = 'BANANA'
index = -1 # because len(fruit) - 1 is the last index in the string_x
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index - 1
