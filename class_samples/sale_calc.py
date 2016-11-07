cents = int(raw_input())

if cents > 1000:
	total_discount = int(cents * float(.10))
	total_cost = int(cents - total_discount)
	print('You spent over $10! Your final price is ' + str(total_cost) + ' cents.')
