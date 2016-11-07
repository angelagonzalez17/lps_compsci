print('How old are you?')
age = int(raw_input(17))

print('What is your GPA?')
GPA = float(raw_input(2.5))
if GPA > 3.0 and age > 16:
	print('Congrats, welcoe to Columbia!')
if GPA <= 3.0  or age <= 16:
	print('Sorry, good luck at Harvard.')
