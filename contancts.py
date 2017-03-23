print("Welcome to your Contacts!")
print("What would you like to do?")
print("(1) Add a phone number")
print("(2) Print your full list of contacts")
print("(3) Enter a name to retrieve that contact's phone number")
print("(0) Exit the Contacts app")


allcontacts = {}
answer = 1

while answer != "0":
   answer = raw_input()

   if answer == "1":
     print("What is the name of your conact?")
     name = raw_input()
     print("What is the phone number of your contact?")
     number = raw_input()
     allcontacts[name] = number
     print("Welcome to your Contacts!")
     print("What would you like to do?")
     print("(1) Add a phone number")
     print("(2) Print your full list of contacts")
     print("(3) Enter a name to retrieve that contact's phone number")
     print("(0) Exit the Contacts app")
     
   if answer == "2":
     print(allcontacts)
     print("Welcome to your Contacts!")
     print("What would you like to do?")
     print("(1) Add a phone number")
     print("(2) Print your full list of contacts")
     print("(3) Enter a name to retrieve that contact's phone number")
     print("(0) Exit the Contacts app")

   if answer == "3":
     print("What is the name of the contact, that you would like to bring up?")
     contactname = raw_input()
     print(allcontacts[name])
     print("Welcome to your Contacts!")
     print("What would you like to do?")
     print("(1) Add a phone number")
     print("(2) Print your full list of contacts")
     print("(3) Enter a name to retrieve that contact's phone number")
     print("(0) Exit the Contacts app")
