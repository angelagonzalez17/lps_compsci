print("How many miles away from Richmond State do you live?")
miles = int(input())
print("What is your GPA?")
GPA = float(input())


if miles <= 30  and GPA >= 2.0:
        print("You are accepted to Richmond State University")
else:
        if miles > 30 and GPA >= 2.5:
                print("What is your ACT score?")
                ACT = int(raw_input())


       elif ACT >= 18 and GPA >= 2.5:
                print("Congrats, you have been accepted to Richmond State!")

	elif ACT < 18 and GPA < 2.5:
		print("Sorry, you are not accepted to Richmond State.") 

