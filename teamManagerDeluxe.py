# This following class defines Team
class Team(object):
  """Encapulates a name, age, goals, jersey and position."""
  def __init__(self,name,age,goals,jersey,position):
    self.name = name
    self.age = age
    self.goals = goals
    self.jersey = jersey
    self.position = position

def saveTeam(playerList, filename):
  # open the file
  my_file = open(filname, "a")
  # write to the file
  for self in playerList:
   playList = []
   save(self.name + ' ' + str(self.age) + ' ' + str(self.goals) + ' ' + str(self.jersey) + ' ' + self.position + '\n')
  # close the file
  my_file.close()
  # placeholder - delete once the function is complete


  def loadTeam(filename):
    # create empty list
    empty=[]
    # open the file
# read each line and create Player from it (use a loop)


        # split each line into a list of the variables

        # read each next line

    # close the file
    filename.close()
    # return the completed list
    for info in empty:
      info.filename()
    # placeholder - delete once the function is complete
    pass

#The next following lines define the printStats function
  def getStats(self):
    seperate = getstats.split()
    print(self.name  + self.age  )
# In the following line I crated an empty list for the players called myPlayers
myPlayers = []
players = True

# In the next following lines I ask the user what they would like to view, and to enter in the number of what they choose to do
print("Hi, welcome to teamManagerDeluxe.py! What do you want to do? Enter the number of your choice and then hit Enter.")
print("(1) Add a player")
print("(2) View all players")
print("(3) Open up a file with team members")
print("(0) Exit the program")
answer = raw_input()

# The next line of code is for when the user wants to exit the program, because it won't print anything, it'll exit
while answer != "0":

# The next following lines of code are for when the user enters 1, and they have to enter the name, age, and the number of goals that the player has. After it will ask them what their next steps will be
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
    print("What do you want to do? Enter the number of your choice and then hit Enter.")
    print("(1) Add a player")
    print("(2) View all players")
    print("(3) Save your player list to a file")
    print("(0) Exit the program")
    answer = raw_input()
elif answer == "2":
    print("Current stats:")
    for info in myPlayers:
     info.getStats()
    print("What do you want to do? Enter the number of your choice and then hit Enter.")
    print("(1) Add Player")
    print("(2) View all players")
    print("(3) Save your player list to a file")
    print("(0) Exit the program")
    answer = raw_input()

  elif answer == "3":
    print("What would you like to name the file? (Remember that we will add the .tmd)")
    choice = raw_input()
    saveTeam(playerList, choice)
