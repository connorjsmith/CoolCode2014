#It's not the weekend :(
weekend = False

#And you still have homework to do!
#setting all your homework variables to unfinished:
math = "unfinished"
science = "unfinished"
music = "unfinished"

#The big loop
#This loop checks if it's the weekend or not:
while weekend == False:
	print "It is a weekday! :("
	#The little loop
    #This loop makes the annoying parent check in on you:
	while math == "unfinished":
		answer = raw_input ("Is your math done?\n")
		if answer != "yes":
			print "GO DO YOUR MATH!"
		else:
			math = "finished"
			print "Good job!"

	#repeat for your other subjects!


	#After you check all the subjects, see if you get more homework later!
    #Afterall, it is STILL not the weekend...
	answer = raw_input ("Is it the weekend? ")
	if answer == "yes":
		#What should go here to break the big loop?
	math = "unfinished" #you got more homework :(
	science = "unfinished"
	music = "unfinished"