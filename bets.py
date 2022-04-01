from datetime import datetime


if __name__ == '__main__':

	f = open('player_bets.txt', 'a')

	# Gets the current date and time.
	f.write(datetime.today())


	# Player bets then go after