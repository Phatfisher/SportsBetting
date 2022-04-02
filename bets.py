from datetime import datetime
import sys


if __name__ == '__main__':

	f = open('player_bets.txt', 'a')

	# Gets the current date and time.
	f.write(datetime.today())


	# Player bets then go after

	f.close()