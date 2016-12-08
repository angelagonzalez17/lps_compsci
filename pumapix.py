# When you enter the show name, the first letter has to be capital, in order for the shows to be in alphabetical order

print("Welcome to PumaPix!")
print("Enter 5 of your favorite TV shows.")
my_list= []
shows= 0

while shows < 5:
  print("Enter a show name.")
  show= str(raw_input())
  my_list.append(show)
  shows= shows + 1
 
print("Okay, so here's what you entered:")
print(my_list)
number= 1
print("We've added a couple of important shows.")
my_list.append("How to Get Away with Murder")
my_list.append("Jane the Virgin")
my_list.sort()

for current_shows in my_list:
  print(str(number) + "." + current_shows)
  number= number + 1
