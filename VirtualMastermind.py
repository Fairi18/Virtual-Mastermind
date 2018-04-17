def getGuessFromUser():
	userGuess = input("Guess: ")
	return userGuess

def displayFeedback (feedback):
	print("Feedback: {0} {1} {2} {3}".format(feedback[0], feedback[1],
		feedback[2], feedback[3]))

def errorMessage():
	print("Error")

def finalScoreCodebreaker(numOfTurns):
	print("Score: - {0}".format(numOfTurns))

def main():
	#Test program....
	file = open("input.txt", "r")
	guess = getGuessFromUser()
	displayFeedback(guess)
	errorMessage()
	finalScoreCodebreaker(6)

# test to use github
#git add -A OR git add then file name
#git commit -m ""

main()
