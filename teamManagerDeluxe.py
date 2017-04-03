# This following class defines Team
class Team(object):
  """Encapulates a name, age, goals, jersey and position."""
  def __init__(self,name,age,goals,jersey,position):
    self.name = name
    self.age = age
    self.goals = goals
    self.jersey = jersey
    self.position = position

  #The next following lines define the printStats function
  def getStats(self):
    print("Name:" + self.name)
    print("Age:" + self.age)
    print("Goals:" + self.goals)
    print("Jersey:" + self.jersey)
    print("Position:" + self.position)

def saveTeam(playerList, filename):
  # open the file
  my_file = open((filename), 'a')
  # write to the file
  for p in playerList:
   save(p.name + ' ' + str(p.age) + ' ' + str(p.goals) + ' ' + str(p.jersey) + ' ' + p.position + '\n')
  # close the file
  my_file.close()
  
  def loadTeam(list, filename):
  # create empty list
  list=[]
  # open the file
  my_file = open((filename), 'r')
  # read each line and create Player from it (use a loop)
  myreads = my_file.readline()
      # split each line into a list of the variables
  while myreads != '':
      splitList= myreads.split()
      list.append(Player(splitList[0], splitList[1], splitList[2], splitList[3], splitList[4]))
      # read each next line
      myreads = my_file.readline()
  # close the file
  my_file.close()
  # return the completed list
  return list

print("Hi, welcome to teamManagerDeluxe.py! What do you want to do? Enter the number of your choice and then hit Enter.")
print("(a)Start a new team")
print("(b)Open an existing file")
ab = raw_input()

if ab == "b":
  print("What's the filename for your existing team?(include the .tmd or the .txt)")
  filename = raw_input()
  list = loadTeam(list, filename)
  print("Here are all the players that were in that file.")
  
  elif ab == "a":
  print(" ")
  playerList = []

# In the following line I crated an empty list for the players called myPlayers
myPlayers = []
players = True

print("(1) Add a player")
print("(2) View all players")
print("(3) Save this file with team members")
print("(0) Exit the program")
answer = raw_input()

# The next line of code is for when the user wants to exit the program, because it won't print anything, it'll exit
while answer != "0":

# The next following lines of code are for when the user enters 1, and they have to enter the name, age, and the number of goals that the player has. A$
  if answer == "1":
    print("We need the following information about your player:")
    print("Name:")
    name = raw_input()
    print("Age:")
    age = raw_input()
    print("Goals:")
    goals = raw_input()
    print("Jersey:")
    jersey = raw_input()
    print("Position:")
    position = raw_input()

    myPlayers.append(Team(name,age,goals,jersey,position))
    print("(1) Add a player")
    print("(2) View all players")
    print("(3) Save this file with team members")
    print("(0) Exit the program")
    answer = raw_input()

# The next following lines of code are for when the  user chooses to enter 2 and it will allow them to see the stats and then ask them once again what $
  elif answer == "2":
    print("Current stats:")
    for info in myPlayers:
     info.getStats()
    print("(1) Add a player")
    print("(2) View all players")
    print("(3) Save this file with team members")
    print("(0) Exit the program")
    answer = raw_input()

  elif answer == "3":
    print("What would you like to name the file? (Remember that we will add the .tmd)")
    savedfile = raw_input()
    saveTeam(playerList, savedfile)
    print("(1) Add a player")
    print("(2) View all players")
    print("(3) Save this file with team members")
    print("(0) Exit the program")
    answer = raw_input()
