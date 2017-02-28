#this first line will welcome the user 
print("Welcome to the Haiku generator!")
#the next couple of lines will ask the user to input a line for ther haiku and thats why there is a code of raw_inpit for the user to type in their haiku
print("Provide a first line for your haiku:")
first = str(raw_input())
print("Provide a second line for your haiku:")
second = str(raw_input())
print("Provide a third line for your haiku:")
third = str(raw_input())
#the next line is asking the user where they want to write their haiku and to enter in the name of the file
print("What file would you like to write your haiku to?")
myFile = str(raw_input())
print("Done! To view your haiku, type 'cat' and the name of your file at the command line.")
#the next lines append the three lines haiku to the file by opening it and then closing it
my_File = open((myFile), "a")
my_File.write(first + '\n' + second + '\n' + third + '\n')
my_File.close()
