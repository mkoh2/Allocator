def allocator():
	principal = input('How much are you starting with?: $')
	rate = input('Please enter the interest rate (1% is .01): ')
	rate = float(rate)
	time = input('Please enter the number of years it will be saved: ')
	time += 1
	compound = input('How many times is the interest compounded a year?: ')
	annual = raw_input('Do you plan on adding funds annually? (Y/N): ')
	if annual == "Y":
		annual = input('How much do you plan on adding a year?: $')
	else:
		annual = 0
	
		print "Year %30s" % "Amount on deposit"
	
 	for time in range(1, time):
 		formula = principal * (1+rate) ** time + \
           annual * (1+rate) * ((1+rate) ** time - 1) / rate
		print "%4d%21.2f" % (time, formula)
	return principal

def start():
	print "Lets start compounding your interest."
	allocator()
	
start()